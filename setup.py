from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='hello-world',
    version='1.0',
    description='My first module',
    author='Avi',
    author_email='avi@mindrocketnow.com',
    packages=['src'],  # same as name
    install_requires=[requirements],  # external packages as dependencies
)
