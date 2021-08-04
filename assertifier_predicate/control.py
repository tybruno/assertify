from dataclasses import dataclass, field
import assertifiers.control
from typing import Any
from typing import Optional, Union, Type, Sequence
from string import Template
from assertifier_predicate.base import AbstractAssertifierPredicate


@dataclass
class AssertifyPredicateLogs(AbstractAssertifierPredicate):
    level: Any = field(default=None)
    assertifier_cls: Type[assertifiers.control.AssertifyLogs] = field(
        default=assertifiers.control.AssertifyLogs, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, logger=None) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(logger=logger, level=self.level)
