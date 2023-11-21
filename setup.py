import io
import os
import sys
from setuptools import setup, find_packages
import sys
import os.path


DESCRIPTION = "Levitation Simulation"
VERSION = '1.0.4'

sys.path.insert(0, os.path.dirname(__file__))
from _version_ import hardcoded  # We cannot import the _version module, but we can import from it.

# read readme.md
try:
    with io.open('README.md', encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

with hardcoded() as version:
    setup(
        name='levitation',
        version=version,
        description='Levitation Simulation',
        long_description=long_description,
        url="https://github.com/peng-ju/levitation",
        author="Peng Ju",
        author_email='ju26@purdue.edu',
        license="Apache-2.0",
        packages=find_packages('.'),
        python_requires='>=3.6',
        install_requires=[
            'numpy',
            'matplotlib',
            'tqdm'
            ],
        tests_require=['pytest', 'pytest-cov'],
        setup_requires=['pytest-runner'],
        include_package_data=True,
    )