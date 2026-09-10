// 示例代码, 用于告知其它 developers 如何引入 3rd 库 (以及 conanfile.py 和 CMakeLists.txt 中要怎么配)

#include <netx/hello.hpp>
#include <fmt/format.h>
#include <iostream>

auto netx::hello_message() -> ::nlohmann::json {
    static auto cnt = 0u;
    std::cerr << ::fmt::format(
        "[info] {} called {} times\n",
        __PRETTY_FUNCTION__, ++cnt
    );

    return {
        {"author", "shynur"},
        {"message", "Hello, NetX!"},
    };
}
