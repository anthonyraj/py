from distutils.core import setup, Extension

module1 = Extension('exmod',
	include_dirs=['/usr/local/include'],
	libraries=['pthread'],
	sources=['exmodmodule.c'])

setup (name = 'exmod',
	version = '1.0',
	description = 'This is an example package',
	author = 'anthonyraj',
	url = 'http://www.anthonyraj.com',
	ext_modules=[module1])