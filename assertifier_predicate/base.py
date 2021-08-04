from typing import Optional, Union, Type
from string import Template
from abc import ABC, abstractmethod
from assertifiers.base import Assertifier
from dataclasses import dataclass


class AbstractAssertifierPredicate(ABC):
    def __init__(
        self,
        assertifier_cls: Type[Assertifier],
        raises: Optional[Union[None, Type[Exception], Type[AssertionError]]],
        msg: Optional[Union[None, str, Template]],
    ):
        self.assertifier_cls = assertifier_cls
        self.raises = raises
        self.msg = msg

    @abstractmethod
    def __call__(self, **kwargs) -> bool:
        ...
