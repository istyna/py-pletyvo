# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("Service",)

import typing

import attrs

from .dapp_service import DAppService
from .delivery_service import DeliveryService

if typing.TYPE_CHECKING:
    from . import traits


@attrs.define
class Service:
    dapp: DAppService = attrs.field()

    delivery: DeliveryService = attrs.field()

    @classmethod
    def di(cls, engine: traits.Engine, signer: traits.Signer) -> Service:
        dapp = DAppService.di(engine)
        delivery = DeliveryService.di(engine, signer, dapp.event)
        return cls(dapp, delivery)
