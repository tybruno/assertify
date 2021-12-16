[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/tybruno/assertify/branch/main/graph/badge.svg?token=ZO94EJFI3G)](https://codecov.io/gh/tybruno/assertify)
# assertify
assertify -- assert or (ver)ify -- is a Flexible, and Extendable python3.6+ library for evaluating an expression by returning `False` or raising an `AssertionError` or the given `Exception` if the expression is invalid.

#### Key Features:
* **Easy**: Designed to make it easy to evaluate an expression and return `True`/`False` or raise an `AssertionError` or `Exception`.
* **Great Developer Experience**: Being fully typed makes it great for editor support.
* **There is More!!!**:
    * [unittest_assertions](https://github.com/tybruno/unittest_assertions): Assertify is built on top of the `unittest_assertions`, which is a library that converts the assertions from `unittest` to standalone assertions.

## Installation
```bash
pip install assertify
```
## Example
 raises an appropriate exception by default.

### Exception Example
`AssertifyIsInstance` will raise a `TypeError` by default, but you can also specify any other type of exception.

```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance()
is_instance("example str", int)  # raise TypeError("'example str' is not an instance of <class 'int'>")
```
### Assertion Example
Specify `AssertionError` to be raised

```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(raises=AssertionError)
is_instance("example str", int)  # raise AssertionError("'example str' is not an instance of <class 'int'>")
```
### Boolean Example
If `raises=None` assertify will return a `Boolean`.

```python
from assertifiers.identity import AssertifyIsInstance

is_instance = AssertifyIsInstance(raises=None)
print(is_instance("example str", int))  # False
```

### Predicate (Partial Function) Example
```python
from functools import partial
from assertifiers.identity import AssertifyIsInstances

is_instance = AssertifyIsInstances(must_be_instance_of=any)
predicate_is_instance = partial(is_instance,classes=[int,float])
print(predicate_is_instance(obj=7.62)) # True

```

# Assertifiers
## Comparison
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyEqual| assertify `first == second`| ValueError|
|AssertifyNotEqual| assertify `first != Second` | ValueError|
|AssertifyAlmostEqual| assertify  `first ~= second`| ValueError|
|AssertifyNotAlmostEqual| assertify  `first !~= second`| ValueError|
|AssertifyCountEqual| assertify  `len(first) == len(second)`| ValueError|
|AssertifyMultilineEqual| assertify  `first.splitlines() == second.splitlines()`| ValueError|
|AssertifySequenceEqual| assertify  `seq1 == seq2`| ValueError|
|AssertifyListEqual| assertify  `list1 == list2`| ValueError|
|AssertifyTupleEqual| assertify  `tuple1 == tuple2`| ValueError|
|AssertifySetEqual| assertify  `set1 == set2` | ValueError|
|AssertifyDictEqual| assertify  `dict1 == dict2`| ValueError|
|AssertifyLess| assertify  `a < b`| ValueError|
|AssertifyLessEqual| assertify  `a <= b` | ValueError|
|AssertifyGreater| assertify  `a > b` | ValueError|
|AssertifyGreater| assertify  `a >= b` | ValueError|
## Container
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyIn| assertify  `member in container`| ValueError|
|AssertifyNotIn| assertify  `member not in container` | ValueError|
## Control
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyRaises| assertify  `function raises expected_exception` | ValueError|
|AssertifyWarns| assertify  `function warns expected_warning` | ValueError|
|AssertifyLogs| assertify  `logger(level)` | ValueError|
## Identity
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyIs| assertify  `exp1 is exp2`| ValueError|
|AssertifyIsNot| assertify  `exp1 is not exp2`| ValueError|
|AssertifyIsNone| assertify  `obj is None`| ValueError|
|AssertifyIsNotNone| assertify  `obj is not None`| ValueError|
|AssertifyIsInstance| assertify  `isinstance(obj,class)` | TypeError|
|AssertifyIsInstances| assertify  `isinstance(obj,cls) for cls in classes` | TypeError|
|AssertifyIsNotInstance| assertify  `not isinstance(obj,class)` | TypeError|
|AssertifyIsNotInstances| assertify  `not isinstance(obj,cls) for cls in classes` | TypeError|
## Logic
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyTrue| assertify  `expr is True`| ValueError|
|AssertifyFalse| assertify  `expr is False` | ValueError|
## Regex
| Assertifier | Expression | raises |
|-----------------|----------------|-----------|
|AssertifyRaisesRegex| assertify  `expected_regex in expected_exception_message` | ValueError|
|AssertifyWarnsRegex| assertify `expected_regex in expected_warning_message` | ValueError|
|AssertifyRegex| assertify `text in expected_regex`| ValueError|
|AssertifyNotRegex| assertify `text not in expected_regex`| ValueError| 