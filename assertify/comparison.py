from dataclasses import dataclass, field
from unittest_assertions.comparison import (
    EqualityAssertion,
    ComparisonAssertion,
    AssertEqual,
    AssertNotEqual,
    AssertAlmostEqual,
    AssertCountEqual,
    AssertDictEqual,
    AssertMultilineEqual,
    AssertNotAlmostEqual,
    AssertGreater,
    AssertGreaterEqual,
    AssertLess,
    AssertLessEqual,
    AssertListEqual,
    AssertSequanceEqual,
    AssertTupleEqual,
    AssertSetEqual,
)
from assertify.base import BuiltinAssertionAssertify


@dataclass
class EqualityAssertify(BuiltinAssertionAssertify):
    def __call__(self, first, second, **kwargs) -> bool:
        return super().__call__(first=first, second=second, **kwargs)


@dataclass
class AssertifyEqual(EqualityAssertify):
    assertion_cls: EqualityAssertion = field(default=AssertEqual, init=False)


@dataclass
class AssertNotEqual(EqualityAssertify):
    assertion_cls: EqualityAssertion = field(
        default=AssertNotEqual, init=False
    )


@dataclass
class AssertAlmostEqual(EqualityAssertify):
    assertion_cls: EqualityAssertion = field(
        default=AssertAlmostEqual, init=False
    )

    def __call__(self, first, second, places=None, detla=None) -> bool:
        return super().__call__(
            first=first, second=second, places=places, delta=detla
        )


@dataclass
class AssertNotAlmostEqual(AssertAlmostEqual):
    function: EqualityAssertion = field(
        default=AssertNotAlmostEqual, init=False
    )


@dataclass
class AssertifyCountEqual(EqualityAssertify):
    function: EqualityAssertion = field(default=AssertCountEqual, init=False)


@dataclass
class AssertifyMultilineEqual(EqualityAssertify):
    function: EqualityAssertion = field(
        default=AssertMultilineEqual, init=False
    )


@dataclass
class SequenceEqual(BuiltinAssertionAssertify):
    assertion_cls: AssertSequanceEqual = field(
        default=AssertSequanceEqual, init=False
    )

    def __call__(self, seq1, seq2) -> bool:
        return super().__call__(seq1=seq1, seq2=seq2)


@dataclass
class ListEqual(BuiltinAssertionAssertify):
    assertion_cls: AssertListEqual = field(default=AssertListEqual, init=False)

    def __call__(self, list1, list2) -> bool:
        return super().__call__(list1=list1, list2=list2)


@dataclass
class TupleEqual(BuiltinAssertionAssertify):
    assertion_cls: AssertTupleEqual = field(
        default=AssertTupleEqual, init=False
    )

    def __call__(self, tuple1, tuple2) -> bool:
        return super().__call__(tuple1=tuple1, tuple2=tuple2)


@dataclass
class SetEqual(BuiltinAssertionAssertify):
    assertion_cls: AssertSetEqual = field(default=AssertSetEqual, init=False)

    def __call__(self, set1, set2) -> bool:
        return super().__call__(set1=set1, set2=set2)


@dataclass
class DictEqual(BuiltinAssertionAssertify):
    assertion_cls: AssertDictEqual = field(default=AssertDictEqual, init=False)

    def __call__(self, dict1, dict2) -> bool:
        return super().__call__(dict1=dict1, dict2=dict2)


@dataclass
class ComparisonAssertify(BuiltinAssertionAssertify):
    def __call__(self, a, b) -> bool:
        return super().__call__(a=a, b=b)


@dataclass
class AssertifyLess(ComparisonAssertify):
    function: ComparisonAssertion = field(default=AssertLess, init=False)


@dataclass
class AssertifyLessEqual(ComparisonAssertify):
    function: ComparisonAssertion = field(default=AssertLessEqual, init=False)


@dataclass
class AssertifyGreater(ComparisonAssertify):
    function: ComparisonAssertion = field(default=AssertGreater, init=False)


@dataclass
class AssertifyGreaterEqual(ComparisonAssertify):
    function: ComparisonAssertion = field(
        default=AssertGreaterEqual, init=False
    )
