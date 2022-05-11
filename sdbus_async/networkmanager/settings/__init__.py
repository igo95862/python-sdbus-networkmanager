# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from .connection import ConnectionSettings
from .ipv4 import Ipv4Settings
from .ipv6 import Ipv6Settings
from .ethernet import EthernetSettings
from .wireless import WirelessSettings
from .wireless_security import WirelessSecuritySettings
from .gsm import GsmSettings
from .lowpan import LowpanSettings
from .ieee802_1x import Ieee8021XSettings
from .adsl import AdslSettings
from .bluetooth import BluetoothSettings
from .bond import BondSettings
from .bridge import BridgeSettings
from .bridge_port import BridgePortSettings
from .cdma import CdmaSettings
from .dcb import DcbSettings
from .infiniband import InfinibandSettings
from .ip_tunnel import IpTunnelSettings
from .macsec import MacsecSettings
from .macvlan import MacvlanSettings
from .match import MatchSettings
from .olpc_mesh import OlpcMeshSettings
from .ovs_bridge import OvsBridgeSettings
from .ovs_dpdk import OvsDpdkSettings
from .ovs_interface import OvsInterfaceSettings
from .ovs_patch import OvsPatchSettings
from .ovs_port import OvsPortSettings
from .ppp import PppSettings
from .pppoe import PppoeSettings
from .proxy import ProxySettings
from .serial import SerialSettings
from .team import TeamSettings
from .team_port import TeamPortSettings
from .tun import TunSettings
from .user import UserSettings
from .vlan import VlanSettings
from .vpn import VpnSettings
from .vrf import VrfSettings
from .vxlan import VxlanSettings
from .wifi_p2p import WifiP2PSettings
from .wimax import WimaxSettings
from .wireguard import WireguardSettings
from .wpan import WpanSettings
from .bond_port import BondPortSettings
from .hostname import HostnameSettings
from .ovs_external_ids import OvsExternalIdsSettings
from .veth import VethSettings
__all__ = (
    'ConnectionSettings', 'Ipv4Settings', 'Ipv6Settings', 'EthernetSettings',
    'WirelessSettings', 'WirelessSecuritySettings', 'GsmSettings',
    'LowpanSettings', 'Ieee8021XSettings', 'AdslSettings', 'BluetoothSettings',
    'BondSettings', 'BridgeSettings', 'BridgePortSettings', 'CdmaSettings',
    'DcbSettings', 'InfinibandSettings', 'IpTunnelSettings', 'MacsecSettings',
    'MacvlanSettings', 'MatchSettings', 'OlpcMeshSettings', 'OvsBridgeSettings',
    'OvsDpdkSettings', 'OvsInterfaceSettings', 'OvsPatchSettings',
    'OvsPortSettings', 'PppSettings', 'PppoeSettings', 'ProxySettings',
    'SerialSettings', 'TeamSettings', 'TeamPortSettings', 'TunSettings',
    'UserSettings', 'VlanSettings', 'VpnSettings', 'VrfSettings',
    'VxlanSettings', 'WifiP2PSettings', 'WimaxSettings', 'WireguardSettings',
    'WpanSettings', 'BondPortSettings', 'HostnameSettings',
    'OvsExternalIdsSettings', 'VethSettings'
)