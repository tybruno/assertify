""" Equality Assertifiers

Objects provided by this module:
    * `AssertifyEqual`: assertify `first == second`
    * `AssertifyNotEqual`: assertify `first != second`
    * `AssertifyAlmostEqual`: assertify `first ~= second`
    * `AssertifyNotAlmostEqual`: assertify `first !~= second`
    * `AssertifyCountEqual`: assertify `len(first) == len(second)`
    * `AssertifyMultilineEqual`: assertify `first.splitlines()
    == second.splitlines()`
    * `AssertifySequenceEqual`: assertify `seq1 == seq2`
    * `AssertifyListEqual`: assertify `list1 == list2`
    * `AssertifyTupleEqual`: assertify `tuple1 == tuple2`
    * `AssertifySetEqual`: assertify `seq1 == seq2`
    * `AssertifyDictEqual`: assertify `dict1 == dict2`
    * `AssertifyLess`: assertify `a < b`
    * `AssertifyLessEqual`: assertify `a <= b`
    * `AssertifyGreater`: assertify `a > b`
    * `AssertifyGreaterEqual`: assertify `a >= b`
"""
from typing import (
    Any,
    Type,
    List,
    Sequence,
    Tuple,
    Set,
    Dict,
)

import unittest_assertions

from assertifiers.base import UnittestAssertionAssertifier


class AssertifyEqual(UnittestAssertionAssertifier):
    """assertify `first == second`

    assertify `first` equals `second`

    Example:
        >>> assertify_equal = AssertifyEqual(raises=None)
        >>> assertify_equal(1,1)
        True
        >>> assertify_equal(first="hello",second="hello")
        True
        >>> assertify_equal(1,2)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertEqual = (
        unittest_assertions.equality.AssertEqual
    )


class AssertifyNotEqual(UnittestAssertionAssertifier):
    """assertify `first != second`

    assertify `first` does not equal `second`

    Example:
        >>> assertify_equal = AssertifyNotEqual(raises=None)
        >>> assertify_equal(1,2)
        True
        >>> assertify_equal(first="foo",second="bar")
        True
        >>> assertify_equal(1,1)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertNotEqual = (
        unittest_assertions.equality.AssertNotEqual
    )


class AssertifyAlmostEqual(UnittestAssertionAssertifier):
    """assertify `first ~= second`

    Fail if the two objects are unequal as determined by their
    difference rounded to the given number of decimal places
    (default 7) and comparing to zero, or by comparing that the
    difference between the two objects is more than the given
    delta.

    Note that decimal places (from zero) are usually not the same
    as significant digits (measured from the most
    significant digit).

    If the two objects compare equal then they will automatically
    compare almost equal.

    assertify `first` almost equals `second`

    Example:
        >>> assertify_not_almost_equal = AssertifyNotAlmostEqual(raises=None)
        >>> assertify_not_almost_equal(1.00000001, 2.0)
        True
        >>> assertify_not_almost_equal(first=1.1,second= 1.0,
        ... places=None, delta=0.05)
        True
        >>> assertify_not_almost_equal(1.000001,1,delta=0.05)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertAlmostEqual = (
        unittest_assertions.equality.AssertAlmostEqual
    )

    def __call__(
        self, first: Any, second: Any, places: int = None, delta: float = None
    ) -> bool:
        """Assertify `first` almost equals `second`

        For more documentation read
        unittest.TestCase.assertSequenceEqual.__doc__

        Args:
            first: will be checked if it almost equals `second`
            second: will be checked if it almost equals `first`
            places: precision of decimal places
            delta: the amount of acceptable difference

        Returns:
            `True` if assertify passes
        """
        result: bool = super().__call__(
            first=first, second=second, places=places, delta=delta
        )
        return result


class AssertifyNotAlmostEqual(AssertifyAlmostEqual):
    """assertify `first` !~= `second`

    raise `AssertionError` if `first` is almost  equal to `second`

    For more documentation read TestCase().assertNotAlmostEqual.__doc__
    Fail if the two objects are equal as determined by their
    difference rounded to the given number of decimal places
    (default 7) and comparing to zero, or by comparing that the
    difference between the two objects is less than the given delta.

    Note that decimal places (from zero) are usually not the same
    as significant digits (measured from the most significant digit).

    Objects that are equal automatically fail.

    Assertify `first` does not almost equal `second`
    Example:
        >>> assertify_almost_equal = AssertifyAlmostEqual(raises=None)
        >>> assertify_almost_equal(1.00000001, 1.0)
        True
        >>> assertify_almost_equal(first=1.1, second=1.0,
        ... places=None, delta=0.5)
        True
        >>> assertify_almost_equal(1.00001, 2.0)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertNotAlmostEqual = (
        unittest_assertions.equality.AssertNotAlmostEqual
    )


class AssertifyCountEqual(UnittestAssertionAssertifier):
    """assertify `Counter(list(first))` ==  `Counter(list(second))`

    Asserts that two iterables have the same elements, the same number of
    times, without regard to order.

    Assertify `first` count equals `second` count

    Example:
        >>> assertify_count_equal = AssertifyCountEqual(raises=None)
        >>> assertify_count_equal([1,2],(1,2))
        True
        >>> assertify_count_equal([],[1,2])
        False
    """

    _assertion_class: unittest_assertions.equality.AssertCountEqual = (
        unittest_assertions.equality.AssertCountEqual
    )


class AssertifyMultilineEqual(UnittestAssertionAssertifier):
    """assertify `first` multiline string == `second` multiline string

    Example:
        >>> multiline = 'line1\\nline2'
        >>> assertify_multiline_equal = AssertifyMultilineEqual(raises=None)
        >>> assertify_multiline_equal(first=multiline,second=multiline)
        True
        >>> assertify_multiline_equal(first="",second=multiline)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertMultilineEqual = (
        unittest_assertions.equality.AssertMultilineEqual
    )

    def __call__(self, first: str, second: str) -> bool:
        """assertify multiline strings
        Args:
            first: multiline string to be compared against `second`
            second: multiline string to be compared against `first`

        Returns:
            `True` if assertify passes
        """
        result = super().__call__(first=first, second=second)
        return result


class AssertifySequenceEqual(UnittestAssertionAssertifier):
    """assertify `seq1` == `seq2`

    An equality assertion for ordered sequences (like lists and tuples).

    For the purposes of this function, a valid
    ordered sequence type is one
    which can be indexed, has a length, and has an equality operator.

    asserfiy `seq1` is not equal to `seq2`

    Example:
        >>> assertify_sequence_equal = AssertifySequenceEqual(raises=None)
        >>> assertify_sequence_equal((1,2.5),[1,2.5])
        True
        >>> assertify_sequence_equal((1,2),[1,2.5])
        False
    """

    _assertion_class: unittest_assertions.equality.AssertSequenceEqual = (
        unittest_assertions.equality.AssertSequenceEqual
    )

    def __call__(
        self, seq1: Sequence, seq2: Sequence, seq_type: Type = None
    ) -> bool:
        """Assertify `seq1` is deep equal to `seq2`

        Args:
            seq1: checks if equal to `seq2`
            seq2: checks if equal to `seq1`
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
        Returns:
            `True` if equal
        """
        result: bool = super().__call__(
            seq1=seq1, seq2=seq2, seq_type=seq_type
        )
        return result


class AssertifyListEqual(UnittestAssertionAssertifier):
    """assertify `list1` == `list2`

    assertify `list1` is not equal to `list2`

    Example:
        >>> l = [1,2,3.5]
        >>> assertify_list_equal = AssertifyListEqual(raises=None)
        >>> assertify_list_equal(l,l)
        True
        >>> assertify_list_equal([],l)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertListEqual = (
        unittest_assertions.equality.AssertListEqual
    )

    def __call__(self, list1: List, list2: List) -> bool:
        """assertify `list1` is deep equal to `list2`

        Args:
            list1: check if equal to `list2`
            list2: check if equal to `list1`

        Returns:
            `True` if `list1` and `list2` is equal
        """
        result: bool = super().__call__(list1=list1, list2=list2)
        return result


class AssertifyTupleEqual(UnittestAssertionAssertifier):
    """assertify `tuple1` == `tuple2`

    assertify `tuple1` is not equal to `tuple2`

    For more documentation read TestCase().assertTupleEqual.__doc__

    Example:
        >>> tup = (1,2,"hello")
        >>> assertify_tuple_equal = AssertifyTupleEqual(raises=None)
        >>> assertify_tuple_equal(tup,tup)
        True
        >>> assertify_tuple_equal((),tup)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertTupleEqual = (
        unittest_assertions.equality.AssertTupleEqual
    )

    def __call__(self, tuple1: Tuple, tuple2: Tuple) -> bool:
        """assertify `tuple1` deep equals `tuple2`

        Args:
            tuple1: check if equal to `tuple2`
            tuple2: check if equal to `tuple1`

        Returns:
            `True` if `tuple1` is deep equal to `tuple2`
        """
        result: bool = super().__call__(tuple1=tuple1, tuple2=tuple2)
        return result


class AssertifySetEqual(UnittestAssertionAssertifier):
    """assertify `set1` == `set2`

    assertify `set1` is not deep equal to `set2`

    Example:
        >>> _set = {1,2,5}
        >>> assertify_set_equal = AssertifySetEqual(raises=None)
        >>> assertify_set_equal(_set,_set)
        True
        >>> assertify_set_equal(_set,set())
        False
    """

    _assertion_class: unittest_assertions.equality.AssertSetEqual = (
        unittest_assertions.equality.AssertSetEqual
    )

    def __call__(self, set1: Set, set2: Set) -> bool:
        """assertify `set1` is deep equal to `set2`

        Args:
            set1: checks if deep equal to `set2`
            set2: checks if deep equal to `set1`

        Returns:
            `True` if `set1` is deep equal to `set2`
        """
        result: bool = super().__call__(set1=set1, set2=set2)
        return result


class AssertifyDictEqual(UnittestAssertionAssertifier):
    """assertify `dic1` == `dict2`

    assertify `dict1` is deep equal to `dict2`

    Example:
        >>> _dict = {"a": 1, "b":2}
        >>> assertify_dict_equal = AssertifyDictEqual(raises=None)
        >>> assertify_dict_equal(_dict,_dict)
        True
        >>> assertify_dict_equal(dict(),_dict)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertDictEqual = (
        unittest_assertions.equality.AssertDictEqual
    )

    def __call__(self, dict1: Dict, dict2: Dict) -> bool:
        """assertify `dict1` is deep equal to `dict2`

        Args:
            dict1: checks if deep equal to `dict2`
            dict2: checks if deep equal to `dict1`

        Returns:
            `True` if `dict1` is deep equal to `dict2`
        """
        result: bool = super().__call__(d1=dict1, d2=dict2)
        return result


class ComparisonAssertifier(UnittestAssertionAssertifier):
    """Parent class for Comparison Assertifiers"""

    def __call__(self, a: Any, b: Any) -> bool:
        """Compares `a` with `b`
        Args:
            a: compares to `b`
            b: compares to `a`

        Returns:
            `True` if `a` and `b` pass comparison
        """
        result: bool = super().__call__(a=a, b=b)
        return result


class AssertifyLess(ComparisonAssertifier):
    """assertify `a` < `b`

    assertify `a` is less than `b`

    Example:
        >>> assertify_less = AssertifyLess(raises=None)
        >>> assertify_less(1,2)
        True
        >>> assertify_less(1,1)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertLess = (
        unittest_assertions.equality.AssertLess
    )


class AssertifyLessEqual(ComparisonAssertifier):
    """assertify `a` <= `b`

    assertify `a` is less or equal to `b`

    Example:
        >>> assertify_less = AssertifyLessEqual(raises=None)
        >>> assertify_less(1,2)
        True
        >>> assertify_less(2,2)
        True
        >>> assertify_less(3,2)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertLessEqual = (
        unittest_assertions.equality.AssertLessEqual
    )


class AssertifyGreater(ComparisonAssertifier):
    """assertify `a` > `b`

    assertify `a` is greater than `b`

    Example:
        >>> assertify_greater = AssertifyGreater(raises=None)
        >>> assertify_greater(2,1)
        True
        >>> assertify_greater(2,2)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertGreater = (
        unittest_assertions.equality.AssertGreater
    )


class AssertifyGreaterEqual(ComparisonAssertifier):
    """assertify `a` >= `b`

    assertify `a` is greater or equal to `b`

    Example:
        >>> assertify_greater_equal = AssertifyGreaterEqual(raises=None)
        >>> assertify_greater_equal(2,1)
        True
        >>> assertify_greater_equal(2.0,2)
        True
        >>> assertify_greater_equal(2,3)
        False
    """

    _assertion_class: unittest_assertions.equality.AssertGreaterEqual = (
        unittest_assertions.equality.AssertGreaterEqual
    )
