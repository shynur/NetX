## 添加依赖

本项目同时维护两条消费路径: Conan package (CMakeDeps 根据 `cpp_info` 现场生成配置) 与 裸 CMake (安装产物里的 `NetXConfig.cmake` + 导出 targets).  两者元数据相互独立, 因此添加依赖时需要同步修改多处.

### Conan 依赖 (第三方库)

需要修改 3 处:

1. `conanfile.py` → `requirements()`: 加 `self.requires("fmt/[~10]")`.  默认 traits 对大多数场景正确 (静态库的依赖会自动向消费者传递), 仅特殊情况才显式调整, 参考 Conan v2 文档的 traits 部分.
2. `CMakeLists.txt` → `find_package(<Pkg> CONFIG REQUIRED)` + `target_link_libraries(netx ... <Pkg>::<target>)`.  包名与 target 名以该依赖 recipe 里的 `cmake_file_name` / `cmake_target_name` 为准, 可能不同于包名本身 (e.g. `eigen` 暴露的是 `Eigen3::Eigen`); 用 `conan graph info .` 或 ConanCenter 页面确认.
3. `cmake/NetXConfig.cmake` → 加 `find_dependency(<Pkg>)`.  链接到静态库的依赖即使 PRIVATE 也会以 `$<LINK_ONLY:...>` 进入导出目标的 link interface (参照现有 `Threads::Threads`), 所以 PRIVATE / PUBLIC 都需要这一行, 否则裸 CMake 消费者报「target 不存在」.

PRIVATE / PUBLIC 的选择在 CML 与 Conan 语义里保持一致: 依赖出现在公开头文件里 → PUBLIC, 否则 PRIVATE.

普通 Conan 依赖不需要改 `package_info()`: requires 在 Conan 依赖图里, `cpp_info.requires` 会被自动填充, CMakeDeps 据此把 `NetX::netx` 接到依赖的 target 上, package_id 也会追踪依赖版本.
只有「图外」的依赖才需要手动声明 — 即系统库 (见下节), 以及 macOS 的系统 framework (`cpp_info.frameworks`).

### 系统库 (Threads, `dl`, `m` 等)

系统库不是 Conan requires, 不要写进 `requirements()`:

- `CMakeLists.txt` 照常 `find_package` + 链接.
- `conanfile.py` → `package_info()` 里声明对应的 `cpp_info.system_libs` (参照现有 `pthread` 的写法).  CMakeDeps 不读 CML, 缺了这行, 静态库场景下 Conan 消费者会漏链接该系统库.

### 验证

- Conan 路径: `conan create . -s:a compiler.cppstd=26`.  test_package 通过 CMakeDeps 生成的配置消费本包, 元数据缺失会在这里暴露.  注意必须 `-s:a`: 默认 profile 的 `compiler.cppstd=29` 超出 Conan 对 gcc 17 的认定范围, 会被 profile 插件拒绝.
- 裸 CMake 路径: `cmake --install` 到 staging 目录后, 用一个独立小工程 `find_package(NetX CONFIG REQUIRED)` 并链接 `NetX::netx` 验证.
