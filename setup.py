from distutils.core import setup

setup(
    name='simple4sq',
    version='0.1dev',
    packages=['simple4sq'],
    install_requires=['requests'],
    license='MIT License',
    long_description=open('README.txt').read(),
)
