from distutils.core import setup
setup(
  name = 'tabtree',
  packages = ['tabtree'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Parsing tabbed tree formatted text files into dict node trees',
  license='MIT License',
  author = 'Fran Oviamionayi',
  author_email = 'fran.ovia@gmail.com',
  url = 'https://github.com/fran-ovia/tabtree-py',
  download_url = 'https://github.com/fran-ovia/tabtree-py/archive/v0.0.1.tar.gz',
  keywords = ['tabbed-tree', 'parsing', 'tab', 'tree'],
  tests_require=['pytest'],
  test_suite = 'tests',
  classifiers = [
    'Programming Language :: Python',
    'Development Status :: 3 - Alpha',
    'Natural Language :: English',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
)