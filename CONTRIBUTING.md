# Contributing to pyseqcol development

## Development setup

### Install Python, Poetry and dependencies

- Make sure that you have Python v3 available from your path. Installation
  of this depends on your local setup. If you are using Conda, you can e.g. install
  a Python environment with:

  - `conda create -n pyseqcol python=3.10`

- Install Poetry (and follow the instructions to add poetry to your PATH):
  - `curl -sSL https://install.python-poetry.org | python3 -`

- Configure locally installed virtualenv (under `.venv`):
  - `poetry config virtualenvs.in-project true`

- Install dependencies:
  - `poetry install --with dev`


### Poetry commands to update dependencies

- Update all dependencies:
  - `poetry update`

- Update single dependency, e.g.:
  - `poetry update httpx`

- If a dependency is not updated to the latest version available on Pypi, you might need to clear
  the pip cache of poetry:
  - `poetry cache clear pypi --all`


### Running tests

- To run all tests, type:
  - `pytest`

### Configure PyCharm project for pyseqcol

- Preparation (in terminal). Note the paths to the Python and Poetry binaries:
  - `which python`
  - `which poetry`

- In Setting/Preferences dialog:
  - Select Project Interpreter (under Project: pyseqcol)
    - Click "Add interpreter" -> "Add Local Interpreter"
    - Select "Poetry Environment"
    - Click the three dots button under "Base Interpreter". Paste the path to the Python binary
    - Make sure that "Install packages from pyproject.toml" is checked
    - Under "Poetry Executable", paste the path to the Poetry binary
    - Click "OK"
  
  - Select "Project structure"
    - Make sure that the "src" directory is selected under "Source Folders"

  - Under "Editor" -> "File Types", select the tab "Ignored Files and Folders"
    - Click the "+" button
      - Type ".venv"
    - Type Enter

  - Click "OK" to save new settings

#### Setting up test configurations

  - From Run menu (in menubar) or configuration popup (by the triangle icon):
    - Select "Edit Configurations..."
      - Click "+" to add new configuration, select "Python tests"->"pytest"
        - Name: `pytest in tests`
        - Script path: select "tests" directory
        - Click OK

#### For automatic formatting and linting

The setup for automatic formatting and linting is rather complex. The main alternative is to use 
black, which is easier to set up, but it does not have as many options and the main pyseqcol developer
is opinionated against the default black setup. The yapf config is not fully defined. 

- To install git hooks that automagically format and lint before every commit:
  - `pre-commit install`

- To update pre-commit-managed dependencies to the latest repos' versions:
  - `pre-commit autoupdate`

- In PyCharm -> File Watchers:
  - Click arrow icon pointing down and to the left
  - Select `pycharm_file_watchers.xml`

#### For mypy support in PyCharm

- In PyCharm, install "Mypy" plugin (not "Mypy (Official)")
  - `which mypy` to get path to mypy binary
  - In the PyCharm settings for the mypy plugin:
    - Select the mypy binary 
    - Select `pyproject.toml` as the mypy config file
- In PyCharm Preferences/Settings->Editor->Inspections, uncheck the following:
  - "Incorrect type"
  - "Invalid type hints definitions and usages"
  - "Missing type hinting for function definition"
