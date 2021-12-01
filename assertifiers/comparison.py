""" Equality Assertifiers

Objects provided by this module:
    * `EqualityAssertifier`
"""
from dataclasses import (
    dataclass,
    field,
)
from typing import Any, Optional, List, Mapping, Sequence, Tuple, Set, Dict

import unittest_assertions.comparison

from assertifiers.base import BuiltinAssertionAssertifier


@dataclass
class EqualityAssertifier(BuiltinAssertionAssertifier):
    """Parent Equality Assertifier class"""

    def __call__(
        self,
        first: Any,
        second: Any,
        *args: Optional[Sequence],
        **kwargs: Optional[Mapping]
    ) -> bool:
        """Run Assertify on the `first` and `second` with `args` and `kwargs`

        Args:
            first: will be compared against `second`
            second: will be compared against `first`
            *args: Optional args
            **kwargs: Optional kwargs

        Returns:
            `True` if assertify passes and `False` if it fails
        """
        result: bool = super().__call__(
            first=first, second=second, *args, **kwargs
        )
        return result


@dataclass
class AssertifyEqual(EqualityAssertifier):
    """assertify `first` == `second`

    assertify `first` equals `second`

    Example:
        >>> assert_equal = AssertifyEqual(raises=None)
        >>> assert_equal(1,1)
        True
        >>> assert_equal(first="hello",second="hello")
        True
        >>> assert_equal(1,2)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertEqual = field(
        default=unittest_assertions.comparison.AssertEqual, init=False
    )


@dataclass
class AssertifyNotEqual(EqualityAssertifier):
    """assertify `first` != `second`

    assertify `first` does not equal `second`

    Example:
        >>> assert_equal = AssertifyNotEqual(raises=None)
        >>> assert_equal(1,2)
        True
        >>> assert_equal(first="foo",second="bar")
        True
        >>> assert_equal(1,1)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertNotEqual = field(
        default=unittest_assertions.comparison.AssertNotEqual, init=False
    )


@dataclass
class AssertifyAlmostEqual(EqualityAssertifier):
    """assertify `first` ~= `second`

    assertify `first` almost equals `second`

    Example:
        >>> assert_not_almost_equal = AssertifyNotAlmostEqual(raises=None)
        >>> assert_not_almost_equal(1.00000001, 2.0)
        True
        >>> assert_not_almost_equal(first=1.1,second= 1.0,
        ... places=None, delta=0.05)
        True
        >>> assert_not_almost_equal(1.000001,1,delta=0.05)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertAlmostEqual = field(
        default=unittest_assertions.comparison.AssertAlmostEqual, init=False
    )

    def __call__(self, first: Any, second, places=None, delta=None) -> bool:
        """Assertify `first` almost equals `second`

        For more documentation read unittest.TestCase.assertSequenceEqual.__doc__

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


@dataclass
class AssertifyNotAlmostEqual(AssertifyAlmostEqual):
    """assertify `first` !~= `second`

    Assertify `first` does not almost equal `second`
    Example:
        >>> assert_almost_equal = AssertifyAlmostEqual(raises=None)
        >>> assert_almost_equal(1.00000001, 1.0)
        True
        >>> assert_almost_equal(first=1.1, second=1.0, places=None, delta=0.5)
        True
        >>> assert_almost_equal(1.00001, 2.0)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertNotAlmostEqual = (
        field(
            default=unittest_assertions.comparison.AssertNotAlmostEqual,
            init=False,
        )
    )


@dataclass
class AssertifyCountEqual(EqualityAssertifier):
    """assertify `Counter(list(first))` ==  `Counter(list(second))`

    Assertify `first` count equals `second` count

    Example:
        >>> assert_count_equal = AssertifyCountEqual(raises=None)
        >>> assert_count_equal([1,2],(1,2))
        True
        >>> assert_count_equal([],[1,2])
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertCountEqual = field(
        default=unittest_assertions.comparison.AssertCountEqual, init=False
    )


@dataclass
class AssertifyMultilineEqual(EqualityAssertifier):
    """assertify `first` multiline string == `second` multiline string

    Example:
        >>> multiline = 'line1\\nline2'
        >>> assert_multiline_equal = AssertifyMultilineEqual(raises=None)
        >>> assert_multiline_equal(first=multiline,second=multiline)
        True
        >>> assert_multiline_equal(first="",second=multiline)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertMultilineEqual = (
        field(
            default=unittest_assertions.comparison.AssertMultilineEqual,
            init=False,
        )
    )


@dataclass
class AssertifierSequenceEqual(BuiltinAssertionAssertifier):
    """assertify `seq1` == `seq2`

    asserfiy `seq1` is not equal to `seq2`

    Example:
        >>> assert_sequence_equal = AssertifierSequenceEqual(raises=None)
        >>> assert_sequence_equal((1,2.5),[1,2.5])
        True
        >>> assert_sequence_equal((1,2),[1,2.5])
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertSequanceEqual = field(
        default=unittest_assertions.comparison.AssertSequanceEqual, init=False
    )

    def __call__(self, seq1: Sequence, seq2: Sequence) -> bool:
        """Assertify `seq1` is deep equal to `seq2`

        Args:
            seq1: checks if equal to `seq2`
            seq2: checks if equal to `seq1`

        Returns:
            `True` if equal
        """
        result: bool = super().__call__(seq1=seq1, seq2=seq2)
        return result


@dataclass
class AssertifierListEqual(BuiltinAssertionAssertifier):
    """assertify `list1` == `list2`

    assertify `list1` is not equal to `list2`

    Example:
        >>> l = [1,2,3.5]
        >>> assert_list_equal = AssertifierListEqual(raises=None)
        >>> assert_list_equal(l,l)
        True
        >>> assert_list_equal([],l)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertListEqual = field(
        default=unittest_assertions.comparison.AssertListEqual, init=False
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


@dataclass
class AssertifierTupleEqual(BuiltinAssertionAssertifier):
    """assertify `tuple1` == `tuple2`

    assertify `tuple1` is not equal to `tuple2`

    For more documentation read TestCase().assertTupleEqual.__doc__

    Example:
        >>> tup = (1,2,"hello")
        >>> assert_tuple_equal = AssertifierTupleEqual(raises=None)
        >>> assert_tuple_equal(tup,tup)
        True
        >>> assert_tuple_equal((),tup)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertTupleEqual = field(
        default=unittest_assertions.comparison.AssertTupleEqual, init=False
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


@dataclass
class AssertifierSetEqual(BuiltinAssertionAssertifier):
    """assertify `set1` == `set2`

    assertify `set1` is not deep equal to `set2`

    Example:
        >>> _set = {1,2,5}
        >>> assert_set_equal = AssertifierSetEqual(raises=None)
        >>> assert_set_equal(_set,_set)
        True
        >>> assert_set_equal(_set,set())
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertSetEqual = field(
        default=unittest_assertions.comparison.AssertSetEqual, init=False
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


@dataclass
class AssertifierDictEqual(BuiltinAssertionAssertifier):
    """assertify `dic1` == `dict2`

    assertify `dict1` is deep equal to `dict2`

    Example:
        >>> _dict = {"a": 1, "b":2}
        >>> assert_dict_equal = AssertifierDictEqual(raises=None)
        >>> assert_dict_equal(_dict,_dict)
        True
        >>> assert_dict_equal(dict(),_dict)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertDictEqual = field(
        default=unittest_assertions.comparison.AssertDictEqual, init=False
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


@dataclass
class ComparisonAssertifier(BuiltinAssertionAssertifier):
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


@dataclass
class AssertifyLess(ComparisonAssertifier):
    """assertify `a` < `b`

    assertify `a` is less than `b`

    Example:
        >>> assert_less = AssertifyLess(raises=None)
        >>> assert_less(1,2)
        True
        >>> assert_less(1,1)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertLess = field(
        default=unittest_assertions.comparison.AssertLess, init=False
    )


@dataclass
class AssertifyLessEqual(ComparisonAssertifier):
    """assertify `a` <= `b`

    assertify `a` is less or equal to `b`

    Example:
        >>> assert_less = AssertifyLessEqual(raises=None)
        >>> assert_less(1,2)
        True
        >>> assert_less(2,2)
        True
        >>> assert_less(3,2)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertLessEqual = field(
        default=unittest_assertions.comparison.AssertLessEqual, init=False
    )


@dataclass
class AssertifyGreater(ComparisonAssertifier):
    """assertify `a` > `b`

    assertify `a` is greater than `b`

    Example:
        >>> assert_greater = AssertifyGreater(raises=None)
        >>> assert_greater(2,1)
        True
        >>> assert_greater(2,2)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertGreater = field(
        default=unittest_assertions.comparison.AssertGreater, init=False
    )


@dataclass
class AssertifyGreaterEqual(ComparisonAssertifier):
    """assertify `a` >= `b`

    assertify `a` is greater or equal to `b`

    Example:
        >>> assert_greater_equal = AssertifyGreaterEqual(raises=None)
        >>> assert_greater_equal(2,1)
        True
        >>> assert_greater_equal(2.0,2)
        True
        >>> assert_greater_equal(2,3)
        False
    """

    _assertion_cls: unittest_assertions.comparison.AssertGreaterEqual = field(
        default=unittest_assertions.comparison.AssertGreaterEqual, init=False
    )
