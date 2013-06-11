'''
Setup File
'''
from setuptools import setup
import multiprocessing

setup(name='textgraph',
      version='0.1',
      description='Library for creating text based graphs',
      long_description=('Library for creating text based graphs, '
                        'including spark and bar graphs'),
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers'
      ],
      keywords='text graph textgraph asciigraph',
      url='https://github.com/markeganfuller/pytextgraph',
      author='Mark Egan-Fuller',
      author_email='markeganfuller@googlemail.com',
      license='',
      packages=['', 'textgraph.utils'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
