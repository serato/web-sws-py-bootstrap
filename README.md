# Serato Web Services Python App Bootstrap

Common functionality for building Serato Web Services (SWS) python web applications.

### Installation

I recommend using `Pipenv` for this project.
Add the following line under `[packages]` in `Pipfile`.

```
web-sws-py-bootstrap = {editable = true, package="~=1", git = "https://${TOKEN}@github.com/serato/web-sws-py-bootstrap.git"}
```

To get the token, search for "Access token to some private repositories on GitHub" on Passpack.

Run the following command:
```
pipenv install
```

The lines above should install the latest tag that belongs to the major version `1`.

### Running tests

Run the tests with:

```
pipenv install --dev
pipenv run python -m pytest
```

This will collect all the tests and run them.

