# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class WireguardSettings(NetworkManagerSettingsMixin):
    """WireGuard Settings"""

    fwmark: Optional[int] = field(
        metadata={'dbus_name': 'fwmark', 'dbus_type': 'u'},
        default=None,
    )
    ip4_auto_default_route: Optional[int] = field(
        metadata={'dbus_name': 'ip4-auto-default-route', 'dbus_type': 'i'},
        default=None,
    )
    ip6_auto_default_route: Optional[int] = field(
        metadata={'dbus_name': 'ip6-auto-default-route', 'dbus_type': 'i'},
        default=None,
    )
    listen_port: Optional[int] = field(
        metadata={'dbus_name': 'listen-port', 'dbus_type': 'u'},
        default=None,
    )
    mtu: Optional[int] = field(
        metadata={'dbus_name': 'mtu', 'dbus_type': 'u'},
        default=None,
    )
    peer_routes: Optional[bool] = field(
        metadata={'dbus_name': 'peer-routes', 'dbus_type': 'b'},
        default=True,
    )
    private_key: Optional[str] = field(
        metadata={'dbus_name': 'private-key', 'dbus_type': 's'},
        default=None,
    )
    private_key_flags: Optional[int] = field(
        metadata={'dbus_name': 'private-key-flags', 'dbus_type': 'i'},
        default=None,
    )