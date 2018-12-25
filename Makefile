.PHONY: release check release

release: clean
	python setup.py clean egg_info bdist_wheel sdist
	twine upload dist/pydantic*

check: clean
	find pydantic-stubs -name '*.pyi' -print0 | xargs -0 flake8
	test -e pydantic || ln -sF pydantic-stubs/ pydantic
	mypy pydantic

clean:
	rm -rf dist
	rm -rf build
	rm -rf pydantic_stubs.egg-info
	rm -rf pydantic
