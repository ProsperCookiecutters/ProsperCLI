.. GENERATED: {{cookiecutter.author_name}} @ {% now 'utc' %} -- {{cookiecutter._template}}v{{cookiecutter.template_version}}

|Show Logo|

{{ '=' * cookiecutter.project_name|length }}
{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

|build| |coverage| |docs| |release|

{{cookiecutter.project_brief}}

Getting Started
---------------

.. code-block:: bash

    pip install .
    {{cookiecutter.cli_name}} --dump_config > app_local.cfg  # for writing secrets
    {{cookiecutter.cli_name}} --config=app_local.cfg 

Meant to be installed directly or into a thin client for easy cronjobs/CLI.  

Powered by `plumbum`_

Features
--------

TODO

.. _plumbum: http://plumbum.readthedocs.io/en/latest/cli.html

.. |Show Logo| image:: http://dl.eveprosper.com/podcast/logo-colour-17_sm2.png
    :target: http://eveprosper.com
.. |build| image:: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}
.. |coverage| image:: https://coveralls.io/repos/github/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}/badge.svg?branch=master
    :target: https://coveralls.io/github/{{cookiecutter.github_name}}/{{cookiecutter.project_name}}?branch=master
.. |docs| image:: https://readthedocs.org/projects/{{cookiecutter.project_name}}/badge/?version=latest
    :target: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |release| image:: https://badge.fury.io/py/{{cookiecutter.project_name}}.svg
    :target: https://badge.fury.io/py/{{cookiecutter.project_name}}
