# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Signer",
    "HashService",
    "EventService",
)

import typing

if typing.TYPE_CHECKING:
    from .hash import Hash
    from .event import (
        Event,
        AuthHeader,
        EventInput,
        EventResponse,
    )
    from pletyvo.types import (
        UUIDLike,
        QueryOption,
    )


class Signer(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    @property
    def sch(cls) -> int:
        raise NotImplementedError

    def sign(self, msg: bytes) -> bytes:
        raise NotImplementedError

    @property
    def pub(self) -> bytes:
        raise NotImplementedError

    @property
    def hash(self) -> Hash:
        raise NotImplementedError

    def auth(self, msg: bytes) -> AuthHeader:
        raise NotImplementedError


class HashService(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def get_by_id(self, id: Hash) -> EventResponse:
        raise NotImplementedError


class EventService(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def get(self, option: typing.Optional[QueryOption] = None) -> list[Event]:
        raise NotImplementedError

    async def get_by_id(self, id: UUIDLike) -> typing.Optional[Event]:
        raise NotImplementedError

    async def create(self, input: EventInput) -> EventResponse:
        raise NotImplementedError
