from dataclasses import dataclass, field
import assertifiers.regex
from typing import Any
from typing import Optional, Union, Type
from string import Template
from assertifier_predicate.base import AbstractAssertifierPredicate


@dataclass
class AssertifyPredicateRaisesRegex(AbstractAssertifierPredicate):
    expected_exception: Any
    kwargs: Any
    assertifier_cls: Type[assertifiers.regex.AssertifyRaisesRegex] = field(
        default=assertifiers.regex.AssertifyRaisesRegex, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, expected_regex) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(
            expected_exception=self.expected_exception,
            expected_regex=expected_regex,
            **self.kwargs
        )


@dataclass
class AssertifyPredicateRaisesWarning(AbstractAssertifierPredicate):
    expected_warning: Any
    kwargs: Any
    assertifier_cls: Type[assertifiers.regex.AssertifyWarnsRegex] = field(
        default=assertifiers.regex.AssertifyWarnsRegex, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, expected_regex) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(
            expected_warning=self.expected_warning,
            expected_regex=expected_regex,
            **self.kwargs
        )


@dataclass
class AssertifyPredicateRegex(AbstractAssertifierPredicate):
    expected_regex: Any
    assertifier_cls: Type[assertifiers.regex.AssertifyRegex] = field(
        default=assertifiers.regex.AssertifyRegex, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, text) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(
            expected_regex=self.expected_regex,
            text=text,
        )


@dataclass
class AssertifyPredicateNotRegex(AbstractAssertifierPredicate):
    unexpected_regex: Any
    assertifier_cls: Type[assertifiers.regex.AssertifyNotRegex] = field(
        default=assertifiers.regex.AssertifyNotRegex, init=False
    )
    raises: Optional[
        Union[None, Type[Exception], Type[AssertionError]]
    ] = field(default=ValueError)
    msg: Optional[Union[None, str, Template]] = field(default=None)

    def __call__(self, text) -> bool:
        assertifier = self.assertifier_cls(raises=self.raises, msg=self.msg)
        return assertifier(
            unexpected_regex=self.unexpected_regex,
            text=text,
        )
