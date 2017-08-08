import distutils.core

try:
	import setuptools
except ImportError:
	pass

packages=[]

distutils.core.setup(
	name='spider',
	version = '0.4.2',
	packages=['util', 'model'],
	author='Hetao',
	author_email='hetaojun1@@sina.com',
	install_requires=packages
)

