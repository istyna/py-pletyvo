# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("QueryOption",)

import typing
from uuid import UUID

import attrs

NIL_UUID = UUID("00000000-0000-0000-0000-000000000000")


def uuid_converter(u: str) -> UUID:
    return u if isinstance(u, UUID) else UUID(u)


@attrs.define
class QueryOption:
    limit: int = attrs.field(default=0)

    order: bool = attrs.field(default=False)

    after: UUID = attrs.field(default=NIL_UUID, converter=uuid_converter)

    before: UUID = attrs.field(default=NIL_UUID, converter=uuid_converter)

    def __str__(self) -> str:
        buf: list[str] = []

        if self.limit != 0:
            buf.append(f"limit={self.limit}")

        if self.order:
            buf.append("order=asc")

        if self.after.version:
            buf.append(f"after={self.after}")

        if self.before.version:
            buf.append(f"before={self.before}")

        return "?" + "&".join(buf) if buf else ""
