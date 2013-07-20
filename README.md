#[![Build Status][travis-status]](https://travis-ci.org/mark-burnett/bank-example)

# Overview

This repository is an attempt to provide a non-trivial code base for
demonstrating the python unittest and mock modules.

The code implements a double-entry accounting system, which approximately
follows Command Query Responsibility Separation (CQRS).


# Installation

Though this module can be installed (using python setup.py install), there
isn't really much point.

If you only want to run the unit tests (not the integration tests), and don't
care about the test coverage, try:

```bash
python setup.py test
```
If you want to explore the functionality of nosetests, first you must do a
development installation of the module:

```bash
python setup.py develop
```
After that, you can run the sample code provided:

```bash
python cqrs_example.py
```


# Tests

Once you have installed the development version of the module, you can run the
tests and generate a coverage report:

```bash
nosetests --with-coverage --cover-package bank --cover-inclusive
```


# Organization

The API for the system is contained in bank/commands/ and bank/queries/.
Commands are used to modify the system, while queries are used to view system
components.

Core business logic is in bank/entities/.

CQRS-related glue is just in bank/.
