from setuptools import setup, find_packages

setup(
    name='mktd-keras-miniproject',
    version='0.1.0.dev0',
    packages=find_packages(),
    include_package_data=True,
    author='Florent',
    install_requires=open('requirements.txt', 'r').readlines()
)
