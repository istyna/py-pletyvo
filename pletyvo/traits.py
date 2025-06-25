# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Engine",
    "Signer",
    "HashService",
    "EventService",
    "ChannelService",
    "PostService",
    "MessageService",
)

import typing

if typing.TYPE_CHECKING:
    from .types import (
        QueryOption,
        JSONType,
        UUIDLike,
    )
    from .dapp import (
        Hash,
        Event,
        EventInput,
        EventResponse,
        AuthHeader,
    )
    from .delivery import (
        Channel,
        ChannelCreateInput,
        ChannelUpdateInput,
        Post,
        PostCreateInput,
        PostUpdateInput,
        Message,
    )


class Engine(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def get(self, endpoint: str) -> JSONType:
        raise NotImplementedError

    async def post(self, endpoint: str, body: JSONType) -> JSONType:
        raise NotImplementedError


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


class ChannelService(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def get_by_id(self, id: UUIDLike) -> Channel:
        raise NotImplementedError

    async def create(self, input: ChannelCreateInput) -> EventResponse:
        raise NotImplementedError

    async def update(self, input: ChannelUpdateInput) -> EventResponse:
        raise NotImplementedError


class MessageService(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def get(
        self,
        channel: UUIDLike,
        option: typing.Optional[QueryOption] = None,
    ) -> list[Message]:
        raise NotImplementedError

    async def get_by_id(
        self,
        channel: UUIDLike,
        id: UUIDLike,
    ) -> typing.Optional[Message]:
        raise NotImplementedError

    async def send(self, message: EventInput) -> None:
        raise NotImplementedError


class PostService(typing.Protocol):
    __slots__: typing.Sequence[str] = ()

    async def get(
        self,
        channel: UUIDLike,
        option: typing.Optional[QueryOption] = None,
    ) -> list[Post]:
        raise NotImplementedError

    async def get_by_id(self, channel: UUIDLike, id: UUIDLike) -> Post:
        raise NotImplementedError

    async def create(self, input: PostCreateInput) -> EventResponse:
        raise NotImplementedError

    async def update(self, input: PostUpdateInput) -> EventResponse:
        raise NotImplementedError
