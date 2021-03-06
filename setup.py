from setuptools import setup, find_packages

setup(
    name='hackathon',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/lindobmasina/hackaton-lindo.git',
    author='Lindokuhle Masina',
    author_email='lindobmasina@gmail.com'
)
