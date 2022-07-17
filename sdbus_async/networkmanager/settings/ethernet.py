# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class EthernetSettings(NetworkManagerSettingsMixin):
    """Wired Ethernet Settings"""

    accept_all_mac_addresses: Optional[int] = field(
        metadata={'dbus_name': 'accept-all-mac-addresses', 'dbus_type': 'i'},
        default=None,
    )
    """When TRUE, setup the interface to accept packets for all MAC addresses.
    This is enabling the kernel interface flag IFF_PROMISC. When FALSE, the
    interface will only accept the packets with the interface destination mac
    address or broadcast."""
    assigned_mac_address: Optional[str] = field(
        metadata={'dbus_name': 'assigned-mac-address', 'dbus_type': 's'},
        default=None,
    )
    """The new field for the cloned MAC address. It can be either a hardware
    address in ASCII representation, or one of the special values "preserve",
    "permanent", "random" or "stable". This field replaces the deprecated "cloned-
    mac-address" on D-Bus, which can only contain explicit hardware addresses.
    Note that this property only exists in D-Bus API. libnm and nmcli continue to
    call this property "cloned-mac-address"."""
    auto_negotiate: Optional[bool] = field(
        metadata={'dbus_name': 'auto-negotiate', 'dbus_type': 'b'},
        default=False,
    )
    """When TRUE, enforce auto-negotiation of speed and duplex mode. If "speed"
    and "duplex" properties are both specified, only that single mode will be
    advertised and accepted during the link auto-negotiation process: this works
    only for BASE-T 802.3 specifications and is useful for enforcing gigabits
    modes, as in these cases link negotiation is mandatory. When FALSE, "speed"
    and "duplex" properties should be both set or link configuration will be
    skipped."""
    cloned_mac_address: Optional[bytes] = field(
        metadata={'dbus_name': 'cloned-mac-address', 'dbus_type': 'ay'},
        default=None,
    )
    """This D-Bus field is deprecated in favor of "assigned-mac-address" which is
    more flexible and allows specifying special variants like "random". For libnm
    and nmcli, this field is called "cloned-mac-address"."""
    duplex: Optional[str] = field(
        metadata={'dbus_name': 'duplex', 'dbus_type': 's'},
        default=None,
    )
    """When a value is set, either "half" or "full", configures the device to use
    the specified duplex mode. If "auto-negotiate" is "yes" the specified duplex
    mode will be the only one advertised during link negotiation: this works only
    for BASE-T 802.3 specifications and is useful for enforcing gigabits modes, as
    in these cases link negotiation is mandatory. If the value is unset (the
    default), the link configuration will be either skipped (if "auto-negotiate"
    is "no", the default) or will be auto-negotiated (if "auto-negotiate" is
    "yes") and the local device will advertise all the supported duplex modes.
    Must be set together with the "speed" property if specified. Before specifying
    a duplex mode be sure your device supports it."""
    generate_mac_address_mask: Optional[str] = field(
        metadata={'dbus_name': 'generate-mac-address-mask', 'dbus_type': 's'},
        default=None,
    )
    """With "cloned-mac-address" setting "random" or "stable", by default all bits
    of the MAC address are scrambled and a locally-administered, unicast MAC
    address is created. This property allows to specify that certain bits are
    fixed. Note that the least significant bit of the first MAC address will
    always be unset to create a unicast MAC address. If the property is NULL, it
    is eligible to be overwritten by a default connection setting. If the value is
    still NULL or an empty string, the default is to create a locally-
    administered, unicast MAC address. If the value contains one MAC address, this
    address is used as mask. The set bits of the mask are to be filled with the
    current MAC address of the device, while the unset bits are subject to
    randomization. Setting "FE:FF:FF:00:00:00" means to preserve the OUI of the
    current MAC address and only randomize the lower 3 bytes using the "random" or
    "stable" algorithm. If the value contains one additional MAC address after the
    mask, this address is used instead of the current MAC address to fill the bits
    that shall not be randomized. For example, a value of "FE:FF:FF:00:00:00
    68:F7:28:00:00:00" will set the OUI of the MAC address to 68:F7:28, while the
    lower bits are randomized. A value of "02:00:00:00:00:00 00:00:00:00:00:00"
    will create a fully scrambled globally-administered, burned-in MAC address. If
    the value contains more than one additional MAC addresses, one of them is
    chosen randomly. For example, "02:00:00:00:00:00 00:00:00:00:00:00
    02:00:00:00:00:00" will create a fully scrambled MAC address, randomly locally
    or globally administered."""
    mac_address: Optional[bytes] = field(
        metadata={'dbus_name': 'mac-address', 'dbus_type': 'ay'},
        default=None,
    )
    """If specified, this connection will only apply to the Ethernet device whose
    permanent MAC address matches. This property does not change the MAC address
    of the device (i.e. MAC spoofing)."""
    mac_address_blacklist: Optional[List[str]] = field(
        metadata={'dbus_name': 'mac-address-blacklist', 'dbus_type': 'as'},
        default=None,
    )
    """If specified, this connection will never apply to the Ethernet device whose
    permanent MAC address matches an address in the list.  Each MAC address is in
    the standard hex-digits-and-colons notation (00:11:22:33:44:55)."""
    mtu: Optional[int] = field(
        metadata={'dbus_name': 'mtu', 'dbus_type': 'u'},
        default=None,
    )
    """If non-zero, only transmit packets of the specified size or smaller,
    breaking larger packets up into multiple Ethernet frames."""
    port: Optional[str] = field(
        metadata={'dbus_name': 'port', 'dbus_type': 's'},
        default=None,
    )
    """Specific port type to use if the device supports multiple attachment
    methods.  One of "tp" (Twisted Pair), "aui" (Attachment Unit Interface), "bnc"
    (Thin Ethernet) or "mii" (Media Independent Interface). If the device supports
    only one port type, this setting is ignored."""
    s390_nettype: Optional[str] = field(
        metadata={'dbus_name': 's390-nettype', 'dbus_type': 's'},
        default=None,
    )
    """s390 network device type; one of "qeth", "lcs", or "ctc", representing the
    different types of virtual network devices available on s390 systems."""
    s390_options: Optional[Dict[str, str]] = field(
        metadata={'dbus_name': 's390-options', 'dbus_type': 'a{ss}'},
        default=None,
    )
    """Dictionary of key/value pairs of s390-specific device options.  Both keys
    and values must be strings.  Allowed keys include "portno", "layer2",
    "portname", "protocol", among others.  Key names must contain only
    alphanumeric characters (ie, [a-zA-Z0-9]). Currently, NetworkManager itself
    does nothing with this information. However, s390utils ships a udev rule which
    parses this information and applies it to the interface."""
    s390_subchannels: Optional[List[str]] = field(
        metadata={'dbus_name': 's390-subchannels', 'dbus_type': 'as'},
        default=None,
    )
    """Identifies specific subchannels that this network device uses for
    communication with z/VM or s390 host.  Like the "mac-address" property for
    non-z/VM devices, this property can be used to ensure this connection only
    applies to the network device that uses these subchannels.  The list should
    contain exactly 3 strings, and each string may only be composed of hexadecimal
    characters and the period (.) character."""
    speed: Optional[int] = field(
        metadata={'dbus_name': 'speed', 'dbus_type': 'u'},
        default=None,
    )
    """When a value greater than 0 is set, configures the device to use the
    specified speed. If "auto-negotiate" is "yes" the specified speed will be the
    only one advertised during link negotiation: this works only for BASE-T 802.3
    specifications and is useful for enforcing gigabit speeds, as in this case
    link negotiation is mandatory. If the value is unset (0, the default), the
    link configuration will be either skipped (if "auto-negotiate" is "no", the
    default) or will be auto-negotiated (if "auto-negotiate" is "yes") and the
    local device will advertise all the supported speeds. In Mbit/s, ie 100 ==
    100Mbit/s. Must be set together with the "duplex" property when non-zero.
    Before specifying a speed value be sure your device supports it."""
    wake_on_lan: Optional[int] = field(
        metadata={'dbus_name': 'wake-on-lan', 'dbus_type': 'u'},
        default=1,
    )
    """The NMSettingWiredWakeOnLan options to enable. Not all devices support all
    options. May be any combination of NM_SETTING_WIRED_WAKE_ON_LAN_PHY (0x2),
    NM_SETTING_WIRED_WAKE_ON_LAN_UNICAST (0x4),
    NM_SETTING_WIRED_WAKE_ON_LAN_MULTICAST (0x8),
    NM_SETTING_WIRED_WAKE_ON_LAN_BROADCAST (0x10),
    NM_SETTING_WIRED_WAKE_ON_LAN_ARP (0x20), NM_SETTING_WIRED_WAKE_ON_LAN_MAGIC
    (0x40) or the special values NM_SETTING_WIRED_WAKE_ON_LAN_DEFAULT (0x1) (to
    use global settings) and NM_SETTING_WIRED_WAKE_ON_LAN_IGNORE (0x8000) (to
    disable management of Wake-on-LAN in NetworkManager)."""
    wake_on_lan_password: Optional[str] = field(
        metadata={'dbus_name': 'wake-on-lan-password', 'dbus_type': 's'},
        default=None,
    )
    """If specified, the password used with magic-packet-based Wake-on-LAN,
    represented as an Ethernet MAC address.  If NULL, no password will be
    required."""
