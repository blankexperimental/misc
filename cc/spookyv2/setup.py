# -*- encoding: utf-8 -*-

from distutils.core import setup, Extension

setup(name = 'wandy-spooky-hash',
    version = '2.0.0',
    license = 'MIT License',
    description = 'python wrapper for SpookyHash V2',
    long_description = 'python wrapper for SpookyHash V2',
    author = 'wanglijie',
    author_email = 'owandywang@gmail.com',
    url = 'https://github.com/owandywang',
    ext_modules = [
        Extension('spooky', sources = ['SpookyV2.cpp', 'py_spooky.cpp'])],
    keywords = "jenkins spooky hash v2 checksum noncryptographic",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development']
)