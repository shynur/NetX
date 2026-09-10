SHELL = /bin/bash -O globstar


.PHONY: all
all:

.PHONY: distclean
distclean:
	rm -f  CMakeUserPresets.json
	rm -rf build install
	rm -f  test_package/CMakeUserPresets.json
	rm -rf test_package/build test_package/__pycache__

%/:
	mkdir -p $@
	-chmod -R a+rwx $@
