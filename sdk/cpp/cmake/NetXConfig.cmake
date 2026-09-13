include(CMakeFindDependencyMacro)
find_dependency(Threads)
find_dependency(nlohmann_json 3.12)
find_dependency(spdlog 1.17)

include(${CMAKE_CURRENT_LIST_DIR}/NetXTargets.cmake)
