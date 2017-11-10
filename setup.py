from os import path
from setuptools import setup, find_packages
from airtable_local_backup import __version__

HERE = path.abspath(path.dirname(__file__))
VERS = __version__
DESC = 'Script to create local backups from airtable databases'

with open(path.join(HERE, 'README.rst'), 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='airtable_local_backup',
    version=VERS,

    description=DESC,
    long_description=LONG_DESCRIPTION,

    url='https://github.com/rickh94/airtable_local_backup',
    author='Rick Henry',
    author_email='fredericmhenry@gmail.com',

    license='MIT',
    python_requires='>=3',

    packages=find_packages(),

    install_requires=[
        'requests',
        'airtable_python_wrapper',
        'boto3',
        'fs',
        'fs-s3fs',
        'better_exceptions',
        'ruamel.yaml'
    ],
    tests_require=['pytest', 'pytest-cov'],
    # setup_requires=['pytest-runner'],

)
