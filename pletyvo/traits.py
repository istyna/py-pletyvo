# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: Sequence[str] = ("Engine",)

import typing

if typing.TYPE_CHECKING:
    from collections.abc import Sequence

    from pletyvo.types import JSONType


class Engine(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def get(self, endpoint: str) -> JSONType:
        raise NotImplementedError

    async def post(self, endpoint: str, body: JSONType) -> JSONType:
        raise NotImplementedError
