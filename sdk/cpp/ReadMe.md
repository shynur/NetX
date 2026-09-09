# NetX

## 如何在你的项目中接入 SDK

### CMake User

#### 从源码 (`add_subdirectory`)

把本仓库放进你的项目 (e.g., git submodule 到 `third_party/NetX`), 然后在你的 CML 添加:

```cmake
add_subdirectory(third_party/NetX/sdk/cpp)
target_link_libraries(your_target PRIVATE NetX::netx)
```

#### 联网下载 (`FetchContent`)

```cmake
include(FetchContent)
FetchContent_Declare(
    netx
    GIT_REPOSITORY https://github.com/shynur/NetX.git
    GIT_TAG        trunk  # 自己改成所需的 branch / commit / tag
    SOURCE_SUBDIR  sdk/cpp
)
FetchContent_MakeAvailable(netx)
target_link_libraries(your_target PRIVATE NetX::netx)
```

#### 先 install 后 `find_package`

```bash
# 在当前 C++ SDK 下执行
cmake -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build
cmake --install build --prefix /usr/local
```

之后在你的项目中:

```cmake
find_package(NetX CONFIG REQUIRED)
target_link_libraries(your_target PRIVATE NetX::netx)
```

### JFrog Conan User

```bash
# 在当前 C++ SDK 下执行
conan create . --build=missing -s build_type=RelWithDebInfo
```

然后在你的 `conanfile.txt` 中声明依赖:

```ini
[requires]
netx/0.1
[generators]
CMakeDeps
CMakeToolchain
[layout]
cmake_layout
```

CML 中写:

```cmake
find_package(NetX CONFIG REQUIRED)
target_link_libraries(your_target PRIVATE NetX::netx)
```

最后用 Conan 生成的 preset 配置并构建:

```bash
conan install . --build=missing -s build_type=RelWithDebInfo
cmake --preset conan-relwithdebinfo
cmake --build --preset conan-relwithdebinfo
```
