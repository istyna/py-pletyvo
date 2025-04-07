# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Message",
    "MessageInput",
)

import typing
from uuid import UUID

import attrs

from pletyvo.protocol import dapp


message_content_validator = (
    attrs.validators.min_len(1),
    attrs.validators.max_len(2048),
)  # type: ignore[var-annotated]


@attrs.define(hash=True)
class Message:
    body: dapp.EventBody = attrs.field(converter=lambda s: s if isinstance(s, dapp.EventBody) else dapp.EventBody.from_str(s))

    auth: dapp.AuthHeader = attrs.field(converter=lambda d: d if isinstance(d, dapp.AuthHeader) else dapp.AuthHeader.from_dict(d))

    @classmethod
    def from_dict(cls, d: dict[str, typing.Any]) -> Message:
        return cls(
            body=d["body"],
            auth=d["auth"],
        )


@attrs.define
class MessageInput:
    id: UUID = attrs.field(converter=UUID)

    channel: dapp.Hash = attrs.field(converter=lambda s: dapp.Hash.from_str(s))

    content: str = attrs.field(validator=message_content_validator)
