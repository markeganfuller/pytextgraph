"""Setup File."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='textgraph',
    version='2.0.0',
    author='Mark Egan-Fuller',
    author_email='markeganfuller@googlemail.com',
    description='Library for creating text based graphs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/markeganfuller/pytextgraph',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU General '
         'Public License v3 or later (GPLv3+)'),
        'Operating System :: OS Independent',
    ],
    keywords='text graph textgraph asciigraph',
    license='GPLv3+',
    packages=['textgraph'],
)
