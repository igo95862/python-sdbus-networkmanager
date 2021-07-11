# SPDX-License-Identifier: LGPL-2.1-or-later

# Copyright (C) 2020, 2021 igo95862

# This file is part of python-sdbus

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
from __future__ import annotations

from .enums import (
    AccessPointCapabilities,
    BluetoothCapabilities,
    ConnectionFlags,
    ConnectionState,
    ConnectionStateFlags,
    ConnectionStateReason,
    ConnectivityState,
    DeviceCapabilities,
    DeviceInterfaceFlags,
    DeviceMetered,
    DeviceState,
    DeviceStateReason,
    DeviceType,
    IpTunnelMode,
    ModemCapabilities,
    NetworkManagerConnectivityState,
    NetworkManagerState,
    SecretAgentCapabilities,
    VpnFailure,
    VpnState,
    WiFiOperationMode,
    WirelessCapabilities,
    WpaSecurityFlags,
)
from .interfaces_devices import (
    NetworkManagerDeviceBluetoothInterfaceAsync,
    NetworkManagerDeviceBondInterfaceAsync,
    NetworkManagerDeviceBridgeInterfaceAsync,
    NetworkManagerDeviceGenericInterfaceAsync,
    NetworkManagerDeviceInterfaceAsync,
    NetworkManagerDeviceIPTunnelInterfaceAsync,
    NetworkManagerDeviceLowpanInterfaceAsync,
    NetworkManagerDeviceMacsecInterfaceAsync,
    NetworkManagerDeviceMacvlanInterfaceAsync,
    NetworkManagerDeviceModemInterfaceAsync,
    NetworkManagerDeviceOlpcMeshInterfaceAsync,
    NetworkManagerDeviceOvsBridgeInterfaceAsync,
    NetworkManagerDeviceOvsPortInterfaceAsync,
    NetworkManagerDeviceStatisticsInterfaceAsync,
    NetworkManagerDeviceTeamInterfaceAsync,
    NetworkManagerDeviceTunInterfaceAsync,
    NetworkManagerDeviceVethInterfaceAsync,
    NetworkManagerDeviceVlanInterfaceAsync,
    NetworkManagerDeviceVrfInterfaceAsync,
    NetworkManagerDeviceVxlanInterfaceAsync,
    NetworkManagerDeviceWifiP2PInterfaceAsync,
    NetworkManagerDeviceWiredInterfaceAsync,
    NetworkManagerDeviceWireGuardInterfaceAsync,
    NetworkManagerDeviceWirelessInterfaceAsync,
    NetworkManagerPPPInterfaceAsync,
)
from .interfaces_other import (
    NetworkManagerAccessPointInterfaceAsync,
    NetworkManagerCheckpointInterfaceAsync,
    NetworkManagerConnectionActiveInterfaceAsync,
    NetworkManagerDHCP4ConfigInterfaceAsync,
    NetworkManagerDHCP6ConfigInterfaceAsync,
    NetworkManagerDnsManagerInterfaceAsync,
    NetworkManagerInterfaceAsync,
    NetworkManagerIP4ConfigInterfaceAsync,
    NetworkManagerIP6ConfigInterfaceAsync,
    NetworkManagerSecretAgentInterfaceAsync,
    NetworkManagerSecretAgentManagerInterfaceAsync,
    NetworkManagerSettingsConnectionInterfaceAsync,
    NetworkManagerSettingsInterfaceAsync,
    NetworkManagerVPNConnectionInterfaceAsync,
    NetworkManagerVPNPluginInterfaceAsync,
    NetworkManagerWifiP2PPeerInterfaceAsync,
)
from .objects import (
    AccessPoint,
    ActiveConnection,
    ActiveVPNConnection,
    ConfigCheckpoint,
    DHCPv4Config,
    DHCPv6Config,
    IPv4Config,
    IPv6Config,
    NetworkConnectionSettings,
    NetworkDeviceBluetooth,
    NetworkDeviceBond,
    NetworkDeviceBridge,
    NetworkDeviceGeneric,
    NetworkDeviceIpTunnel,
    NetworkDeviceMacsec,
    NetworkDeviceMacvlan,
    NetworkDeviceModem,
    NetworkDeviceOlpcMesh,
    NetworkDeviceOpenVSwitchBridge,
    NetworkDeviceOpenVSwitchPort,
    NetworkDevicePPP,
    NetworkDeviceTeam,
    NetworkDeviceTun,
    NetworkDeviceVeth,
    NetworkDeviceVlan,
    NetworkDeviceVrf,
    NetworkDeviceVxlan,
    NetworkDeviceWifiP2P,
    NetworkDeviceWired,
    NetworkDeviceWireGuard,
    NetworkDeviceWireless,
    NetworkManager,
    NetworkManagerAgentManager,
    NetworkManagerDnsManager,
    NetworkManagerSettings,
    WiFiP2PPeer,
)


DEVICE_TYPE_TO_CLASS = {
    DeviceType.ETHERNET: NetworkDeviceWired,
    DeviceType.WIFI: NetworkDeviceWireless,
    DeviceType.BLUETOOTH: NetworkDeviceBluetooth,
    DeviceType.OLPC_MESH: NetworkDeviceOlpcMesh,
    DeviceType.VETH: NetworkDeviceVeth,
    DeviceType.WIREGUARD: NetworkDeviceWireGuard,
    DeviceType.PPP: NetworkDevicePPP,
    DeviceType.BRIDGE: NetworkDeviceBridge,
    DeviceType.MODEM: NetworkDeviceModem,
}


__all__ = (
    'AccessPointCapabilities', 'BluetoothCapabilities',
    'ConnectionFlags', 'ConnectionState', 'ConnectionStateFlags',
    'ConnectionStateReason', 'ConnectivityState',
    'DeviceCapabilities', 'DeviceInterfaceFlags', 'DeviceMetered',
    'DeviceState', 'DeviceStateReason', 'DeviceType', 'IpTunnelMode',
    'ModemCapabilities', 'NetworkManagerConnectivityState',
    'NetworkManagerState', 'SecretAgentCapabilities', 'VpnFailure',
    'VpnState', 'WiFiOperationMode', 'WirelessCapabilities',
    'WpaSecurityFlags',

    'NetworkManagerDeviceBluetoothInterfaceAsync',
    'NetworkManagerDeviceBondInterfaceAsync',
    'NetworkManagerDeviceBridgeInterfaceAsync',
    'NetworkManagerDeviceGenericInterfaceAsync',
    'NetworkManagerDeviceInterfaceAsync',
    'NetworkManagerDeviceIPTunnelInterfaceAsync',
    'NetworkManagerDeviceLowpanInterfaceAsync',
    'NetworkManagerDeviceMacsecInterfaceAsync',
    'NetworkManagerDeviceMacvlanInterfaceAsync',
    'NetworkManagerDeviceModemInterfaceAsync',
    'NetworkManagerDeviceOlpcMeshInterfaceAsync',
    'NetworkManagerDeviceOvsBridgeInterfaceAsync',
    'NetworkManagerDeviceOvsPortInterfaceAsync',
    'NetworkManagerDeviceStatisticsInterfaceAsync',
    'NetworkManagerDeviceTeamInterfaceAsync',
    'NetworkManagerDeviceTunInterfaceAsync',
    'NetworkManagerDeviceVethInterfaceAsync',
    'NetworkManagerDeviceVlanInterfaceAsync',
    'NetworkManagerDeviceVrfInterfaceAsync',
    'NetworkManagerDeviceVxlanInterfaceAsync',
    'NetworkManagerDeviceWifiP2PInterfaceAsync',
    'NetworkManagerDeviceWiredInterfaceAsync',
    'NetworkManagerDeviceWireGuardInterfaceAsync',
    'NetworkManagerDeviceWirelessInterfaceAsync',
    'NetworkManagerPPPInterfaceAsync',

    'NetworkManagerAccessPointInterfaceAsync',
    'NetworkManagerCheckpointInterfaceAsync',
    'NetworkManagerConnectionActiveInterfaceAsync',
    'NetworkManagerDHCP4ConfigInterfaceAsync',
    'NetworkManagerDHCP6ConfigInterfaceAsync',
    'NetworkManagerDnsManagerInterfaceAsync',
    'NetworkManagerInterfaceAsync',
    'NetworkManagerIP4ConfigInterfaceAsync',
    'NetworkManagerIP6ConfigInterfaceAsync',
    'NetworkManagerSecretAgentInterfaceAsync',
    'NetworkManagerSecretAgentManagerInterfaceAsync',
    'NetworkManagerSettingsConnectionInterfaceAsync',
    'NetworkManagerSettingsInterfaceAsync',
    'NetworkManagerVPNConnectionInterfaceAsync',
    'NetworkManagerVPNPluginInterfaceAsync',
    'NetworkManagerWifiP2PPeerInterfaceAsync',

    'NetworkManager',
    'NetworkManagerAgentManager',
    'NetworkManagerDnsManager',
    'NetworkManagerSettings',
    'NetworkConnectionSettings',
    'NetworkDeviceGeneric',
    'NetworkDeviceWired',
    'NetworkDeviceWireless',
    'NetworkDeviceBluetooth',
    'NetworkDeviceBond',
    'NetworkDeviceBridge',
    'NetworkDeviceIpTunnel',
    'NetworkDeviceMacsec',
    'NetworkDeviceMacvlan',
    'NetworkDeviceModem',
    'NetworkDeviceOlpcMesh',
    'NetworkDeviceOpenVSwitchBridge',
    'NetworkDeviceOpenVSwitchPort',
    'NetworkDeviceTeam',
    'NetworkDeviceTun',
    'NetworkDeviceVeth',
    'NetworkDeviceVlan',
    'NetworkDeviceVrf',
    'NetworkDeviceVxlan',
    'NetworkDeviceWifiP2P',
    'NetworkDeviceWireGuard',
    'NetworkDevicePPP',
    'ActiveConnection',
    'ActiveVPNConnection',
    'IPv4Config',
    'IPv6Config',
    'DHCPv4Config',
    'DHCPv6Config',
    'AccessPoint',
    'WiFiP2PPeer',
    'ConfigCheckpoint',

    'DEVICE_TYPE_TO_CLASS',
)
