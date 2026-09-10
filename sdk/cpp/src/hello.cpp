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
