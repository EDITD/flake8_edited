# flake8_edited
EDITED rules for linting python

## Usage
Just add it to your requirements, ideally with a flexible version, e.g.:
```
edited_flake8>=0.0.1,<0.1
```

## Development
A version of `tox` is required to be available in your PATH:
```bash
sudo pip install tox
```

There is very minimal validation on this package, but at least to check that it
installs correctly in all supported versions of python:
```bash
tox
```