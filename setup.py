"""Setup File."""
import multiprocessing
from setuptools import setup

setup(
    name='textgraph',
    version='1.0.0',
    description='Library for creating text based graphs',
    long_description=('Library for creating text based graphs, '
                      'including spark and bar graphs'),
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
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
)
