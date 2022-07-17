# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class PppSettings(NetworkManagerSettingsMixin):
    """Point-to-Point Protocol Settings"""

    baud: Optional[int] = field(
        metadata={'dbus_name': 'baud', 'dbus_type': 'u'},
        default=None,
    )
    """If non-zero, instruct pppd to set the serial port to the specified
    baudrate.  This value should normally be left as 0 to automatically choose the
    speed."""
    crtscts: Optional[bool] = field(
        metadata={'dbus_name': 'crtscts', 'dbus_type': 'b'},
        default=False,
    )
    """If TRUE, specify that pppd should set the serial port to use hardware flow
    control with RTS and CTS signals.  This value should normally be set to
    FALSE."""
    lcp_echo_failure: Optional[int] = field(
        metadata={'dbus_name': 'lcp-echo-failure', 'dbus_type': 'u'},
        default=None,
    )
    """If non-zero, instruct pppd to presume the connection to the peer has failed
    if the specified number of LCP echo-requests go unanswered by the peer.  The
    "lcp-echo-interval" property must also be set to a non-zero value if this
    property is used."""
    lcp_echo_interval: Optional[int] = field(
        metadata={'dbus_name': 'lcp-echo-interval', 'dbus_type': 'u'},
        default=None,
    )
    """If non-zero, instruct pppd to send an LCP echo-request frame to the peer
    every n seconds (where n is the specified value).  Note that some PPP peers
    will respond to echo requests and some will not, and it is not possible to
    autodetect this."""
    mppe_stateful: Optional[bool] = field(
        metadata={'dbus_name': 'mppe-stateful', 'dbus_type': 'b'},
        default=False,
    )
    """If TRUE, stateful MPPE is used.  See pppd documentation for more
    information on stateful MPPE."""
    mru: Optional[int] = field(
        metadata={'dbus_name': 'mru', 'dbus_type': 'u'},
        default=None,
    )
    """If non-zero, instruct pppd to request that the peer send packets no larger
    than the specified size.  If non-zero, the MRU should be between 128 and
    16384."""
    mtu: Optional[int] = field(
        metadata={'dbus_name': 'mtu', 'dbus_type': 'u'},
        default=None,
    )
    """If non-zero, instruct pppd to send packets no larger than the specified
    size."""
    no_vj_comp: Optional[bool] = field(
        metadata={'dbus_name': 'no-vj-comp', 'dbus_type': 'b'},
        default=False,
    )
    noauth: Optional[bool] = field(
        metadata={'dbus_name': 'noauth', 'dbus_type': 'b'},
        default=True,
    )
    """If TRUE, do not require the other side (usually the PPP server) to
    authenticate itself to the client.  If FALSE, require authentication from the
    remote side.  In almost all cases, this should be TRUE."""
    nobsdcomp: Optional[bool] = field(
        metadata={'dbus_name': 'nobsdcomp', 'dbus_type': 'b'},
        default=False,
    )
    nodeflate: Optional[bool] = field(
        metadata={'dbus_name': 'nodeflate', 'dbus_type': 'b'},
        default=False,
    )
    refuse_chap: Optional[bool] = field(
        metadata={'dbus_name': 'refuse-chap', 'dbus_type': 'b'},
        default=False,
    )
    refuse_eap: Optional[bool] = field(
        metadata={'dbus_name': 'refuse-eap', 'dbus_type': 'b'},
        default=False,
    )
    refuse_mschap: Optional[bool] = field(
        metadata={'dbus_name': 'refuse-mschap', 'dbus_type': 'b'},
        default=False,
    )
    refuse_mschapv2: Optional[bool] = field(
        metadata={'dbus_name': 'refuse-mschapv2', 'dbus_type': 'b'},
        default=False,
    )
    refuse_pap: Optional[bool] = field(
        metadata={'dbus_name': 'refuse-pap', 'dbus_type': 'b'},
        default=False,
    )
    require_mppe: Optional[bool] = field(
        metadata={'dbus_name': 'require-mppe', 'dbus_type': 'b'},
        default=False,
    )
    """If TRUE, MPPE (Microsoft Point-to-Point Encryption) will be required for
    the PPP session.  If either 64-bit or 128-bit MPPE is not available the
    session will fail.  Note that MPPE is not used on mobile broadband
    connections."""
    require_mppe_128: Optional[bool] = field(
        metadata={'dbus_name': 'require-mppe-128', 'dbus_type': 'b'},
        default=False,
    )
    """If TRUE, 128-bit MPPE (Microsoft Point-to-Point Encryption) will be
    required for the PPP session, and the "require-mppe" property must also be set
    to TRUE.  If 128-bit MPPE is not available the session will fail."""
