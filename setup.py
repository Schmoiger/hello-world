import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.etup(
    name='hello-world-pkg',
    version='0.1',
    description='My first module',
    author='Schmogier',
    author_email='info@mindrocketnow.com',
    url='https://github.com/Schmoiger/hello-world'
    packages=['src'],  # same as name
    install_requires=[requirements],  # external packages as dependencies
    python_requires='>=3.6'
)
