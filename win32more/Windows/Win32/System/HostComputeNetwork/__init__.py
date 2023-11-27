from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.HostComputeNetwork
@winfunctype('computenetwork.dll')
def HcnEnumerateNetworks(Query: win32more.Windows.Win32.Foundation.PWSTR, Networks: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateNetwork(Id: POINTER(Guid), Settings: win32more.Windows.Win32.Foundation.PWSTR, Network: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenNetwork(Id: POINTER(Guid), Network: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyNetwork(Network: VoidPtr, Settings: win32more.Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryNetworkProperties(Network: VoidPtr, Query: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteNetwork(Id: POINTER(Guid), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseNetwork(Network: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateNamespaces(Query: win32more.Windows.Win32.Foundation.PWSTR, Namespaces: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateNamespace(Id: POINTER(Guid), Settings: win32more.Windows.Win32.Foundation.PWSTR, Namespace: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenNamespace(Id: POINTER(Guid), Namespace: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyNamespace(Namespace: VoidPtr, Settings: win32more.Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryNamespaceProperties(Namespace: VoidPtr, Query: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteNamespace(Id: POINTER(Guid), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseNamespace(Namespace: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateEndpoints(Query: win32more.Windows.Win32.Foundation.PWSTR, Endpoints: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateEndpoint(Network: VoidPtr, Id: POINTER(Guid), Settings: win32more.Windows.Win32.Foundation.PWSTR, Endpoint: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenEndpoint(Id: POINTER(Guid), Endpoint: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyEndpoint(Endpoint: VoidPtr, Settings: win32more.Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryEndpointProperties(Endpoint: VoidPtr, Query: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteEndpoint(Id: POINTER(Guid), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseEndpoint(Endpoint: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateLoadBalancers(Query: win32more.Windows.Win32.Foundation.PWSTR, LoadBalancer: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateLoadBalancer(Id: POINTER(Guid), Settings: win32more.Windows.Win32.Foundation.PWSTR, LoadBalancer: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnOpenLoadBalancer(Id: POINTER(Guid), LoadBalancer: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyLoadBalancer(LoadBalancer: VoidPtr, Settings: win32more.Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryLoadBalancerProperties(LoadBalancer: VoidPtr, Query: win32more.Windows.Win32.Foundation.PWSTR, Properties: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteLoadBalancer(Id: POINTER(Guid), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseLoadBalancer(LoadBalancer: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnRegisterServiceCallback(Callback: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK, Context: VoidPtr, CallbackHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnUnregisterServiceCallback(CallbackHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnRegisterGuestNetworkServiceCallback(GuestNetworkService: VoidPtr, Callback: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATION_CALLBACK, Context: VoidPtr, CallbackHandle: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnUnregisterGuestNetworkServiceCallback(CallbackHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCreateGuestNetworkService(Id: POINTER(Guid), Settings: win32more.Windows.Win32.Foundation.PWSTR, GuestNetworkService: POINTER(VoidPtr), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnCloseGuestNetworkService(GuestNetworkService: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnModifyGuestNetworkService(GuestNetworkService: VoidPtr, Settings: win32more.Windows.Win32.Foundation.PWSTR, ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnDeleteGuestNetworkService(Id: POINTER(Guid), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnReserveGuestNetworkServicePort(GuestNetworkService: VoidPtr, Protocol: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_PROTOCOL, Access: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_ACCESS, Port: UInt16, PortReservationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnReserveGuestNetworkServicePortRange(GuestNetworkService: VoidPtr, PortCount: UInt16, PortRangeReservation: POINTER(win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_RANGE_RESERVATION), PortReservationHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnReleaseGuestNetworkServicePortReservationHandle(PortReservationHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnEnumerateGuestNetworkPortReservations(ReturnCount: POINTER(UInt32), PortEntries: POINTER(POINTER(win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnFreeGuestNetworkPortReservations(PortEntries: POINTER(win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_RANGE_ENTRY)) -> Void: ...
@winfunctype('computenetwork.dll')
def HcnQueryEndpointStats(Endpoint: VoidPtr, Query: win32more.Windows.Win32.Foundation.PWSTR, Stats: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computenetwork.dll')
def HcnQueryEndpointAddresses(Endpoint: VoidPtr, Query: win32more.Windows.Win32.Foundation.PWSTR, Addresses: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ErrorRecord: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
HCN_NOTIFICATIONS = Int32
HCN_NOTIFICATIONS_HcnNotificationInvalid: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 0
HCN_NOTIFICATIONS_HcnNotificationNetworkPreCreate: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 1
HCN_NOTIFICATIONS_HcnNotificationNetworkCreate: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 2
HCN_NOTIFICATIONS_HcnNotificationNetworkPreDelete: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 3
HCN_NOTIFICATIONS_HcnNotificationNetworkDelete: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 4
HCN_NOTIFICATIONS_HcnNotificationNamespaceCreate: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 5
HCN_NOTIFICATIONS_HcnNotificationNamespaceDelete: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 6
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceCreate: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 7
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceDelete: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 8
HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointAttached: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 9
HCN_NOTIFICATIONS_HcnNotificationNetworkEndpointDetached: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 16
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceStateChanged: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 17
HCN_NOTIFICATIONS_HcnNotificationGuestNetworkServiceInterfaceStateChanged: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 18
HCN_NOTIFICATIONS_HcnNotificationServiceDisconnect: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = 16777216
HCN_NOTIFICATIONS_HcnNotificationFlagsReserved: win32more.Windows.Win32.System.HostComputeNetwork.HCN_NOTIFICATIONS = -268435456
@winfunctype_pointer
def HCN_NOTIFICATION_CALLBACK(NotificationType: UInt32, Context: VoidPtr, NotificationStatus: win32more.Windows.Win32.Foundation.HRESULT, NotificationData: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
HCN_PORT_ACCESS = Int32
HCN_PORT_ACCESS_EXCLUSIVE: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_ACCESS = 1
HCN_PORT_ACCESS_SHARED: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_ACCESS = 2
HCN_PORT_PROTOCOL = Int32
HCN_PORT_PROTOCOL_TCP: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_PROTOCOL = 1
HCN_PORT_PROTOCOL_UDP: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_PROTOCOL = 2
HCN_PORT_PROTOCOL_BOTH: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_PROTOCOL = 3
class HCN_PORT_RANGE_ENTRY(EasyCastStructure):
    OwningPartitionId: Guid
    TargetPartitionId: Guid
    Protocol: win32more.Windows.Win32.System.HostComputeNetwork.HCN_PORT_PROTOCOL
    Priority: UInt64
    ReservationType: UInt32
    SharingFlags: UInt32
    DeliveryMode: UInt32
    StartingPort: UInt16
    EndingPort: UInt16
class HCN_PORT_RANGE_RESERVATION(EasyCastStructure):
    startingPort: UInt16
    endingPort: UInt16


make_ready(__name__)