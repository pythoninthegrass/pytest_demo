# pytest_demo

## Summary
This is a demo project to show how to use
[pytest](https://docs.pytest.org/en/8.0.x/) with a
[flask](https://flask.palletsprojects.com/en/3.0.x/) project.

**Table of Contents**
* [pytest\_demo](#pytest_demo)
  * [Summary](#summary)
  * [Setup](#setup)
    * [Minimum requirements](#minimum-requirements)
    * [Recommended requirements](#recommended-requirements)
  * [Running tests](#running-tests)
    * [Start server](#start-server)
    * [Run test(s)](#run-tests)
    * [Stop server](#stop-server)
  * [Development](#development)
    * [Makefile](#makefile)
    * [Taskfile](#taskfile)
  * [TODO](#todo)
  * [Further Reading](#further-reading)

## Setup
### Minimum requirements
* [Python 3.11](https://www.python.org/downloads/)
* Dev dependencies
  * make
    * [Linux](https://www.gnu.org/software/make/)
    * [macOS](https://www.freecodecamp.org/news/install-xcode-command-line-tools/)
  * [editorconfig](https://editorconfig.org/)
  * [wsl](https://docs.microsoft.com/en-us/windows/wsl/setup/environment) [Windows-only]

### Recommended requirements
* [task](https://taskfile.dev/#/installation)

## Running tests
### Start server
```bash
# standalone server
./app/server.py start

# taskfile
task serve -- start
```
### Run test(s)
```bash
# all tests
pytest

# fuzzy search (can match multiple tests/files)
pytest -k app

# specific file
pytest tests/unit/test_app.py

# specific test
pytest tests/unit/test_app.py::test_index
```
### Stop server
```bash
# standalone server
./app/server.py stop

# taskfile
task serve -- stop
```

## Development
### Makefile
```bash
# install all repo dependcies
make install

# install specific repo dependencies
make <xcode|asdf|brew|devbox|pre-commit|task>
```

### Taskfile
```bash
λ task
task: [default] task --list
task: Available tasks for this project:
* default:                  Default task
* format:                   Run formatters
* install:                  Install project dependencies
* lint:                     Run linters
* pre-commit:               Run pre-commit hooks
* pyclean:                  Remove .pyc and __pycache__
* serve:                    Run the server
* test:                     Run tests
* docker:build:             Build the docker image                                                     (aliases: docker:build)
* docker:down:              Stop and remove containers, networks, and volumes with docker compose      (aliases: docker:down)
* docker:exec:              Shell into a running container                                             (aliases: docker:exec)
* docker:login:             Login to the container registry                                            (aliases: docker:login)
* docker:logs:              Follow the logs of a running container                                     (aliases: docker:logs)
* docker:net:               Create docker network                                                      (aliases: docker:net)
* docker:prune:             Prune docker                                                               (aliases: docker:prune)
* docker:push:              Push the docker image to the registry                                      (aliases: docker:push)
* docker:stop:              Stop the project with docker compose                                       (aliases: docker:stop)
* docker:up:                Start the project with docker compose                                      (aliases: docker:up)
* docker:vol:               Create docker volume                                                       (aliases: docker:vol)
* playwright:codegen:       Generate playwright code                                                   (aliases: pw:codegen)
* playwright:install:       Install playwright drivers                                                 (aliases: pw:install)
* poetry:add-pypi:          Add test-pypi repository                                                   (aliases: poetry:add-pypi)
* poetry:build:             Build the poetry bin                                                       (aliases: poetry:build)
* poetry:bump-semver:       Bump the project semantic version                                          (aliases: poetry:bump-semver)
* poetry:export-reqs:       Export requirements.txt                                                    (aliases: poetry:export-reqs)
* poetry:install:           Install project dependencies                                               (aliases: poetry:install)
* poetry:publish:           Publish the poetry bin                                                     (aliases: poetry:publish)
* poetry:update-deps:       Update dependencies                                                        (aliases: poetry:update-deps)                                           (aliases: poetry:update-deps)                                                    (aliases: poetry:update-deps)
```

## TODO
* [Open Issues](https://github.com/pythoninthegrass/pytest_demo/issues)
* Write boilerplate pytest tests

## Further Reading
* [Generating a Static Site with Flask | TestDriven.io](https://testdriven.io/blog/static-site-flask-and-netlify/)
* [Create a Static Blog Using Python Flask](https://dev.to/arrantate/create-a-static-blog-using-python-flask-1oab)
* [insomnux/flaskblog: A very simple blog with Flask and Flask-Flatpages.](https://github.com/insomnux/flaskblog)
* [Flask-FlatPages](https://flask-flatpages.readthedocs.io/en/v0.8.2/index.html#)
* [python](https://www.python.org/)
* [asdf](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf)
* [poetry](https://python-poetry.org/docs/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [pre-commit hooks](https://pre-commit.com/)
