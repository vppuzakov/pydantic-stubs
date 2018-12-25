.PHONY: release
release:
	python setup.py clean egg_info bdist_wheel sdist
	twine upload dist/pydantic*

.PHONY: check
check:
	find pydantic-stubs -name '*.pyi' -print0 | xargs -0 flake8
	test -e pydantic || ln -sF pydantic-stubs/ pydantic
	mypy pydantic
