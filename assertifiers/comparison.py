from dataclasses import (
    dataclass,
    field,
)

import unittest_assertions.comparison

from assertifiers.base import BuiltinAssertionAssertify


@dataclass
class EqualityAssertify(BuiltinAssertionAssertify):
    def __call__(self, first, second, **kwargs) -> bool:
        return super().__call__(first=first, second=second, **kwargs)


@dataclass
class AssertifyEqual(EqualityAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertEqual = field(
        default=unittest_assertions.comparison.AssertEqual, init=False
    )


@dataclass
class AssertifyNotEqual(EqualityAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertNotEqual = field(
        default=unittest_assertions.comparison.AssertNotEqual, init=False
    )


@dataclass
class AssertifyAlmostEqual(EqualityAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertAlmostEqual = field(
        default=unittest_assertions.comparison.AssertAlmostEqual, init=False
    )

    def __call__(self, first, second, places=None, delta=None) -> bool:
        return super().__call__(
            first=first, second=second, places=places, delta=delta
        )


@dataclass
class AssertifyNotAlmostEqual(AssertifyAlmostEqual):
    _assertion_cls: unittest_assertions.comparison.AssertNotAlmostEqual = (
        field(
            default=unittest_assertions.comparison.AssertNotAlmostEqual,
            init=False,
        )
    )


@dataclass
class AssertifyCountEqual(EqualityAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertCountEqual = field(
        default=unittest_assertions.comparison.AssertCountEqual, init=False
    )


@dataclass
class AssertifyMultilineEqual(EqualityAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertMultilineEqual = (
        field(
            default=unittest_assertions.comparison.AssertMultilineEqual,
            init=False,
        )
    )


@dataclass
class AssertifySequenceEqual(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertSequanceEqual = field(
        default=unittest_assertions.comparison.AssertSequanceEqual, init=False
    )

    def __call__(self, seq1, seq2) -> bool:
        return super().__call__(seq1=seq1, seq2=seq2)


@dataclass
class AssertifyListEqual(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertListEqual = field(
        default=unittest_assertions.comparison.AssertListEqual, init=False
    )

    def __call__(self, list1, list2) -> bool:
        return super().__call__(list1=list1, list2=list2)


@dataclass
class AssertifyTupleEqual(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertTupleEqual = field(
        default=unittest_assertions.comparison.AssertTupleEqual, init=False
    )

    def __call__(self, tuple1, tuple2) -> bool:
        return super().__call__(tuple1=tuple1, tuple2=tuple2)


@dataclass
class AssertifySetEqual(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertSetEqual = field(
        default=unittest_assertions.comparison.AssertSetEqual, init=False
    )

    def __call__(self, set1, set2) -> bool:
        return super().__call__(set1=set1, set2=set2)


@dataclass
class AssertifyDictEqual(BuiltinAssertionAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertDictEqual = field(
        default=unittest_assertions.comparison.AssertDictEqual, init=False
    )

    def __call__(self, dict1, dict2) -> bool:
        return super().__call__(d1=dict1, d2=dict2)


@dataclass
class ComparisonAssertify(BuiltinAssertionAssertify):
    def __call__(self, a, b) -> bool:
        return super().__call__(a=a, b=b)


@dataclass
class AssertifyLess(ComparisonAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertLess = field(
        default=unittest_assertions.comparison.AssertLess, init=False
    )


@dataclass
class AssertifyLessEqual(ComparisonAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertLessEqual = field(
        default=unittest_assertions.comparison.AssertLessEqual, init=False
    )


@dataclass
class AssertifyGreater(ComparisonAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertGreater = field(
        default=unittest_assertions.comparison.AssertGreater, init=False
    )


@dataclass
class AssertifyGreaterEqual(ComparisonAssertify):
    _assertion_cls: unittest_assertions.comparison.AssertGreaterEqual = field(
        default=unittest_assertions.comparison.AssertGreaterEqual, init=False
    )
