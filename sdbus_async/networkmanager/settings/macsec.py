# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class MacsecSettings(NetworkManagerSettingsMixin):
    """MACSec Settings"""

    encrypt: Optional[bool] = field(
        metadata={'dbus_name': 'encrypt', 'dbus_type': 'b'},
        default=True,
    )
    mka_cak: Optional[str] = field(
        metadata={'dbus_name': 'mka-cak', 'dbus_type': 's'},
        default=None,
    )
    """The pre-shared CAK (Connectivity Association Key) for MACsec Key
    Agreement."""
    mka_cak_flags: Optional[int] = field(
        metadata={'dbus_name': 'mka-cak-flags', 'dbus_type': 'i'},
        default=None,
    )
    mka_ckn: Optional[str] = field(
        metadata={'dbus_name': 'mka-ckn', 'dbus_type': 's'},
        default=None,
    )
    """The pre-shared CKN (Connectivity-association Key Name) for MACsec Key
    Agreement."""
    mode: Optional[int] = field(
        metadata={'dbus_name': 'mode', 'dbus_type': 'i'},
        default=None,
    )
    """Specifies how the CAK (Connectivity Association Key) for MKA (MACsec Key
    Agreement) is obtained."""
    parent: Optional[str] = field(
        metadata={'dbus_name': 'parent', 'dbus_type': 's'},
        default=None,
    )
    """If given, specifies the parent interface name or parent connection UUID
    from which this MACSEC interface should be created.  If this property is not
    specified, the connection must contain an "802-3-ethernet" setting with a
    "mac-address" property."""
    port: Optional[int] = field(
        metadata={'dbus_name': 'port', 'dbus_type': 'i'},
        default=1,
    )
    """The port component of the SCI (Secure Channel Identifier), between 1 and
    65534."""
    send_sci: Optional[bool] = field(
        metadata={'dbus_name': 'send-sci', 'dbus_type': 'b'},
        default=True,
    )
    """Specifies whether the SCI (Secure Channel Identifier) is included in every
    packet."""
    validation: Optional[int] = field(
        metadata={'dbus_name': 'validation', 'dbus_type': 'i'},
        default=2,
    )
