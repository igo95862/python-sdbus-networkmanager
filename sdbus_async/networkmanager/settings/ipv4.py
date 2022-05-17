# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from .base import NetworkManagerSettingsMixin
from .datatypes import AddressData, RouteData


@dataclass
class Ipv4Settings(NetworkManagerSettingsMixin):
    """IPv4 Settings"""

    address_data: Optional[List[AddressData]] = field(
        metadata={'dbus_name': 'address-data',
                  'dbus_type': 'aa{sv}',
                  'dbus_inner_class': AddressData},
        default=None,
    )
    addresses: Optional[List[List[int]]] = field(
        metadata={'dbus_name': 'addresses', 'dbus_type': 'aau'},
        default=None,
    )
    dad_timeout: Optional[int] = field(
        metadata={'dbus_name': 'dad-timeout', 'dbus_type': 'i'},
        default=None,
    )
    dhcp_client_id: Optional[str] = field(
        metadata={'dbus_name': 'dhcp-client-id', 'dbus_type': 's'},
        default=None,
    )
    dhcp_fqdn: Optional[str] = field(
        metadata={'dbus_name': 'dhcp-fqdn', 'dbus_type': 's'},
        default=None,
    )
    dhcp_hostname: Optional[str] = field(
        metadata={'dbus_name': 'dhcp-hostname', 'dbus_type': 's'},
        default=None,
    )
    dhcp_hostname_flags: Optional[int] = field(
        metadata={'dbus_name': 'dhcp-hostname-flags', 'dbus_type': 'u'},
        default=None,
    )
    dhcp_iaid: Optional[str] = field(
        metadata={'dbus_name': 'dhcp-iaid', 'dbus_type': 's'},
        default=None,
    )
    dhcp_reject_servers: Optional[List[str]] = field(
        metadata={'dbus_name': 'dhcp-reject-servers', 'dbus_type': 'as'},
        default=None,
    )
    dhcp_send_hostname: Optional[bool] = field(
        metadata={'dbus_name': 'dhcp-send-hostname', 'dbus_type': 'b'},
        default=True,
    )
    dhcp_timeout: Optional[int] = field(
        metadata={'dbus_name': 'dhcp-timeout', 'dbus_type': 'i'},
        default=None,
    )
    dhcp_vendor_class_identifier: Optional[str] = field(
        metadata={'dbus_name': 'dhcp-vendor-class-identifier',
                  'dbus_type': 's'},
        default=None,
    )
    dns: Optional[List[int]] = field(
        metadata={'dbus_name': 'dns', 'dbus_type': 'au'},
        default=None,
    )
    dns_options: Optional[List[str]] = field(
        metadata={'dbus_name': 'dns-options', 'dbus_type': 'as'},
        default=None,
    )
    dns_priority: Optional[int] = field(
        metadata={'dbus_name': 'dns-priority', 'dbus_type': 'i'},
        default=None,
    )
    dns_search: Optional[List[str]] = field(
        metadata={'dbus_name': 'dns-search', 'dbus_type': 'as'},
        default=None,
    )
    gateway: Optional[str] = field(
        metadata={'dbus_name': 'gateway', 'dbus_type': 's'},
        default=None,
    )
    ignore_auto_dns: Optional[bool] = field(
        metadata={'dbus_name': 'ignore-auto-dns', 'dbus_type': 'b'},
        default=False,
    )
    ignore_auto_routes: Optional[bool] = field(
        metadata={'dbus_name': 'ignore-auto-routes', 'dbus_type': 'b'},
        default=False,
    )
    may_fail: Optional[bool] = field(
        metadata={'dbus_name': 'may-fail', 'dbus_type': 'b'},
        default=True,
    )
    method: Optional[str] = field(
        metadata={'dbus_name': 'method', 'dbus_type': 's'},
        default=None,
    )
    never_default: Optional[bool] = field(
        metadata={'dbus_name': 'never-default', 'dbus_type': 'b'},
        default=False,
    )
    required_timeout: Optional[int] = field(
        metadata={'dbus_name': 'required-timeout', 'dbus_type': 'i'},
        default=None,
    )
    route_data: Optional[List[RouteData]] = field(
        metadata={'dbus_name': 'route-data',
                  'dbus_type': 'aa{sv}',
                  'dbus_inner_class': RouteData},
        default=None,
    )
    route_metric: Optional[int] = field(
        metadata={'dbus_name': 'route-metric', 'dbus_type': 'x'},
        default=None,
    )
    route_table: Optional[int] = field(
        metadata={'dbus_name': 'route-table', 'dbus_type': 'u'},
        default=None,
    )
    routes: Optional[List[List[int]]] = field(
        metadata={'dbus_name': 'routes', 'dbus_type': 'aau'},
        default=None,
    )
