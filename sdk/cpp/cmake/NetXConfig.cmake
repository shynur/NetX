include(CMakeFindDependencyMacro)
find_dependency(Threads)
find_dependency(fmt)
find_dependency(nlohmann_json)

include(${CMAKE_CURRENT_LIST_DIR}/NetXTargets.cmake)
