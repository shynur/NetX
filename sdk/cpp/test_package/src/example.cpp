#include <netx.hpp>
#include <iostream>

int main() {
    const auto msg = ::netx::hello_message();
    std::cout << msg.dump(2) << std::endl;
}
