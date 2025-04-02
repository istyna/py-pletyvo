# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("AuthHeader",)

import typing
import base64

import attrs

from .hash import Hash


@attrs.define
class AuthHeader:
    sch: int = attrs.field()

    pub: bytes = attrs.field()

    sig: bytes = attrs.field()

    def as_dict(self):
        return {
            "sch": self.sch,
            "pub": base64.b64encode(self.pub).decode("utf-8"),
            "sig": base64.b64encode(self.sig).decode("utf-8"),
        }

    @classmethod
    def from_dict(cls, d: dict[str, typing.Any]) -> AuthHeader:
        return cls(
            sch=d["sch"],
            pub=base64.b64decode(d["pub"]),
            sig=base64.b64decode(d["sig"]),
        )

    @property
    def author(self) -> Hash:
        return Hash(self.pub)
