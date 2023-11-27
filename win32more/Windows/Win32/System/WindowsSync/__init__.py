from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WindowsSync
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
SYNC_VERSION_FLAG_FROM_FEED: UInt32 = 1
SYNC_VERSION_FLAG_HAS_BY: UInt32 = 2
SYNC_SERIALIZE_REPLICA_KEY_MAP: UInt32 = 1
SYNC_FILTER_INFO_FLAG_ITEM_LIST: UInt32 = 1
SYNC_FILTER_INFO_FLAG_CHANGE_UNIT_LIST: UInt32 = 2
SYNC_FILTER_INFO_FLAG_CUSTOM: UInt32 = 4
SYNC_FILTER_INFO_COMBINED: UInt32 = 8
SYNC_CHANGE_FLAG_DELETED: UInt32 = 1
SYNC_CHANGE_FLAG_DOES_NOT_EXIST: UInt32 = 2
SYNC_CHANGE_FLAG_GHOST: UInt32 = 4
SCC_DEFAULT: UInt32 = 0
SCC_CAN_CREATE_WITHOUT_UI: UInt32 = 1
SCC_CAN_MODIFY_WITHOUT_UI: UInt32 = 2
SCC_CREATE_NOT_SUPPORTED: UInt32 = 4
SCC_MODIFY_NOT_SUPPORTED: UInt32 = 8
SPC_DEFAULT: UInt32 = 0
SYNC_PROVIDER_STATE_ENABLED: UInt32 = 1
SYNC_PROVIDER_STATE_DIRTY: UInt32 = 2
SYNC_PROVIDER_CONFIGURATION_VERSION: UInt32 = 1
SYNC_PROVIDER_CONFIGUI_CONFIGURATION_VERSION: UInt32 = 1
SYNC_32_BIT_SUPPORTED: UInt32 = 1
SYNC_64_BIT_SUPPORTED: UInt32 = 2
def PKEY_PROVIDER_INSTANCEID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=2)
def PKEY_PROVIDER_CLSID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=3)
def PKEY_PROVIDER_CONFIGUI():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=4)
def PKEY_PROVIDER_CONTENTTYPE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=5)
def PKEY_PROVIDER_CAPABILITIES():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=6)
def PKEY_PROVIDER_SUPPORTED_ARCHITECTURE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=7)
def PKEY_PROVIDER_NAME():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=8)
def PKEY_PROVIDER_DESCRIPTION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=9)
def PKEY_PROVIDER_TOOLTIPS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=10)
def PKEY_PROVIDER_ICON():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=11)
def PKEY_CONFIGUI_INSTANCEID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=2)
def PKEY_CONFIGUI_CLSID():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=3)
def PKEY_CONFIGUI_CONTENTTYPE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=4)
def PKEY_CONFIGUI_CAPABILITIES():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=5)
def PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=6)
def PKEY_CONFIGUI_IS_GLOBAL():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=7)
def PKEY_CONFIGUI_NAME():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=8)
def PKEY_CONFIGUI_DESCRIPTION():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=9)
def PKEY_CONFIGUI_TOOLTIPS():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=10)
def PKEY_CONFIGUI_ICON():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=11)
def PKEY_CONFIGUI_MENUITEM_NOUI():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=12)
def PKEY_CONFIGUI_MENUITEM():
    return win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=13)
CONFLICT_RESOLUTION_POLICY = Int32
CRP_NONE: win32more.Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY = 0
CRP_DESTINATION_PROVIDER_WINS: win32more.Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY = 1
CRP_SOURCE_PROVIDER_WINS: win32more.Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY = 2
CRP_LAST: win32more.Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY = 3
CONSTRAINT_CONFLICT_REASON = Int32
CCR_OTHER: win32more.Windows.Win32.System.WindowsSync.CONSTRAINT_CONFLICT_REASON = 0
CCR_COLLISION: win32more.Windows.Win32.System.WindowsSync.CONSTRAINT_CONFLICT_REASON = 1
CCR_NOPARENT: win32more.Windows.Win32.System.WindowsSync.CONSTRAINT_CONFLICT_REASON = 2
CCR_IDENTITY: win32more.Windows.Win32.System.WindowsSync.CONSTRAINT_CONFLICT_REASON = 3
FILTERING_TYPE = Int32
FT_CURRENT_ITEMS_ONLY: win32more.Windows.Win32.System.WindowsSync.FILTERING_TYPE = 0
FT_CURRENT_ITEMS_AND_VERSIONS_FOR_MOVED_OUT_ITEMS: win32more.Windows.Win32.System.WindowsSync.FILTERING_TYPE = 1
FILTER_COMBINATION_TYPE = Int32
FCT_INTERSECTION: win32more.Windows.Win32.System.WindowsSync.FILTER_COMBINATION_TYPE = 0
class IAsynchronousDataRetriever(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9fc7e470-61ea-4a88-9be4-df56a27cfef2}')
    @commethod(3)
    def GetIdParameters(self, pIdParameters: POINTER(win32more.Windows.Win32.System.WindowsSync.ID_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterCallback(self, pDataRetrieverCallback: win32more.Windows.Win32.System.WindowsSync.IDataRetrieverCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeCallback(self, pDataRetrieverCallback: win32more.Windows.Win32.System.WindowsSync.IDataRetrieverCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LoadChangeData(self, pLoadChangeContext: win32more.Windows.Win32.System.WindowsSync.ILoadChangeContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IChangeConflict(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{014ebf97-9f20-4f7a-bdd4-25979c77c002}')
    @commethod(3)
    def GetDestinationProviderConflictingChange(self, ppConflictingChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceProviderConflictingChange(self, ppConflictingChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDestinationProviderConflictingData(self, ppConflictingData: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceProviderConflictingData(self, ppConflictingData: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResolveActionForChange(self, pResolveAction: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetResolveActionForChange(self, resolveAction: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetResolveActionForChangeUnit(self, pChangeUnit: win32more.Windows.Win32.System.WindowsSync.ISyncChangeUnit, pResolveAction: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetResolveActionForChangeUnit(self, pChangeUnit: win32more.Windows.Win32.System.WindowsSync.ISyncChangeUnit, resolveAction: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IChangeUnitException(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0cd7ee7c-fec0-4021-99ee-f0e5348f2a5f}')
    @commethod(3)
    def GetItemId(self, pbItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitId(self, pbChangeUnitId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClockVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IChangeUnitListFilterInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{f2837671-0bdf-43fa-b502-232375fb50c2}')
    @commethod(4)
    def Initialize(self, ppbChangeUnitIds: POINTER(POINTER(Byte)), dwChangeUnitCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeUnitIdCount(self, pdwChangeUnitIdCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeUnitId(self, dwChangeUnitIdIndex: UInt32, pbChangeUnitId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IClockVector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{14b2274a-8698-4cc6-9333-f89bd1d47bc4}')
    @commethod(3)
    def GetClockVectorElements(self, riid: POINTER(Guid), ppiEnumClockVector: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClockVectorElementCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IClockVectorElement(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e71c4250-adf8-4a07-8fae-5669596909c1}')
    @commethod(3)
    def GetReplicaKey(self, pdwReplicaKey: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTickCount(self, pullTickCount: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICombinedFilterInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{11f9de71-2818-4779-b2ac-42d450565f45}')
    @commethod(4)
    def GetFilterCount(self, pdwFilterCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilterInfo(self, dwFilterIndex: UInt32, ppIFilterInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncFilterInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilterCombinationType(self, pFilterCombinationType: POINTER(win32more.Windows.Win32.System.WindowsSync.FILTER_COMBINATION_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConstraintConflict(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00d2302e-1cf8-4835-b85f-b7ca4f799e0a}')
    @commethod(3)
    def GetDestinationProviderConflictingChange(self, ppConflictingChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceProviderConflictingChange(self, ppConflictingChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDestinationProviderOriginalChange(self, ppOriginalChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDestinationProviderConflictingData(self, ppConflictingData: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSourceProviderConflictingData(self, ppConflictingData: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDestinationProviderOriginalData(self, ppOriginalData: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetConstraintResolveActionForChange(self, pConstraintResolveAction: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetConstraintResolveActionForChange(self, constraintResolveAction: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetConstraintResolveActionForChangeUnit(self, pChangeUnit: win32more.Windows.Win32.System.WindowsSync.ISyncChangeUnit, pConstraintResolveAction: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetConstraintResolveActionForChangeUnit(self, pChangeUnit: win32more.Windows.Win32.System.WindowsSync.ISyncChangeUnit, constraintResolveAction: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConstraintConflictReason(self, pConstraintConflictReason: POINTER(win32more.Windows.Win32.System.WindowsSync.CONSTRAINT_CONFLICT_REASON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsTemporary(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConstructReplicaKeyMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ded10970-ec85-4115-b52c-4405845642a5}')
    @commethod(3)
    def FindOrAddReplica(self, pbReplicaId: POINTER(Byte), pdwReplicaKey: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoreFragment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{613b2ab5-b304-47d9-9c31-ce6c54401a15}')
    @commethod(3)
    def NextColumn(self, pChangeUnitId: POINTER(Byte), pChangeUnitIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NextRange(self, pItemId: POINTER(Byte), pItemIdSize: POINTER(UInt32), piClockVector: POINTER(win32more.Windows.Win32.System.WindowsSync.IClockVector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnCount(self, pColumnCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRangeCount(self, pRangeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoreFragmentInspector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7fcc5fd-ae26-4679-ba16-96aac583c134}')
    @commethod(3)
    def NextCoreFragments(self, requestedCount: UInt32, ppiCoreFragments: POINTER(win32more.Windows.Win32.System.WindowsSync.ICoreFragment), pFetchedCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICustomFilterInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{1d335dff-6f88-4e4d-91a8-a3f351cfd473}')
    @commethod(4)
    def GetSyncFilter(self, pISyncFilter: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ID_PARAMETERS(EasyCastStructure):
    dwSize: UInt32
    replicaId: win32more.Windows.Win32.System.WindowsSync.ID_PARAMETER_PAIR
    itemId: win32more.Windows.Win32.System.WindowsSync.ID_PARAMETER_PAIR
    changeUnitId: win32more.Windows.Win32.System.WindowsSync.ID_PARAMETER_PAIR
class ID_PARAMETER_PAIR(EasyCastStructure):
    fIsVariable: win32more.Windows.Win32.Foundation.BOOL
    cbIdSize: UInt16
class IDataRetrieverCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71b4863b-f969-4676-bbc3-3d9fdc3fb2c7}')
    @commethod(3)
    def LoadChangeDataComplete(self, pUnkData: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadChangeDataError(self, hrError: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumChangeUnitExceptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3074e802-9319-4420-be21-1022e2e21da8}')
    @commethod(3)
    def Next(self, cExceptions: UInt32, ppChangeUnitException: POINTER(win32more.Windows.Win32.System.WindowsSync.IChangeUnitException), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cExceptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumChangeUnitExceptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumClockVector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{525844db-2837-4799-9e80-81a66e02220c}')
    @commethod(3)
    def Next(self, cClockVectorElements: UInt32, ppiClockVectorElements: POINTER(win32more.Windows.Win32.System.WindowsSync.IClockVectorElement), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cSyncVersions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppiEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumClockVector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumFeedClockVector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{550f763d-146a-48f6-abeb-6c88c7f70514}')
    @commethod(3)
    def Next(self, cClockVectorElements: UInt32, ppiClockVectorElements: POINTER(win32more.Windows.Win32.System.WindowsSync.IFeedClockVectorElement), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cSyncVersions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppiEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumFeedClockVector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumItemIds(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{43aa3f61-4b2e-4b60-83df-b110d3e148f1}')
    @commethod(3)
    def Next(self, pbItemId: POINTER(Byte), pcbItemIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumRangeExceptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0944439f-ddb1-4176-b703-046ff22a2386}')
    @commethod(3)
    def Next(self, cExceptions: UInt32, ppRangeException: POINTER(win32more.Windows.Win32.System.WindowsSync.IRangeException), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cExceptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumRangeExceptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSingleItemExceptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e563381c-1b4d-4c66-9796-c86faccdcd40}')
    @commethod(3)
    def Next(self, cExceptions: UInt32, ppSingleItemException: POINTER(win32more.Windows.Win32.System.WindowsSync.ISingleItemException), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cExceptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSingleItemExceptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncChangeUnits(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{346b35f1-8703-4c6d-ab1a-4dbca2cff97f}')
    @commethod(3)
    def Next(self, cChanges: UInt32, ppChangeUnit: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeUnit), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cChanges: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncChangeUnits)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncChanges(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5f86be4a-5e78-4e32-ac1c-c24fd223ef85}')
    @commethod(3)
    def Next(self, cChanges: UInt32, ppChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cChanges: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncChanges)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncProviderConfigUIInfos(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f6be2602-17c6-4658-a2d7-68ed3330f641}')
    @commethod(3)
    def Next(self, cFactories: UInt32, ppSyncProviderConfigUIInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cFactories: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncProviderConfigUIInfos)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncProviderInfos(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a04ba850-5eb1-460d-a973-393fcb608a11}')
    @commethod(3)
    def Next(self, cInstances: UInt32, ppSyncProviderInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderInfo), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cInstances: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncProviderInfos)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFeedClockVector(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.IClockVector
    _iid_ = Guid('{8d1d98d1-9fb8-4ec9-a553-54dd924e0f67}')
    @commethod(5)
    def GetUpdateCount(self, pdwUpdateCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsNoConflictsSpecified(self, pfIsNoConflictsSpecified: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFeedClockVectorElement(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.IClockVectorElement
    _iid_ = Guid('{a40b46d2-e97b-4156-b6da-991f501b0f05}')
    @commethod(5)
    def GetSyncTime(self, pSyncTime: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_TIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFlags(self, pbFlags: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterKeyMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca169652-07c6-4708-a3da-6e4eba8d2297}')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddFilter(self, pISyncFilter: win32more.Windows.Win32.System.WindowsSync.ISyncFilter, pdwFilterKey: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilter(self, dwFilterKey: UInt32, ppISyncFilter: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Serialize(self, pbFilterKeyMap: POINTER(Byte), pcbFilterKeyMap: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterRequestCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82df8873-6360-463a-a8a1-ede5e1a1594d}')
    @commethod(3)
    def RequestFilter(self, pFilter: win32more.Windows.Win32.System.Com.IUnknown, filteringType: win32more.Windows.Win32.System.WindowsSync.FILTERING_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterTrackingProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{743383c0-fc4e-45ba-ad81-d9d84c7a24f8}')
    @commethod(3)
    def SpecifyTrackedFilters(self, pCallback: win32more.Windows.Win32.System.WindowsSync.IFilterTrackingRequestCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddTrackedFilter(self, pFilter: win32more.Windows.Win32.System.WindowsSync.ISyncFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterTrackingRequestCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{713ca7bb-c858-4674-b4b6-1122436587a9}')
    @commethod(3)
    def RequestTrackedFilter(self, pFilter: win32more.Windows.Win32.System.WindowsSync.ISyncFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFilterTrackingSyncChangeBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{295024a0-70da-4c58-883c-ce2afb308d0b}')
    @commethod(3)
    def AddFilterChange(self, dwFilterKey: UInt32, pFilterChange: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_FILTER_CHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAllChangeUnitsPresentFlag(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IForgottenKnowledge(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge
    _iid_ = Guid('{456e0f96-6036-452b-9f9d-bcc4b4a85db2}')
    @commethod(27)
    def ForgetToVersion(self, pKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IKnowledgeSyncProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncProvider
    _iid_ = Guid('{43434a49-8da4-47f2-8172-ad7b8b024978}')
    @commethod(4)
    def BeginSession(self, role: win32more.Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE, pSessionState: win32more.Windows.Win32.System.WindowsSync.ISyncSessionState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSyncBatchParameters(self, ppSyncKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge), pdwRequestedBatchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeBatch(self, dwBatchSize: UInt32, pSyncKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppSyncChangeBatch: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatch), ppUnkDataRetriever: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFullEnumerationChangeBatch(self, dwBatchSize: UInt32, pbLowerEnumerationBound: POINTER(Byte), pSyncKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppSyncChangeBatch: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncFullEnumerationChangeBatch), ppUnkDataRetriever: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ProcessChangeBatch(self, resolutionPolicy: win32more.Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY, pSourceChangeBatch: win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatch, pUnkDataRetriever: win32more.Windows.Win32.System.Com.IUnknown, pCallback: win32more.Windows.Win32.System.WindowsSync.ISyncCallback, pSyncSessionStatistics: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_SESSION_STATISTICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ProcessFullEnumerationChangeBatch(self, resolutionPolicy: win32more.Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY, pSourceChangeBatch: win32more.Windows.Win32.System.WindowsSync.ISyncFullEnumerationChangeBatch, pUnkDataRetriever: win32more.Windows.Win32.System.Com.IUnknown, pCallback: win32more.Windows.Win32.System.WindowsSync.ISyncCallback, pSyncSessionStatistics: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_SESSION_STATISTICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndSession(self, pSessionState: win32more.Windows.Win32.System.WindowsSync.ISyncSessionState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILoadChangeContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44a4aaca-ec39-46d5-b5c9-d633c0ee67e2}')
    @commethod(3)
    def GetSyncChange(self, ppSyncChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRecoverableErrorOnChange(self, hrError: win32more.Windows.Win32.Foundation.HRESULT, pErrorData: win32more.Windows.Win32.System.WindowsSync.IRecoverableErrorData) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRecoverableErrorOnChangeUnit(self, hrError: win32more.Windows.Win32.Foundation.HRESULT, pChangeUnit: win32more.Windows.Win32.System.WindowsSync.ISyncChangeUnit, pErrorData: win32more.Windows.Win32.System.WindowsSync.IRecoverableErrorData) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProviderConverter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{809b7276-98cf-4957-93a5-0ebdd3dddffd}')
    @commethod(3)
    def Initialize(self, pISyncProvider: win32more.Windows.Win32.System.WindowsSync.ISyncProvider) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRangeException(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75ae8777-6848-49f7-956c-a3a92f5096e8}')
    @commethod(3)
    def GetClosedRangeStart(self, pbClosedRangeStart: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClosedRangeEnd(self, pbClosedRangeEnd: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClockVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRecoverableError(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f5625e8-0a7b-45ee-9637-1ce13645909e}')
    @commethod(3)
    def GetStage(self, pStage: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProvider(self, pProviderRole: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeWithRecoverableError(self, ppChangeWithRecoverableError: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecoverableErrorDataForChange(self, phrError: POINTER(win32more.Windows.Win32.Foundation.HRESULT), ppErrorData: POINTER(win32more.Windows.Win32.System.WindowsSync.IRecoverableErrorData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecoverableErrorDataForChangeUnit(self, pChangeUnit: win32more.Windows.Win32.System.WindowsSync.ISyncChangeUnit, phrError: POINTER(win32more.Windows.Win32.Foundation.HRESULT), ppErrorData: POINTER(win32more.Windows.Win32.System.WindowsSync.IRecoverableErrorData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRecoverableErrorData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b37c4a0a-4b7d-4c2d-9711-3b00d119b1c8}')
    @commethod(3)
    def Initialize(self, pcszItemDisplayName: win32more.Windows.Win32.Foundation.PWSTR, pcszErrorDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemDisplayName(self, pszItemDisplayName: win32more.Windows.Win32.Foundation.PWSTR, pcchItemDisplayName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(self, pszErrorDescription: win32more.Windows.Win32.Foundation.PWSTR, pcchErrorDescription: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRegisteredSyncProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{913bcf76-47c1-40b5-a896-5e8a9c414c14}')
    @commethod(3)
    def Init(self, pguidInstanceId: POINTER(Guid), pguidContentType: POINTER(Guid), pContextPropertyStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceId(self, pguidInstanceId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IReplicaKeyMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2209f4fc-fd10-4ff0-84a8-f0a1982e440e}')
    @commethod(3)
    def LookupReplicaKey(self, pbReplicaId: POINTER(Byte), pdwReplicaKey: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LookupReplicaId(self, dwReplicaKey: UInt32, pbReplicaId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Serialize(self, pbReplicaKeyMap: POINTER(Byte), pcbReplicaKeyMap: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRequestFilteredSync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e020184-6d18-46a7-a32a-da4aeb06696c}')
    @commethod(3)
    def SpecifyFilter(self, pCallback: win32more.Windows.Win32.System.WindowsSync.IFilterRequestCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISingleItemException(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{892fb9b0-7c55-4a18-9316-fdf449569b64}')
    @commethod(3)
    def GetItemId(self, pbItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClockVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISupportFilteredSync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d128ded-d555-4e0d-bf4b-fb213a8a9302}')
    @commethod(3)
    def AddFilter(self, pFilter: win32more.Windows.Win32.System.Com.IUnknown, filteringType: win32more.Windows.Win32.System.WindowsSync.FILTERING_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISupportLastWriteTime(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eadf816f-d0bd-43ca-8f40-5acdc6c06f7a}')
    @commethod(3)
    def GetItemChangeTime(self, pbItemId: POINTER(Byte), pullTimestamp: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitChangeTime(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), pullTimestamp: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0599797f-5ed9-485c-ae36-0c5d1bf2e7a5}')
    @commethod(3)
    def OnProgress(self, provider: win32more.Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE, syncStage: win32more.Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE, dwCompletedWork: UInt32, dwTotalWork: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnChange(self, pSyncChange: win32more.Windows.Win32.System.WindowsSync.ISyncChange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnConflict(self, pConflict: win32more.Windows.Win32.System.WindowsSync.IChangeConflict) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnFullEnumerationNeeded(self, pFullEnumerationAction: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_FULL_ENUMERATION_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnRecoverableError(self, pRecoverableError: win32more.Windows.Win32.System.WindowsSync.IRecoverableError) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncCallback2(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncCallback
    _iid_ = Guid('{47ce84af-7442-4ead-8630-12015e030ad7}')
    @commethod(8)
    def OnChangeApplied(self, dwChangesApplied: UInt32, dwChangesFailed: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnChangeFailed(self, dwChangesApplied: UInt32, dwChangesFailed: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1952beb-0f6b-4711-b136-01da85b968a6}')
    @commethod(3)
    def GetOwnerReplicaId(self, pbReplicaId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRootItemId(self, pbRootItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeVersion(self, pbCurrentReplicaId: POINTER(Byte), pVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCreationVersion(self, pbCurrentReplicaId: POINTER(Byte), pVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWorkEstimate(self, pdwWork: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetChangeUnits(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncChangeUnits)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMadeWithKnowledge(self, ppMadeWithKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLearnedKnowledge(self, ppLearnedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetWorkEstimate(self, dwWork: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{70c64dee-380f-4c2e-8f70-31c55bd5f9b3}')
    @commethod(17)
    def BeginUnorderedGroup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EndUnorderedGroup(self, pMadeWithKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, fAllChangesForKnowledge: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddLoggedConflict(self, pbOwnerReplicaId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), pCreationVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), dwFlags: UInt32, dwWorkForChange: UInt32, pConflictKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppChangeBuilder: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatch2(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatch
    _iid_ = Guid('{225f4a33-f5ee-4cc7-b039-67a262b4b2ac}')
    @commethod(20)
    def AddMergeTombstoneMetadataToGroup(self, pbOwnerReplicaId: POINTER(Byte), pbWinnerItemId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), pCreationVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), dwWorkForChange: UInt32, ppChangeBuilder: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddMergeTombstoneLoggedConflict(self, pbOwnerReplicaId: POINTER(Byte), pbWinnerItemId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), pCreationVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), dwWorkForChange: UInt32, pConflictKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppChangeBuilder: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchAdvanced(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f1a4995-cbc8-421d-b550-5d0bebf3e9a5}')
    @commethod(3)
    def GetFilterInfo(self, ppFilterInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncFilterInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertFullEnumerationChangeBatchToRegularChangeBatch(self, ppChangeBatch: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUpperBoundItemId(self, pbItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBatchLevelKnowledgeShouldBeApplied(self, pfBatchKnowledgeShouldBeApplied: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchBase(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52f6e694-6a71-4494-a184-a8311bf5d227}')
    @commethod(3)
    def GetChangeEnumerator(self, ppEnum: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncChanges)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIsLastBatch(self, pfLastBatch: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetWorkEstimateForBatch(self, pdwWorkForBatch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRemainingWorkEstimateForSession(self, pdwRemainingWorkForSession: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginOrderedGroup(self, pbLowerBound: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EndOrderedGroup(self, pbUpperBound: POINTER(Byte), pMadeWithKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddItemMetadataToGroup(self, pbOwnerReplicaId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), pCreationVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), dwFlags: UInt32, dwWorkForChange: UInt32, ppChangeBuilder: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetLearnedKnowledge(self, ppLearnedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPrerequisiteKnowledge(self, ppPrerequisteKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSourceForgottenKnowledge(self, ppSourceForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.IForgottenKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetLastBatch(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetWorkEstimateForBatch(self, dwWorkForBatch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetRemainingWorkEstimateForSession(self, dwRemainingWorkForSession: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Serialize(self, pbChangeBatch: POINTER(Byte), pcbChangeBatch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchBase2(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{6fdb596a-d755-4584-bd0c-c0c23a548fbf}')
    @commethod(17)
    def SerializeWithOptions(self, targetFormatVersion: win32more.Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION, dwFlags: UInt32, pbBuffer: POINTER(Byte), pdwSerializedSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchWithFilterKeyMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de247002-566d-459a-a6ed-a5aab3459fb7}')
    @commethod(3)
    def GetFilterKeyMap(self, ppIFilterKeyMap: POINTER(win32more.Windows.Win32.System.WindowsSync.IFilterKeyMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFilterKeyMap(self, pIFilterKeyMap: win32more.Windows.Win32.System.WindowsSync.IFilterKeyMap) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFilterForgottenKnowledge(self, dwFilterKey: UInt32, pFilterForgottenKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilteredReplicaLearnedKnowledge(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, ppLearnedForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLearnedFilterForgottenKnowledge(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFilteredReplicaLearnedForgottenKnowledge(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, ppLearnedForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, ppLearnedForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchWithPrerequisite(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{097f13be-5b92-4048-b3f2-7b42a2515e07}')
    @commethod(17)
    def SetPrerequisiteKnowledge(self, pPrerequisiteKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetLearnedKnowledgeWithPrerequisite(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppLearnedWithPrerequisiteKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetLearnedForgottenKnowledge(self, ppLearnedForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.IForgottenKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56f14771-8677-484f-a170-e386e418a676}')
    @commethod(3)
    def AddChangeUnitMetadata(self, pbChangeUnitId: POINTER(Byte), pChangeUnitVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeUnit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{60edd8ca-7341-4bb7-95ce-fab6394b51cb}')
    @commethod(3)
    def GetItemChange(self, ppSyncChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitId(self, pbChangeUnitId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeUnitVersion(self, pbCurrentReplicaId: POINTER(Byte), pVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeWithFilterKeyMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bfe1ef00-e87d-42fd-a4e9-242d70414aef}')
    @commethod(3)
    def GetFilterCount(self, pdwFilterCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFilterChange(self, dwFilterKey: UInt32, pFilterChange: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_FILTER_CHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAllChangeUnitsPresentFlag(self, pfAllChangeUnitsPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilterForgottenKnowledge(self, dwFilterKey: UInt32, ppIFilterForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFilteredReplicaLearnedKnowledge(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, ppLearnedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLearnedFilterForgottenKnowledge(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilteredReplicaLearnedForgottenKnowledge(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, ppLearnedForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, ppLearnedForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pNewMoveins: win32more.Windows.Win32.System.WindowsSync.IEnumItemIds, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeWithPrerequisite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9e38382f-1589-48c3-92e4-05ecdcb4f3f7}')
    @commethod(3)
    def GetPrerequisiteKnowledge(self, ppPrerequisiteKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLearnedKnowledgeWithPrerequisite(self, pDestinationKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppLearnedKnowledgeWithPrerequisite: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncConstraintCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8af3843e-75b3-438c-bb51-6f020d70d3cb}')
    @commethod(3)
    def OnConstraintConflict(self, pConflict: win32more.Windows.Win32.System.WindowsSync.IConstraintConflict) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncDataConverter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{435d4861-68d5-44aa-a0f9-72a0b00ef9cf}')
    @commethod(3)
    def ConvertDataRetrieverFromProviderFormat(self, pUnkDataRetrieverIn: win32more.Windows.Win32.System.Com.IUnknown, pEnumSyncChanges: win32more.Windows.Win32.System.WindowsSync.IEnumSyncChanges, ppUnkDataOut: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertDataRetrieverToProviderFormat(self, pUnkDataRetrieverIn: win32more.Windows.Win32.System.Com.IUnknown, pEnumSyncChanges: win32more.Windows.Win32.System.WindowsSync.IEnumSyncChanges, ppUnkDataOut: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertDataFromProviderFormat(self, pDataContext: win32more.Windows.Win32.System.WindowsSync.ILoadChangeContext, pUnkDataIn: win32more.Windows.Win32.System.Com.IUnknown, ppUnkDataOut: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertDataToProviderFormat(self, pDataContext: win32more.Windows.Win32.System.WindowsSync.ILoadChangeContext, pUnkDataOut: win32more.Windows.Win32.System.Com.IUnknown, ppUnkDataout: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{087a3f15-0fcb-44c1-9639-53c14e2b5506}')
    @commethod(3)
    def IsIdentical(self, pSyncFilter: win32more.Windows.Win32.System.WindowsSync.ISyncFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Serialize(self, pbSyncFilter: POINTER(Byte), pcbSyncFilter: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncFilterDeserializer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b45b7a72-e5c7-46be-9c82-77b8b15dab8a}')
    @commethod(3)
    def DeserializeSyncFilter(self, pbSyncFilter: POINTER(Byte), dwCbSyncFilter: UInt32, ppISyncFilter: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncFilterInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{794eaaf8-3f2e-47e6-9728-17e6fcf94cb7}')
    @commethod(3)
    def Serialize(self, pbBuffer: POINTER(Byte), pcbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncFilterInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{19b394ba-e3d0-468c-934d-321968b2ab34}')
    @commethod(4)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncFullEnumerationChange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9785e0bd-bdff-40c4-98c5-b34b2f1991b3}')
    @commethod(3)
    def GetLearnedKnowledgeAfterRecoveryComplete(self, ppLearnedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLearnedForgottenKnowledge(self, ppLearnedForgottenKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.IForgottenKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncFullEnumerationChangeBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{ef64197d-4f44-4ea2-b355-4524713e3bed}')
    @commethod(17)
    def GetLearnedKnowledgeAfterRecoveryComplete(self, ppLearnedKnowledgeAfterRecoveryComplete: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetClosedLowerBoundItemId(self, pbClosedLowerBoundItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetClosedUpperBoundItemId(self, pbClosedUpperBoundItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncFullEnumerationChangeBatch2(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncFullEnumerationChangeBatch
    _iid_ = Guid('{e06449f4-a205-4b65-9724-01b22101eec1}')
    @commethod(20)
    def AddMergeTombstoneMetadataToGroup(self, pbOwnerReplicaId: POINTER(Byte), pbWinnerItemId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), pCreationVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), dwWorkForChange: UInt32, ppChangeBuilder: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncChangeBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncKnowledge(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{615bbb53-c945-4203-bf4b-2cb65919a0aa}')
    @commethod(3)
    def GetOwnerReplicaId(self, pbReplicaId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Serialize(self, fSerializeReplicaKeyMap: win32more.Windows.Win32.Foundation.BOOL, pbKnowledge: POINTER(Byte), pcbKnowledge: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLocalTickCount(self, ullTickCount: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ContainsChange(self, pbVersionOwnerReplicaId: POINTER(Byte), pgidItemId: POINTER(Byte), pSyncVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ContainsChangeUnit(self, pbVersionOwnerReplicaId: POINTER(Byte), pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), pSyncVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetScopeVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetReplicaKeyMap(self, ppReplicaKeyMap: POINTER(win32more.Windows.Win32.System.WindowsSync.IReplicaKeyMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Clone(self, ppClonedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ConvertVersion(self, pKnowledgeIn: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pbCurrentOwnerId: POINTER(Byte), pVersionIn: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION), pbNewOwnerId: POINTER(Byte), pcbIdSize: POINTER(UInt32), pVersionOut: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MapRemoteToLocal(self, pRemoteKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppMappedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Union(self, pKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ProjectOntoItem(self, pbItemId: POINTER(Byte), ppKnowledgeOut: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ProjectOntoChangeUnit(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), ppKnowledgeOut: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ProjectOntoRange(self, psrngSyncRange: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_RANGE), ppKnowledgeOut: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ExcludeItem(self, pbItemId: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ExcludeChangeUnit(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ContainsKnowledge(self, pKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FindMinTickCountForReplica(self, pbReplicaId: POINTER(Byte), pullReplicaTickCount: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRangeExceptions(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetSingleItemExceptions(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetChangeUnitExceptions(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def FindClockVectorForItem(self, pbItemId: POINTER(Byte), riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def FindClockVectorForChangeUnit(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetVersion(self, pdwVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncKnowledge2(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge
    _iid_ = Guid('{ed0addc0-3b4b-46a1-9a45-45661d2114c8}')
    @commethod(27)
    def GetIdParameters(self, pIdParameters: POINTER(win32more.Windows.Win32.System.WindowsSync.ID_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def ProjectOntoColumnSet(self, ppColumns: POINTER(POINTER(Byte)), count: UInt32, ppiKnowledgeOut: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SerializeWithOptions(self, targetFormatVersion: win32more.Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION, dwFlags: UInt32, pbBuffer: POINTER(Byte), pdwSerializedSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetLowestUncontainedId(self, piSyncKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge2, pbItemId: POINTER(Byte), pcbItemIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetInspector(self, riid: POINTER(Guid), ppiInspector: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetMinimumSupportedVersion(self, pVersion: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetStatistics(self, which: win32more.Windows.Win32.System.WindowsSync.SYNC_STATISTICS, pValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def ContainsKnowledgeForItem(self, pKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pbItemId: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ContainsKnowledgeForChangeUnit(self, pKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def ProjectOntoKnowledgeWithPrerequisite(self, pPrerequisiteKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, pTemplateKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppProjectedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Complement(self, pSyncKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge, ppComplementedKnowledge: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def IntersectsWithKnowledge(self, pSyncKnowledge: win32more.Windows.Win32.System.WindowsSync.ISyncKnowledge) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetKnowledgeCookie(self, ppKnowledgeCookie: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def CompareToKnowledgeCookie(self, pKnowledgeCookie: win32more.Windows.Win32.System.Com.IUnknown, pResult: POINTER(win32more.Windows.Win32.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMergeTombstoneChange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ec62597-0903-484c-ad61-36d6e938f47b}')
    @commethod(3)
    def GetWinnerItemId(self, pbWinnerItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8f657056-2bce-4a17-8c68-c7bb7898b56f}')
    @commethod(3)
    def GetIdParameters(self, pIdParameters: POINTER(win32more.Windows.Win32.System.WindowsSync.ID_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderConfigUI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7b0705f6-cbcd-4071-ab05-3bdc364d4a0c}')
    @commethod(3)
    def Init(self, pguidInstanceId: POINTER(Guid), pguidContentType: POINTER(Guid), pConfigurationProperties: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRegisteredProperties(self, ppConfigUIProperties: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateAndRegisterNewSyncProvider(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pUnkContext: win32more.Windows.Win32.System.Com.IUnknown, ppProviderInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ModifySyncProvider(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pUnkContext: win32more.Windows.Win32.System.Com.IUnknown, pProviderInfo: win32more.Windows.Win32.System.WindowsSync.ISyncProviderInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderConfigUIInfo(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    _iid_ = Guid('{214141ae-33d7-4d8d-8e37-f227e880ce50}')
    @commethod(8)
    def GetSyncProviderConfigUI(self, dwClsContext: UInt32, ppSyncProviderConfigUI: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderConfigUI)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    _iid_ = Guid('{1ee135de-88a4-4504-b0d0-f7920d7e5ba6}')
    @commethod(8)
    def GetSyncProvider(self, dwClsContext: UInt32, ppSyncProvider: POINTER(win32more.Windows.Win32.System.WindowsSync.IRegisteredSyncProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb45953b-7624-47bc-a472-eb8cac6b222e}')
    @commethod(3)
    def CreateSyncProviderConfigUIRegistrationInstance(self, pConfigUIConfig: POINTER(win32more.Windows.Win32.System.WindowsSync.SyncProviderConfigUIConfiguration), ppConfigUIInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterSyncProviderConfigUI(self, pguidInstanceId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateSyncProviderConfigUIs(self, pguidContentType: POINTER(Guid), dwSupportedArchitecture: UInt32, ppEnumSyncProviderConfigUIInfos: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncProviderConfigUIInfos)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSyncProviderRegistrationInstance(self, pProviderConfiguration: POINTER(win32more.Windows.Win32.System.WindowsSync.SyncProviderConfiguration), ppProviderInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterSyncProvider(self, pguidInstanceId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSyncProviderConfigUIInfoforProvider(self, pguidProviderInstanceId: POINTER(Guid), ppProviderConfigUIInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateSyncProviders(self, pguidContentType: POINTER(Guid), dwStateFlagsToFilterMask: UInt32, dwStateFlagsToFilter: UInt32, refProviderClsId: POINTER(Guid), dwSupportedArchitecture: UInt32, ppEnumSyncProviderInfos: POINTER(win32more.Windows.Win32.System.WindowsSync.IEnumSyncProviderInfos)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSyncProviderInfo(self, pguidInstanceId: POINTER(Guid), ppProviderInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSyncProviderFromInstanceId(self, pguidInstanceId: POINTER(Guid), dwClsContext: UInt32, ppSyncProvider: POINTER(win32more.Windows.Win32.System.WindowsSync.IRegisteredSyncProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSyncProviderConfigUIInfo(self, pguidInstanceId: POINTER(Guid), ppConfigUIInfo: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSyncProviderConfigUIFromInstanceId(self, pguidInstanceId: POINTER(Guid), dwClsContext: UInt32, ppConfigUI: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProviderConfigUI)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSyncProviderState(self, pguidInstanceId: POINTER(Guid), pdwStateFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetSyncProviderState(self, pguidInstanceId: POINTER(Guid), dwStateFlagsMask: UInt32, dwStateFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForEvent(self, phEvent: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RevokeEvent(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetChange(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE, ppChange: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncRegistrationChange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncRegistrationChange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eea0d9ae-6b29-43b4-9e70-e3ae33bb2c3b}')
    @commethod(3)
    def GetEvent(self, psreEvent: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceId(self, pguidInstanceId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncSessionExtendedErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{326c6810-790a-409b-b741-6999388761eb}')
    @commethod(3)
    def GetSyncProviderWithError(self, ppProviderWithError: POINTER(win32more.Windows.Win32.System.WindowsSync.ISyncProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncSessionState(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b8a940fe-9f01-483b-9434-c37d361225d9}')
    @commethod(3)
    def IsCanceled(self, pfIsCanceled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInfoForChangeApplication(self, pbChangeApplierInfo: POINTER(Byte), pcbChangeApplierInfo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadInfoFromChangeApplication(self, pbChangeApplierInfo: POINTER(Byte), cbChangeApplierInfo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetForgottenKnowledgeRecoveryRangeStart(self, pbRangeStart: POINTER(Byte), pcbRangeStart: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetForgottenKnowledgeRecoveryRangeEnd(self, pbRangeEnd: POINTER(Byte), pcbRangeEnd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetForgottenKnowledgeRecoveryRange(self, pRange: POINTER(win32more.Windows.Win32.System.WindowsSync.SYNC_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnProgress(self, provider: win32more.Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE, syncStage: win32more.Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE, dwCompletedWork: UInt32, dwTotalWork: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncSessionState2(ComPtr):
    extends: win32more.Windows.Win32.System.WindowsSync.ISyncSessionState
    _iid_ = Guid('{9e37cfa3-9e38-4c61-9ca3-ffe810b45ca2}')
    @commethod(10)
    def SetProviderWithError(self, fSelf: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSessionErrorStatus(self, phrSessionError: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISynchronousDataRetriever(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b22f2a9-a4cd-4648-9d8e-3a510d4da04b}')
    @commethod(3)
    def GetIdParameters(self, pIdParameters: POINTER(win32more.Windows.Win32.System.WindowsSync.ID_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadChangeData(self, pLoadChangeContext: win32more.Windows.Win32.System.WindowsSync.ILoadChangeContext, ppUnkData: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
KNOWLEDGE_COOKIE_COMPARISON_RESULT = Int32
KCCR_COOKIE_KNOWLEDGE_EQUAL: win32more.Windows.Win32.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT = 0
KCCR_COOKIE_KNOWLEDGE_CONTAINED: win32more.Windows.Win32.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT = 1
KCCR_COOKIE_KNOWLEDGE_CONTAINS: win32more.Windows.Win32.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT = 2
KCCR_COOKIE_KNOWLEDGE_NOT_COMPARABLE: win32more.Windows.Win32.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT = 3
SYNC_CONSTRAINT_RESOLVE_ACTION = Int32
SCRA_DEFER: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION = 0
SCRA_ACCEPT_DESTINATION_PROVIDER: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION = 1
SCRA_ACCEPT_SOURCE_PROVIDER: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION = 2
SCRA_TRANSFER_AND_DEFER: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION = 3
SCRA_MERGE: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION = 4
SCRA_RENAME_SOURCE: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION = 5
SCRA_RENAME_DESTINATION: win32more.Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION = 6
class SYNC_FILTER_CHANGE(EasyCastStructure):
    fMoveIn: win32more.Windows.Win32.Foundation.BOOL
    moveVersion: win32more.Windows.Win32.System.WindowsSync.SYNC_VERSION
SYNC_FULL_ENUMERATION_ACTION = Int32
SFEA_FULL_ENUMERATION: win32more.Windows.Win32.System.WindowsSync.SYNC_FULL_ENUMERATION_ACTION = 0
SFEA_PARTIAL_SYNC: win32more.Windows.Win32.System.WindowsSync.SYNC_FULL_ENUMERATION_ACTION = 1
SFEA_ABORT: win32more.Windows.Win32.System.WindowsSync.SYNC_FULL_ENUMERATION_ACTION = 2
SYNC_PROGRESS_STAGE = Int32
SPS_CHANGE_DETECTION: win32more.Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE = 0
SPS_CHANGE_ENUMERATION: win32more.Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE = 1
SPS_CHANGE_APPLICATION: win32more.Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE = 2
SYNC_PROVIDER_ROLE = Int32
SPR_SOURCE: win32more.Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE = 0
SPR_DESTINATION: win32more.Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE = 1
class SYNC_RANGE(EasyCastStructure):
    pbClosedLowerBound: POINTER(Byte)
    pbClosedUpperBound: POINTER(Byte)
SYNC_REGISTRATION_EVENT = Int32
SRE_PROVIDER_ADDED: win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT = 0
SRE_PROVIDER_REMOVED: win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT = 1
SRE_PROVIDER_UPDATED: win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT = 2
SRE_PROVIDER_STATE_CHANGED: win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT = 3
SRE_CONFIGUI_ADDED: win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT = 4
SRE_CONFIGUI_REMOVED: win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT = 5
SRE_CONFIGUI_UPDATED: win32more.Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT = 6
SYNC_RESOLVE_ACTION = Int32
SRA_DEFER: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION = 0
SRA_ACCEPT_DESTINATION_PROVIDER: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION = 1
SRA_ACCEPT_SOURCE_PROVIDER: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION = 2
SRA_MERGE: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION = 3
SRA_TRANSFER_AND_DEFER: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION = 4
SRA_LAST: win32more.Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION = 5
SYNC_SERIALIZATION_VERSION = Int32
SYNC_SERIALIZATION_VERSION_V1: win32more.Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION = 1
SYNC_SERIALIZATION_VERSION_V2: win32more.Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION = 4
SYNC_SERIALIZATION_VERSION_V3: win32more.Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION = 5
class SYNC_SESSION_STATISTICS(EasyCastStructure):
    dwChangesApplied: UInt32
    dwChangesFailed: UInt32
SYNC_STATISTICS = Int32
SYNC_STATISTICS_RANGE_COUNT: win32more.Windows.Win32.System.WindowsSync.SYNC_STATISTICS = 0
class SYNC_TIME(EasyCastStructure):
    dwDate: UInt32
    dwTime: UInt32
class SYNC_VERSION(EasyCastStructure):
    dwLastUpdatingReplicaKey: UInt32
    ullTickCount: UInt64
class SyncProviderConfigUIConfiguration(EasyCastStructure):
    dwVersion: UInt32
    guidInstanceId: Guid
    clsidConfigUI: Guid
    guidContentType: Guid
    dwCapabilities: UInt32
    dwSupportedArchitecture: UInt32
    fIsGlobal: win32more.Windows.Win32.Foundation.BOOL
class SyncProviderConfiguration(EasyCastStructure):
    dwVersion: UInt32
    guidInstanceId: Guid
    clsidProvider: Guid
    guidConfigUIInstanceId: Guid
    guidContentType: Guid
    dwCapabilities: UInt32
    dwSupportedArchitecture: UInt32
SyncProviderRegistration = Guid('{f82b4ef1-93a9-4dde-8015-f7950a1a6e31}')


make_ready(__name__)