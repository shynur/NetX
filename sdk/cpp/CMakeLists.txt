cmake_minimum_required(VERSION 3.23)

project(NetX
    VERSION 0.1
    LANGUAGES CXX
)

#---------------- dependencies ----------------
find_package(Threads)

#---------------- libnetx ----------------
add_library(netx)
add_library(NetX::netx ALIAS netx)
target_sources(netx
    PRIVATE
        src/hello.cpp
    PUBLIC
        FILE_SET  HEADERS
        BASE_DIRS include/
        FILES
            include/netx.hpp
            include/netx/hello.hpp
)
target_link_libraries(netx
    PRIVATE
        Threads::Threads
)
target_compile_features(netx
    PUBLIC
        cxx_std_26
)
set_target_properties(netx
    PROPERTIES
        SOVERSION 0  # Break ABI 时需要手动递增 (不过 PROJECT_VERSION v0.x 阶段暂时不需要管)
)

#--------------- install -------------------
include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

install(
    TARGETS
        netx
    EXPORT
        NetXTargets
    FILE_SET
        HEADERS
)
install(
       EXPORT  NetXTargets
  DESTINATION  ${CMAKE_INSTALL_LIBDIR}/cmake/NetX
    NAMESPACE  NetX::
)
install(
    FILES
        cmake/NetXConfig.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/NetX
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/NetXConfigVersion.cmake
    COMPATIBILITY SameMajorVersion
)
install(
    FILES ${CMAKE_CURRENT_BINARY_DIR}/NetXConfigVersion.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/NetX
)
