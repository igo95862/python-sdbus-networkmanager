# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class OlpcMeshSettings(NetworkManagerSettingsMixin):
    """OLPC Wireless Mesh Settings"""

    channel: Optional[int] = field(
        metadata={'dbus_name': 'channel', 'dbus_type': 'u'},
        default=None,
    )
    dhcp_anycast_address: Optional[bytes] = field(
        metadata={'dbus_name': 'dhcp-anycast-address', 'dbus_type': 'ay'},
        default=None,
    )
    """Anycast DHCP MAC address used when requesting an IP address via DHCP. The
    specific anycast address used determines which DHCP server class answers the
    request. This is currently only implemented by dhclient DHCP plugin."""
    ssid: Optional[bytes] = field(
        metadata={'dbus_name': 'ssid', 'dbus_type': 'ay'},
        default=None,
    )
