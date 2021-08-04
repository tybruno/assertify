from dataclasses import dataclass, field
import assertifiers.container
from typing import Any
from typing import Optional, Union, Type, Sequence
from string import Template
from assertifier_predicate.base import AbstractAssertifierPredicate


@dataclass
class AssertifyPredicateIn(AbstractAssertifierPredicate):
    container: Any
    assertifier_cls: Type[assertifiers.container.AssertifyIn] = field(
        default=assertifiers.container.AssertifyIn, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, member) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(member=member, container=self.container)


@dataclass
class AssertifyPredicateNotIn(AssertifyPredicateIn):
    assertifier_cls: Type[assertifiers.container.AssertifyNotIn] = field(
        default=assertifiers.container.AssertifyNotIn, init=False
    )
