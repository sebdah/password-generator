password-generator
==================

Simple password generator module for Python

## Installation

Install `password_generator` via `pip` with

    pip install password-generator

## Usage

The password genererator only have one function `generate`.

`password_generator.generate`(count=1, length=12, chars=ALPHNUM)

Where _count_ is how many passwords you want. _length_ is how long each password should be and _chars_ is a string with all allowed characters. Per default a-z, A-Z and 0-9 are allowed.

Some examples might be in place

    import password_generator
    password_generator.generate()
    # 'wNWPGABtM2nm'
    password_generator.generate(count=10)
    # ['zco6rUlEy7nA', 'Hi6A0JCWX3GB', 'SyYM40bFqeAi', 'S0Ll3x1KHWEG', 'DpQquSt0esH2', 'mioVPtrIE0FL', 'rZvzqWB6H9Em', 'zvb60NjcJkrt', 'riU81em0qoXP', 'sDK4jRnN9rJ1']
    password_generator.generate(count=2, length=4)
    # ['CZPY', '3qtF']
    password_generator.generate(count=2, length=4, chars='helo120')
    ['lohe', 'oe1l']

## Release notes

### 0.1.0 (2013-01-09)

- Initial release

## Updating PyPi

    python setup.py register
    python setup.py sdist upload

