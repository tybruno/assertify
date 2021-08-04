from dataclasses import dataclass, field
import assertifiers.identity
from typing import Any
from typing import Optional, Union, Type, Sequence
from string import Template
from assertifier_predicate.base import AbstractAssertifierPredicate


@dataclass
class AssertifyPredicateIs(AbstractAssertifierPredicate):
    exp1: Any
    assertifier_cls: Type[assertifiers.identity.AssertifyIs] = field(
        default=assertifiers.identity.AssertifyIs, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, exp2) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(exp1=self.exp1, exp2=exp2)


@dataclass
class AssertifyPredicateIsNot(AssertifyPredicateIs):
    assertifier_cls: Type[assertifiers.identity.AssertifyIsNot] = field(
        default=assertifiers.identity.AssertifyIsNot, init=False
    )


@dataclass
class AssertifyPredicateIsInstance(AbstractAssertifierPredicate):
    cls: Any
    assertifier_cls: Type[assertifiers.identity.AssertifyIsInstance] = field(
        default=assertifiers.identity.AssertifyIsInstance, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=TypeError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, obj) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(obj=obj, cls=self.cls)


@dataclass
class AssertifyPredicateNotIsInstance(AssertifyPredicateIsInstance):
    assertifier_cls: Type[
        assertifiers.identity.AssertifyNotIsInstance
    ] = field(default=assertifiers.identity.AssertifyNotIsInstance, init=False)
