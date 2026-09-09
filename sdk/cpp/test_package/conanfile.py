import os

import conan
import conan.tools.build
import conan.tools.cmake


class NetxTestConan(conan.ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'CMakeToolchain', 'CMakeDeps'

    def requirements(self):
        self.requires(self.tested_reference_str)

    def layout(self):
        conan.tools.cmake.cmake_layout(self)

    def build(self):
        cmake = conan.tools.cmake.CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if conan.tools.build.can_run(self):
            cmd = os.path.join(self.cpp.build.bindir, 'example')
            self.run(cmd, env='conanrun')
