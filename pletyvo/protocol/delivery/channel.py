# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Channel",
    "ChannelCreateInput",
    "ChannelUpdateInput",
)

import typing

import attrs

from pletyvo.protocol import dapp


channel_name_validator = attrs.validators.max_len(40)  # type: ignore[var-annotated]


@attrs.define
class Channel(dapp.EventHeader):
    name: str = attrs.field(validator=channel_name_validator)

    author: dapp.Hash = attrs.field(converter=lambda s: dapp.Hash.from_str(s))

    def as_dict(self):
        return {
            "id": str(self.id),
            "hash": str(self.hash),
            "author": str(self.author),
            "name": str(self.name),
        }

    @classmethod
    def from_dict(cls, d: dict[str, typing.Any]) -> Channel:
        return cls(
            id=d["id"],
            hash=d["hash"],
            author=d["author"],
            name=d["name"],
        )


@attrs.define
class ChannelCreateInput:
    name: str = attrs.field(validator=channel_name_validator)

    def as_dict(self):
        return {
            "name": self.name,
        }


@attrs.define
class ChannelUpdateInput:
    name: str = attrs.field(validator=channel_name_validator)

    def as_dict(self):
        return {
            "name": self.name,
        }
