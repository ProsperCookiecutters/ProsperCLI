"""packaging for {{cookiecutter.project_name}}

GENERATED: {{cookiecutter.author_name}} @ {% now 'utc' %} -- {{cookiecutter._template}}v{{cookiecutter.template_version}}
"""
from codecs import open
import importlib

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


__package_name__ = '{{cookiecutter.project_name}}'
__library_name__ = '{{cookiecutter.library_name}}'

def get_version(package_name):
    """find __version__ for making package

    Args:
        package_name (str): path to _version.py folder (abspath > relpath)

    Returns:
        str: __version__ value

    """
    module = package_name + '._version'
    package = importlib.import_module(module)

    version = package.__version__

    return version

class PyTest(TestCommand):
    """PyTest cmdclass hook for test-at-buildtime functionality

    http://doc.pytest.org/en/latest/goodpractices.html#manual-integration

    """
    user_options = [
        ('pytest-args=', 'a', 'Arguments to pass to pytest'),
        ('secret-cfg=', None, 'secrets template for configuration'),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.secret_cfg = ''
        self.pytest_args = [
            'tests',
            '-rx',
            f'--cov={__library_name__}',
            '--cov-report=term-missing',
            '--cov-config=.coveragerc',
        ]

    def run_tests(self):
        import shlex
        import pytest
        pytest_commands = []
        try:
            pytest_commands = shlex.split(self.pytest_args)
        except AttributeError:
            pytest_commands = self.pytest_args

        if self.secret_cfg:
            pytest_commands.append(f'--secret-cfg={self.secret_cfg}')

        errno = pytest.main(pytest_commands)
        exit(errno)

setup(
    name=__package_name__,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/{{cookiecutter.github_name}}/' + __package_name__,
    download_url=f'https://github.com/{{cookiecutter.github_name}}/{__package_name__}/tarball/v{get_version(__library_name__)}',
    version=get_version(__library_name__),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
    keywords='{{cookiecutter.keywords}}',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['LICENSE', 'README.rst'],
        __library_name__: ['version.txt', 'app.cfg']
    },
    entry_points={
        'console_scripts': [
            f'{{cookiecutter.cli_name}}={__library_name__}.{{cookiecutter.cli_name}}:run_main',
        ]
    },
    package_requires='>=3.6',
    install_requires=[
        'ProsperCommon',
        'plumbum',
    ],
    tests_require=[
        'pytest',
        'pytest_cov',
        'pytest-prosper',
    ],
    extras_require={
        'dev':[
            'sphinx',
            'sphinxcontrib-napoleon',
            'semantic-version',
        ]
    },
    cmdclass={
        'test':PyTest,
    }
)
