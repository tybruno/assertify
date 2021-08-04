from dataclasses import dataclass, field
import assertifiers.comparison
from typing import Any
from typing import Optional, Union, Type, Sequence
from string import Template
from assertifier_predicate.base import AbstractAssertifierPredicate


@dataclass
class EqaulityPredicateAssertify(AbstractAssertifierPredicate):
    first: Any
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, second) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(first=self.first, second=second)


@dataclass
class AssertifyPredicateEqual(EqaulityPredicateAssertify):
    assertifier_cls: Type[assertifiers.comparison.AssertifyEqual] = field(
        default=assertifiers.comparison.AssertifyEqual, init=False
    )


@dataclass
class AssertifyPredicateNotEqual(EqaulityPredicateAssertify):
    assertifier_cls: Type[assertifiers.comparison.AssertifyNotEqual] = field(
        default=assertifiers.comparison.AssertifyNotEqual, init=False
    )


@dataclass
class AssertifyPredicateAlmostEqual(AbstractAssertifierPredicate):
    first: Any
    assertifier_cls: Type[
        assertifiers.comparison.AssertifyAlmostEqual
    ] = field(default=assertifiers.comparison.AssertifyAlmostEqual, init=False)
    places: Optional[int] = field(default=None)
    delta: Optional[float] = field(default=None)
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, second) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(
            first=self.first,
            second=second,
            places=self.places,
            detla=self.delta,
        )


@dataclass
class AssertifyPredicateNotAlmostEqual(AssertifyPredicateAlmostEqual):
    assertifier_cls: Type[
        assertifiers.comparison.AssertifyNotAlmostEqual
    ] = field(
        default=assertifiers.comparison.AssertifyNotAlmostEqual, init=False
    )

    def __call__(self, second) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(
            first=self.first,
            second=second,
            places=self.places,
            detla=self.delta,
        )


@dataclass
class AssertifyPredicateCountEqual(EqaulityPredicateAssertify):
    assertifier_cls: Type[assertifiers.comparison.AssertifyCountEqual] = field(
        default=assertifiers.comparison.AssertifyCountEqual, init=False
    )


@dataclass
class AssertifyPredicateMultilineEqual(EqaulityPredicateAssertify):
    assertifier_cls: Type[
        assertifiers.comparison.AssertifyMultilineEqual
    ] = field(
        default=assertifiers.comparison.AssertifyMultilineEqual, init=False
    )


@dataclass
class AssertifyPredicateSequenceEqual(AbstractAssertifierPredicate):
    seq1: Sequence
    assertifier_cls: Type[
        assertifiers.comparison.AssertifySequenceEqual
    ] = field(
        default=assertifiers.comparison.AssertifySequenceEqual, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, seq2) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(seq1=self.seq1, seq2=seq2)


@dataclass
class AssertifyPredicateListEqual(AbstractAssertifierPredicate):
    list1: list
    assertifier_cls: Type[assertifiers.comparison.AssertifyListEqual] = field(
        default=assertifiers.comparison.AssertifyListEqual, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, list2) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(list1=self.list1, list2=list2)


@dataclass
class AssertifyPredicateTupleEqual(AbstractAssertifierPredicate):
    tuple1: tuple
    assertifier_cls: Type[assertifiers.comparison.AssertifyTupleEqual] = field(
        default=assertifiers.comparison.AssertifyTupleEqual, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, tuple2) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(tuple1=self.tuple1, tuple2=tuple2)


@dataclass
class AssertifyPredicateSetEqual(AbstractAssertifierPredicate):
    set1: set
    assertifier_cls: Type[assertifiers.comparison.AssertifySetEqual] = field(
        default=assertifiers.comparison.AssertifySetEqual, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, set2) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(set1=self.set1, set2=set2)


@dataclass
class AssertifyPredicateDictEqual(AbstractAssertifierPredicate):
    dict1: dict
    assertifier_cls: Type[assertifiers.comparison.AssertifyDictEqual] = field(
        default=assertifiers.comparison.AssertifyDictEqual, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, dict2) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(dict1=self.dict1, dict2=dict2)


@dataclass
class AssertifyPredicateLess(AbstractAssertifierPredicate):
    a: Any
    assertifier_cls: Type[assertifiers.comparison.AssertifyLess] = field(
        default=assertifiers.comparison.AssertifyLess, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, b) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(a=self.a, b=b)


@dataclass
class AssertifyPredicateLess(AssertifyPredicateLess):
    assertifier_cls: Type[assertifiers.comparison.AssertifyLessEqual] = field(
        default=assertifiers.comparison.AssertifyLessEqual, init=False
    )


@dataclass
class AssertifyPredicateGreater(AssertifyPredicateLess):
    assertifier_cls: Type[assertifiers.comparison.AssertifyGreater] = field(
        default=assertifiers.comparison.AssertifyGreater, init=False
    )


@dataclass
class AssertifyPredicateGreaterEqual(AssertifyPredicateLess):
    assertifier_cls: Type[
        assertifiers.comparison.AssertifyGreaterEqual
    ] = field(
        default=assertifiers.comparison.AssertifyGreaterEqual, init=False
    )
