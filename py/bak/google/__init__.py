import sys
if sys.platform != 'win32':
	__import__('pkg_resources').declare_namespace(__name__)
