"""test_cli: make sure user experiance works as expected
GENERATED: {{cookiecutter.author_name}} @ {% now 'utc' %} -- {{cookiecutter._template}}v{{cookiecutter.template_version}}
"""

from plumbum import local
import pytest

from {{cookiecutter.library_name}} import _version

class TestCLI:
    """validate cli launches and works as users expect"""
    app_command = local['{{cookiecutter.cli_name}}']

    def test_help(self):
        """validate -h works"""
        output = self.app_command('-h')

    def test_version(self):
        """validate app name/version are as expected"""
        output = self.app_command('--version')

        assert output.rstrip() == '{PROGNAME} {version}'.format(
            PROGNAME=_version.PROGNAME,
            version=_version.__version__,
        )
