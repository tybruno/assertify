from typing import Iterable
from assertifiers.base import Assertifier


class Assertify:
    assertifiers: Iterable[Assertifier]

    def __call__(self, predicate):
        ...


assertify = Assertify()
