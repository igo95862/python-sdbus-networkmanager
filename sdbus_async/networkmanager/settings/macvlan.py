# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class MacvlanSettings(NetworkManagerSettingsMixin):
    """MAC VLAN Settings"""

    mode: Optional[int] = field(
        metadata={'dbus_name': 'mode', 'dbus_type': 'u'},
        default=None,
    )
    parent: Optional[str] = field(
        metadata={'dbus_name': 'parent', 'dbus_type': 's'},
        default=None,
    )
    promiscuous: Optional[bool] = field(
        metadata={'dbus_name': 'promiscuous', 'dbus_type': 'b'},
        default=True,
    )
    tap: Optional[bool] = field(
        metadata={'dbus_name': 'tap', 'dbus_type': 'b'},
        default=False,
    )
