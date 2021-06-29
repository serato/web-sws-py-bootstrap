# Serato Web Services Python App Bootstrap

Common functionality for building Serato Web Services (SWS) python web applications.

### Installation

I recommend using `Pipenv` for this project.


```
pipenv install -e "git+https://${TOKEN}@github.com/serato/web-sws-py-bootstrap.git@master#egg=web-sws-py-bootstrap"
```

To get the token, search for "Access token to some private repositories on GitHub" on Passpack.


### Running tests

Run the tests with:

```
pipenv install --dev
pipenv run python -m pytest
```

This will collect all the tests and run them.

