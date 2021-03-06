import os

from setuptools import setup


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for f in files:
            path = os.path.join(root, f).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name='pydantic-stubs',
    version='0.1.2',
    description='PEP 561 type stubs for pydantic',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/vppuzakov/pydantic-stubs',
    author='Vladimir Puzakov',
    author_email='vppuzakov@gmail.com',
    packages=['pydantic-stubs'],
    install_requires=['pydantic==0.12.1'],
    python_requires=">=3.5",
    package_data=find_stubs('pydantic-stubs'),
    include_package_data=True,
    zip_safe=False,
)
