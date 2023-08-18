from collections.abc import Mapping
# TODO: py3.10: typing.Optional, typing.Union -> '|' operator
from typing import Any, TypeVar, Union

from ._compat.typing import ParamSpec, TypeAlias

T = TypeVar('T')
P = ParamSpec('P')

RawDataType: TypeAlias = Union[None, int, float, str, bool]
ListDataType: TypeAlias = list[Union[RawDataType, 'ListDataType', 'DictDataType']]
DictDataType: TypeAlias = dict[str, Union[RawDataType, ListDataType, 'DictDataType']]
NotListDataType: TypeAlias = Union[RawDataType, DictDataType]
# Equivalent to:
# JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None
DataType: TypeAlias = Union[RawDataType, ListDataType, DictDataType]
TreeData: TypeAlias = dict[str, DataType]
TreeDataPath: TypeAlias = Union[TreeData, str]  # Either TreeData or path
JsonSchema: TypeAlias = Mapping[str, Any]
