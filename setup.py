'''
Setup File
'''
from setuptools import setup
import multiprocessing

setup(name='textgraph',
      version='0.2',
      description='Library for creating text based graphs',
      long_description=('Library for creating text based graphs, '
                        'including spark and bar graphs'),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
      ],
      keywords='text graph textgraph asciigraph',
      url='https://github.com/markeganfuller/pytextgraph',
      author='Mark Egan-Fuller',
      author_email='markeganfuller@googlemail.com',
      license='GPLv3+',
      packages=['textgraph'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
