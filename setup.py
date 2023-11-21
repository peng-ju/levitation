import io
import os
import sys
from setuptools import setup, find_packages
import sys
import os.path


DESCRIPTION = "Levitation Simulation"
VERSION = '1.0.4'

sys.path.insert(0, os.path.dirname(__file__))
# from version import hardcoded  # We cannot import the _version module, but we can import from it.

# read readme.md
try:
    with io.open('README.md', encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


import subprocess
import os.path
import contextlib


def git_version():
    """Get the package version from git tags."""
    d = os.path.dirname(__file__)
    cmd = ['git', 'describe', '--tags', '--dirty', '--always']
    try:
        p_out = subprocess.run(cmd, cwd=d, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError:
        return {'short': None}

    # Format the version
    description = p_out.stdout.decode().strip().lstrip('Vversion')
    parts = description.split('-')
    version = {'short': parts[0]}

    if len(parts) > 1:
        version['full'] = version['short'] + '+' + '.'.join(parts[1:])
    else:
        version['full'] = version['short']

    version['release'] = '.g' not in version['full']
    version['clean'] = 'dirty' not in version['full']

    try:
        p_out = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=d, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError:
        version['git revision'] = None
    else:
        version['git revision'] = p_out.stdout.decode().strip()

    return version


version_info = git_version()
version = version_info['short']


packaged_contents = \
f'''"""File generated while packaging."""
import contextlib

version_info = {version_info}
version_info['packaged'] = True
version = '{version}'


@contextlib.contextmanager
def hardcoded():
    """Dummy context manager, returns the version."""
    yield version
'''

version_info['packaged'] = False


@contextlib.contextmanager
def hardcoded():
    """Context manager for hardcoding the version while packaging.

    Use this context managed around the `setup()` call while packaging to replace
    the dynamic git-tag versioning with a hardcoded version number.
    Will return the current version, hardcode the file for packaging, and
    restore the file afterwards.
    """
    if version is None:
        raise RuntimeError('Cannot get version from git, nothing to hardcode')

    with open(__file__, 'r') as f:
        contents = f.read()
    with open(__file__, 'w') as f:
        f.write(packaged_contents)
    try:
        yield version
    finally:
        with open(__file__, 'w') as f:
            f.write(contents)


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