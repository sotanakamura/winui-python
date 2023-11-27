from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.Events
import win32more.Windows.Win32.System.Variant
CEventClass = Guid('{cdbec9c0-7a68-11d1-88f9-0080c7d771bf}')
CEventPublisher = Guid('{ab944620-79c6-11d1-88f9-0080c7d771bf}')
CEventSubscription = Guid('{7542e960-79c7-11d1-88f9-0080c7d771bf}')
CEventSystem = Guid('{4e14fba2-2e22-11d1-9964-00c04fbbb345}')
class COMEVENTSYSCHANGEINFO(EasyCastStructure):
    cbSize: UInt32
    changeType: win32more.Windows.Win32.System.Com.Events.EOC_ChangeType
    objectId: win32more.Windows.Win32.Foundation.BSTR
    partitionId: win32more.Windows.Win32.Foundation.BSTR
    applicationId: win32more.Windows.Win32.Foundation.BSTR
    reserved: Guid * 10
EOC_ChangeType = Int32
EOC_NewObject: win32more.Windows.Win32.System.Com.Events.EOC_ChangeType = 0
EOC_ModifiedObject: win32more.Windows.Win32.System.Com.Events.EOC_ChangeType = 1
EOC_DeletedObject: win32more.Windows.Win32.System.Com.Events.EOC_ChangeType = 2
EventObjectChange = Guid('{d0565000-9df4-11d1-a281-00c04fca0aa7}')
EventObjectChange2 = Guid('{bb07bacd-cd56-4e63-a8ff-cbf0355fb9f4}')
class IDontSupportEventSubscription(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{784121f1-62a6-4b89-855f-d65f296de83a}')
class IEnumEventObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4a07d63-2e25-11d1-9964-00c04fbbb345}')
    @commethod(3)
    def Clone(self, ppInterface: POINTER(win32more.Windows.Win32.System.Com.Events.IEnumEventObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, cReqElem: UInt32, ppInterface: POINTER(win32more.Windows.Win32.System.Com.IUnknown), cRetElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, cSkipElem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventClass(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fb2b72a0-7a68-11d1-88f9-0080c7d771bf}')
    @commethod(7)
    def get_EventClassID(self, pbstrEventClassID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_EventClassID(self, bstrEventClassID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventClassName(self, pbstrEventClassName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_EventClassName(self, bstrEventClassName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_OwnerSID(self, pbstrOwnerSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_OwnerSID(self, bstrOwnerSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FiringInterfaceID(self, pbstrFiringInterfaceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_FiringInterfaceID(self, bstrFiringInterfaceID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CustomConfigCLSID(self, pbstrCustomConfigCLSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_CustomConfigCLSID(self, bstrCustomConfigCLSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TypeLib(self, pbstrTypeLib: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_TypeLib(self, bstrTypeLib: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventClass2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Events.IEventClass
    _iid_ = Guid('{fb2b72a1-7a68-11d1-88f9-0080c7d771bf}')
    @commethod(21)
    def get_PublisherID(self, pbstrPublisherID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_PublisherID(self, bstrPublisherID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_MultiInterfacePublisherFilterCLSID(self, pbstrPubFilCLSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MultiInterfacePublisherFilterCLSID(self, bstrPubFilCLSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowInprocActivation(self, pfAllowInprocActivation: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowInprocActivation(self, fAllowInprocActivation: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_FireInParallel(self, pfFireInParallel: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_FireInParallel(self, fFireInParallel: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0343e2f4-86f6-11d1-b760-00c04fb926af}')
    @commethod(7)
    def SetPublisherFilter(self, methodName: win32more.Windows.Win32.Foundation.BSTR, pPublisherFilter: win32more.Windows.Win32.System.Com.Events.IPublisherFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AllowInprocActivation(self, pfAllowInprocActivation: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_AllowInprocActivation(self, fAllowInprocActivation: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSubscriptions(self, methodName: win32more.Windows.Win32.Foundation.BSTR, optionalCriteria: win32more.Windows.Win32.Foundation.BSTR, optionalErrorIndex: POINTER(Int32), ppCollection: POINTER(win32more.Windows.Win32.System.Com.Events.IEventObjectCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultQuery(self, methodName: win32more.Windows.Win32.Foundation.BSTR, criteria: win32more.Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventObjectChange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4a07d70-2e25-11d1-9964-00c04fbbb345}')
    @commethod(3)
    def ChangedSubscription(self, changeType: win32more.Windows.Win32.System.Com.Events.EOC_ChangeType, bstrSubscriptionID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChangedEventClass(self, changeType: win32more.Windows.Win32.System.Com.Events.EOC_ChangeType, bstrEventClassID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChangedPublisher(self, changeType: win32more.Windows.Win32.System.Com.Events.EOC_ChangeType, bstrPublisherID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventObjectChange2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7701a9c3-bd68-438f-83e0-67bf4f53a422}')
    @commethod(3)
    def ChangedSubscription(self, pInfo: POINTER(win32more.Windows.Win32.System.Com.Events.COMEVENTSYSCHANGEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChangedEventClass(self, pInfo: POINTER(win32more.Windows.Win32.System.Com.Events.COMEVENTSYSCHANGEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventObjectCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f89ac270-d4eb-11d1-b682-00805fc79216}')
    @commethod(7)
    def get__NewEnum(self, ppUnkEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, objectID: win32more.Windows.Win32.Foundation.BSTR, pItem: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NewEnum(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.Events.IEnumEventObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Count(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, item: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), objectID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, objectID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{da538ee2-f4de-11d1-b6bb-00805fc79216}')
    @commethod(7)
    def get_Name(self, propertyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, propertyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(self, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Value(self, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventPublisher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e341516b-2e32-11d1-9964-00c04fbbb345}')
    @commethod(7)
    def get_PublisherID(self, pbstrPublisherID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_PublisherID(self, bstrPublisherID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PublisherName(self, pbstrPublisherName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PublisherName(self, bstrPublisherName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PublisherType(self, pbstrPublisherType: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PublisherType(self, bstrPublisherType: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OwnerSID(self, pbstrOwnerSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_OwnerSID(self, bstrOwnerSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDefaultProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def PutDefaultProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RemoveDefaultProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultPropertyCollection(self, collection: POINTER(win32more.Windows.Win32.System.Com.Events.IEventObjectCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventSubscription(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4a6b0e15-2e38-11d1-9965-00c04fbbb345}')
    @commethod(7)
    def get_SubscriptionID(self, pbstrSubscriptionID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SubscriptionID(self, bstrSubscriptionID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SubscriptionName(self, pbstrSubscriptionName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_SubscriptionName(self, bstrSubscriptionName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PublisherID(self, pbstrPublisherID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PublisherID(self, bstrPublisherID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_EventClassID(self, pbstrEventClassID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_EventClassID(self, bstrEventClassID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MethodName(self, pbstrMethodName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MethodName(self, bstrMethodName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SubscriberCLSID(self, pbstrSubscriberCLSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SubscriberCLSID(self, bstrSubscriberCLSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SubscriberInterface(self, ppSubscriberInterface: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SubscriberInterface(self, pSubscriberInterface: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_PerUser(self, pfPerUser: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_PerUser(self, fPerUser: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_OwnerSID(self, pbstrOwnerSID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_OwnerSID(self, bstrOwnerSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Enabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Enabled(self, fEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Description(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Description(self, bstrDescription: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_MachineName(self, pbstrMachineName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MachineName(self, bstrMachineName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetPublisherProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def PutPublisherProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemovePublisherProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetPublisherPropertyCollection(self, collection: POINTER(win32more.Windows.Win32.System.Com.Events.IEventObjectCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetSubscriberProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def PutSubscriberProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def RemoveSubscriberProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetSubscriberPropertyCollection(self, collection: POINTER(win32more.Windows.Win32.System.Com.Events.IEventObjectCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_InterfaceID(self, pbstrInterfaceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_InterfaceID(self, bstrInterfaceID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEventSystem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4e14fb9f-2e22-11d1-9964-00c04fbbb345}')
    @commethod(7)
    def Query(self, progID: win32more.Windows.Win32.Foundation.BSTR, queryCriteria: win32more.Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32), ppInterface: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Store(self, ProgID: win32more.Windows.Win32.Foundation.BSTR, pInterface: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(self, progID: win32more.Windows.Win32.Foundation.BSTR, queryCriteria: win32more.Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EventObjectChangeEventClassID(self, pbstrEventClassID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def QueryS(self, progID: win32more.Windows.Win32.Foundation.BSTR, queryCriteria: win32more.Windows.Win32.Foundation.BSTR, ppInterface: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveS(self, progID: win32more.Windows.Win32.Foundation.BSTR, queryCriteria: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFiringControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e0498c93-4efe-11d1-9971-00c04fbbb345}')
    @commethod(7)
    def FireSubscription(self, subscription: win32more.Windows.Win32.System.Com.Events.IEventSubscription) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultiInterfaceEventControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0343e2f5-86f6-11d1-b760-00c04fb926af}')
    @commethod(3)
    def SetMultiInterfacePublisherFilter(self, classFilter: win32more.Windows.Win32.System.Com.Events.IMultiInterfacePublisherFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSubscriptions(self, eventIID: POINTER(Guid), bstrMethodName: win32more.Windows.Win32.Foundation.BSTR, optionalCriteria: win32more.Windows.Win32.Foundation.BSTR, optionalErrorIndex: POINTER(Int32), ppCollection: POINTER(win32more.Windows.Win32.System.Com.Events.IEventObjectCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultQuery(self, eventIID: POINTER(Guid), bstrMethodName: win32more.Windows.Win32.Foundation.BSTR, bstrCriteria: win32more.Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_AllowInprocActivation(self, pfAllowInprocActivation: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_AllowInprocActivation(self, fAllowInprocActivation: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FireInParallel(self, pfFireInParallel: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_FireInParallel(self, fFireInParallel: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultiInterfacePublisherFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{465e5cc1-7b26-11d1-88fb-0080c7d771bf}')
    @commethod(3)
    def Initialize(self, pEIC: win32more.Windows.Win32.System.Com.Events.IMultiInterfaceEventControl) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareToFire(self, iid: POINTER(Guid), methodName: win32more.Windows.Win32.Foundation.BSTR, firingControl: win32more.Windows.Win32.System.Com.Events.IFiringControl) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPublisherFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{465e5cc0-7b26-11d1-88fb-0080c7d771bf}')
    @commethod(3)
    def Initialize(self, methodName: win32more.Windows.Win32.Foundation.BSTR, dispUserDefined: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareToFire(self, methodName: win32more.Windows.Win32.Foundation.BSTR, firingControl: win32more.Windows.Win32.System.Com.Events.IFiringControl) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
