## 如何向本项目添加第三方依赖

本项目同时维护两条 consumption 方式:
- JFrog Conan package
- 裸 CMake 项目

因此添加依赖时需要同步修改多处:
- `conanfile.py` の `requirements()`: 调用 `self.requires(...)`.
- `CMakeLists.txt`: `find_package()` + `target_link_libraries()`.
- `cmake/NetXConfig.cmake`: `find_dependency()`.
这样 consumer 才能在两种方式下都能正确使用.

每次添加依赖, 都要站在各种 consumer 的视角进行测试.

## 环境配置

### Conan

如果发现 conan 不认 `~/.conan2/profiles/default` 中设置的 `compiler.cppstd` 值,
则依次 减 3 直到合法.
