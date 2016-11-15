# -*- encoding: utf-8 -*-

from distutils.core import setup, Extension

module = Extension('lookup3',
                    define_macros = [('MAJOR_VERSION', '0'),
                                     ('MINOR_VERSION', '1')],
                    include_dirs = ['.'],
                    library_dirs = ['.'],
                    extra_compile_args=["-std=c++11", "-O2"],
                    language="c++",
                    sources = ['./lookup3.c', './py_lookup3.c'])

setup (name = 'wandy-lookup3',
       version = '0.1',
       description = 'Python bindings for fast hashing with lookup3, windows and linux',
       author = 'wanglijie',
       author_email = 'wanglijie@gmail.com',
       url = 'https://github.com/owandywang',
       long_description = 'Python bindings for fast hashing with lookup3',
       ext_modules = [module])
