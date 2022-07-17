# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class TunSettings(NetworkManagerSettingsMixin):
    """Tunnel Settings"""

    group: Optional[str] = field(
        metadata={'dbus_name': 'group', 'dbus_type': 's'},
        default=None,
    )
    """The group ID which will own the device. If set to NULL everyone will be
    able to use the device."""
    mode: Optional[int] = field(
        metadata={'dbus_name': 'mode', 'dbus_type': 'u'},
        default=1,
    )
    """The operating mode of the virtual device. Allowed values are
    NM_SETTING_TUN_MODE_TUN (1) to create a layer 3 device and
    NM_SETTING_TUN_MODE_TAP (2) to create an Ethernet-like layer 2 one."""
    multi_queue: Optional[bool] = field(
        metadata={'dbus_name': 'multi-queue', 'dbus_type': 'b'},
        default=False,
    )
    """If the property is set to TRUE, the interface will support multiple file
    descriptors (queues) to parallelize packet sending or receiving. Otherwise,
    the interface will only support a single queue."""
    owner: Optional[str] = field(
        metadata={'dbus_name': 'owner', 'dbus_type': 's'},
        default=None,
    )
    """The user ID which will own the device. If set to NULL everyone will be able
    to use the device."""
    pi: Optional[bool] = field(
        metadata={'dbus_name': 'pi', 'dbus_type': 'b'},
        default=False,
    )
    """If TRUE the interface will prepend a 4 byte header describing the physical
    interface to the packets."""
    vnet_hdr: Optional[bool] = field(
        metadata={'dbus_name': 'vnet-hdr', 'dbus_type': 'b'},
        default=False,
    )
    """If TRUE the IFF_VNET_HDR the tunnel packets will include a virtio network
    header."""
