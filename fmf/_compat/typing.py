from __future__ import annotations

import sys

if sys.version_info < (3, 11):
    from typing_extensions import Concatenate, ParamSpec, Self, TypeAlias

else:
    from typing import Concatenate, ParamSpec, Self, TypeAlias

__all__ = [
    "Self", "TypeAlias", "ParamSpec", "Concatenate",
    ]


def __dir__() -> list[str]:
    return __all__
