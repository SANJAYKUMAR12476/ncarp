import os
from setuptools import setup, find_namespace_packages


def __path(filename):
    return os.path.join(os.path.dirname(__file__),
                        filename)


def __get_version():
    build_number = "1.1.0"
    path_data = __path("build.info")
    if os.path.exists(path_data):
        build_data = open(path_data).read().strip()
        build_number = f"1.1.{build_data}"
    return build_number

setup(
    name='ncarp-lens-api',
    version=__get_version(),
    packages=find_namespace_packages(include=("DataApi.*",)),
    url='',
    license='MIT',
    author='Net Carbon Vision',
    author_email='chandru@netcarbonvision.com',
    description='Ncarp-api'
)
