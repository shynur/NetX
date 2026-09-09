import conan
import conan.tools.cmake


class NetXRecipe(conan.ConanFile):
    name = 'netx'
    version = '0.1'
    package_type = 'library'

    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {'shared': [True, False], 'fPIC': [True, False]}
    default_options = {'shared': True, 'fPIC': True}

    exports_sources = 'CMakeLists.txt', 'src/*', 'include/*', 'cmake/*'

    def config_options(self):
        if self.settings.os == 'Windows':
            self.options.rm_safe('fPIC')

    def configure(self):
        if self.options.shared:
            self.options.rm_safe('fPIC')

    def layout(self):
        conan.tools.cmake.cmake_layout(self)

    def requirements(self):
        # E.g., self.requires('fmt/[>=10]')
        ...

    def generate(self):
        deps = conan.tools.cmake.CMakeDeps(self)
        deps.generate()
        tc = conan.tools.cmake.CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = conan.tools.cmake.CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = conan.tools.cmake.CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property('cmake_file_name', 'NetX')
        self.cpp_info.set_property('cmake_target_name', 'NetX::netx')
        self.cpp_info.libs = ['netx']
        if self.settings.os in ['Linux', 'FreeBSD']:
            self.cpp_info.system_libs.append('pthread')
