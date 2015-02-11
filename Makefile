.PHONY: rpm egg

egg:
	python setup.py bdist_egg

rpm:
	python setup.py bdist_rpm

