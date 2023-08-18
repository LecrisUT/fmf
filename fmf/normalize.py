from types import GenericAlias
from typing import Any, Callable, overload

from ._compat.typing import Concatenate, TypeAlias
from .typing import ListDataType, NotListDataType, P, T

Normalizer: TypeAlias = Callable[Concatenate[NotListDataType, P], T]


@overload
def normalize(cls: type[T], data: NotListDataType, *args: P.args,  # type: ignore
              normalizer: Normalizer[P, T],
              **kwargs: P.kwargs) -> T:
    ...


@overload
def normalize(cls: type[T], data: NotListDataType, *args: Any,
              **kwargs: Any) -> T:
    ...


@overload
def normalize(cls: type[list[T]], data: NotListDataType, *args: P.args,  # type: ignore
              normalizer: Normalizer[P, T],
              **kwargs: P.kwargs) -> list[T]:
    ...


@overload
def normalize(cls: type[list[T]], data: NotListDataType, *args: Any,  # type: ignore
              **kwargs: Any) -> list[T]:
    ...


@overload
def normalize(cls: type[list[T]], data: ListDataType, *args: P.args,  # type: ignore
              normalizer: Normalizer[P, T],
              **kwargs: P.kwargs) -> list[T]:
    ...


@overload
def normalize(cls: type[list[T]], data: ListDataType, *args: Any,
              **kwargs: Any) -> list[T]:
    ...


def normalize(cls, data, *args, normalizer=None, **kwargs):
    if isinstance(cls, GenericAlias) and cls.__origin__ == list:
        if not isinstance(data, list):
            data = [data]
        if normalizer:
            return [normalizer(d, *args, **kwargs) for d in data]
        obj_cls = cls.__args__[0]
        return [obj_cls(d, *args, **kwargs) for d in data]
    if normalizer:
        return normalizer(data, *args, **kwargs)
    return cls(data, *args, **kwargs)
