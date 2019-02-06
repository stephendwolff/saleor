from setuptools import setup, find_packages

version = '2.2.0b2'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='saleor',
    version=version,
    install_requires=requirements,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
