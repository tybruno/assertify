[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)
# assertify
assertify -- assert (ver)ify -- is a Flexible, and Extendable python3.6+ library for boolean expressions, assertions, and verifications.

#### Key Features:
* **Easy**: Designed to make it easy to evaulate an expression and return `True`/`False` or raise an assertion or exception.
* **Great Developer Experience**: Being fully typed makes it great for editor support.
* **There is More!!!**:
    * [unittest_assertions](https://github.com/tybruno/unittest_assertions): Assertify is built on top of the `unittest_assertions`, which is a library that converts the assertions from `unittest` to standalone assertions.
    * [assertify_predicates](https://github.com/tybruno/assertify_predicates): Is an extension of Assertify which allows for assertifying predicates. This is useful for validating variables or user input.
    * [descriptify](https://github.com/tybruno/descriptify): Descriptify is a library that contians helpful python descriptors. It uses `assertify_predicates` to validate various descriptors.

## Installation
```bash
pip install "git+https://github.com/tybruno/assertify.git#egg=assertify"
```
## Example
Each Assertifier raises an appropriate exception by default.
### Exception Example
AssertifyIsInstance will raise a `TypeError` by default, but you can also specify any other type of exception.
```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(msg="Raising Exception")
is_instance("example str", int) # Raises TypeError("'example str' is not an instance of <class 'int'> : Raising Exception")
```
### Assertion Example
Specify `AssertionError` to be raised
```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(raises=AssertionError, msg="Raising AssertionError")
is_instance("example str", int) # Raises AssertionError("'example str' is not an instance of <class 'int'> : Raising AssertionError")
```
### Boolean Example
If `raises=None` assertify will return a `Boolean`.
```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(raises=None)
print(is_instance("example str", int)) # False
```
