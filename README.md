[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)
# assertify
assertify -- assert (ver)ify -- is a Flexible, and Extendable python3.6+ library for boolean expressions, assertions, and verifications.

#### Key Features:
* **Easy**: Designed to make it easy to evaulate an expression and return `True`/`False` or raise an `AssertionError` or `Exception`.
* **Great Developer Experience**: Being fully typed makes it great for editor support.
* **There is More!!!**:
    * [unittest_assertions](https://github.com/tybruno/unittest_assertions): Assertify is built on top of the `unittest_assertions`, which is a library that converts the assertions from `unittest` to standalone assertions.
    * [assertify_predicates](https://github.com/tybruno/assertify_predicates): Is an extension of Assertify which allows for assertifying predicates. This is useful for validating variables or user input.
    * [descriptify](https://github.com/tybruno/descriptify): Descriptify is a library that contians helpful python descriptors. It uses `assertify_predicates` to validate various descriptors.

## Installation
```bash
pip install assertify
```
## Example
Each Assertifier raises an appropriate exception by default.
### Exception Example
`AssertifyIsInstance` will raise a `TypeError` by default, but you can also specify any other type of exception.
```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(msg="Raising Exception")
is_instance("example str", int) # raise TypeError("'example str' is not an instance of <class 'int'> : Raising Exception")
```
### Assertion Example
Specify `AssertionError` to be raised
```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(raises=AssertionError, msg="Raising AssertionError")
is_instance("example str", int) # raise AssertionError("'example str' is not an instance of <class 'int'> : Raising AssertionError")
```
### Boolean Example
If `raises=None` assertify will return a `Boolean`.
```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(raises=None)
print(is_instance("example str", int)) # False
```
# Assertifiers
## Comparison
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyEqual| first == second| ValueError|
| AsserifyNotEqual| first != Second | ValueError|
|AssertifyAlmostEqual| first ~ second| ValueError|
|AssertifyNotAlmostEqual| first !~ second| ValueError|
|AssertifyCountEqual| len(first) == len(second)| ValueError|
|AssertifyMultilineEqual| first.splitlines() == second.splitlines()| ValueError|
|AssertifySequenceEqual| seq1 == seq2| ValueError|
|AssertifyListEqual| list1 == list2| ValueError|
|AssertifyTupleEqual| tuple1 == tuple2| ValueError|
|AssertifySetEqual| set1 == set2 | ValueError|
|AssertifyDictEqual| dict1 == dict2| ValueError|
|AssertifyLess| a < b| ValueError|
|AssertifyLessEqual| a <= b | ValueError|
|AssertifyGreater| a > b | ValueError|
|AssertifyGreater| a >= b | ValueError|
## Container
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyIn| member in container| ValueError|
| AssertifyNotIn| member not in container | ValueError|
## Control
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyRaises| excpected_exception | ValueError|
|AssertifyWarns| excpected_warning| ValueError|
|AssertifyLogs| logger(level) | ValueError|
## Identity
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyIs| exp1 is exp2| ValueError|
|AssertifyIsNot| exp1 is not exp2| ValueError|
|AssertifyIsNone| obj is None| ValueError|
|AssertifyIsNotNone| obj is not None| ValueError|
|AssertifyIsInstance|isinstance(obj,class) | TypeError|
|AssertifyIsInstances| isinstance(obj,cls) for cls in classes | TypeError|
|AssertifyIsNotInstance| not isinstance(obj,class) | TypeError|
|AssertifyIsNotInstances| not isinstance(obj,cls) for cls in classes | TypeError|
## Logic
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyTrue| expr | ValueError|
|AssertifyFalse| not expr | ValueError|
## Regex
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyRaisesRegex| expected_regex in expected_exception_message | ValueError|
|AssertifyWarnsRegex| expected_regex in expected_warning_message | ValueError|
|AssertifyRegex| text in expected_regex| ValueError|
|AssertifyNotRegex| text not in expected_regex| ValueError| 
