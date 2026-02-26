# E*TRADE API Python Sample Application

This sample Python application provides examples on using the ETRADE API endpoints.

## Table of Contents

* [Requirements](#requirements)
* [Setup](#setup)
* [Running Code](#running-code)


## Setup

1. Unzip python zip file


3. Create the virtual environment by running the Python's venv command; see the command syntax below

```
$ python3 -m venv venv
```

4. Activate the Python virtual environment

On Windows, run:

```
$ venv\Scripts\activate.bat
```

On Unix or Mac OS, run:

```
$ source venv/bin/activate
```

5. Use pip to install dependencies for the sample application

```
$ pip install -r requirements.txt
```


## Running Code

Complete these steps to run the code for the sample application:

1. Activate the Python virtual environment

On Windows, run:

```
$ venv\Scripts\activate.bat
```

On Unix or Mac OS, run:

```
$ source venv/bin/activate
```

2. Run the application

```
$ cd Playwright
$ python3 main.py
```

# How to run pytest tests
```
Run all tests in a specific file:
$ pytest tests/test_file.py

Run a specific test function within a file:
$ pytest tests/test_file.py::test_function_name

Run all tests in the current directory and subdirectories:
$ pytest
```