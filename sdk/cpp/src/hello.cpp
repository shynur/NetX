#include <netx/hello.hpp>
#include <fmt/format.h>
#include <iostream>

void netx::hello() {
    std::cout << ::fmt::format("Hello, {}!", "NetX") << std::endl;
}
