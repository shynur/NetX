#include <netx/hello.hpp>
#include <print>

void netx::hello() {
    std::println(
        "Hello, {}!",
        "NetX"
    );
}
