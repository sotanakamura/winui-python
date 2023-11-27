from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Usb
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
class IUsbBulkInEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkInEndpointDescriptor'
    _iid_ = Guid('{3c6e4846-06cf-42a9-9dc2-971c1b14b6e3}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Pipe(self) -> win32more.Windows.Devices.Usb.UsbBulkInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class IUsbBulkInPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkInPipe'
    _iid_ = Guid('{f01d2d3b-4548-4d50-b326-d82cdabe1220}')
    @winrt_commethod(6)
    def get_MaxTransferSizeBytes(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_commethod(8)
    def ClearStallAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def put_ReadOptions(self, value: win32more.Windows.Devices.Usb.UsbReadOptions) -> Void: ...
    @winrt_commethod(10)
    def get_ReadOptions(self) -> win32more.Windows.Devices.Usb.UsbReadOptions: ...
    @winrt_commethod(11)
    def FlushBuffer(self) -> Void: ...
    @winrt_commethod(12)
    def get_InputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    MaxTransferSizeBytes = property(get_MaxTransferSizeBytes, None)
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    ReadOptions = property(get_ReadOptions, put_ReadOptions)
    InputStream = property(get_InputStream, None)
class IUsbBulkOutEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor'
    _iid_ = Guid('{2820847a-ffee-4f60-9be1-956cac3ecb65}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Pipe(self) -> win32more.Windows.Devices.Usb.UsbBulkOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class IUsbBulkOutPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkOutPipe'
    _iid_ = Guid('{a8e9ee6e-0115-45aa-8b21-37b225bccee7}')
    @winrt_commethod(6)
    def get_EndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_commethod(7)
    def ClearStallAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def put_WriteOptions(self, value: win32more.Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_commethod(9)
    def get_WriteOptions(self) -> win32more.Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_commethod(10)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
class IUsbConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbConfiguration'
    _iid_ = Guid('{68177429-36a9-46d7-b873-fc689251ec30}')
    @winrt_commethod(6)
    def get_UsbInterfaces(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterface]: ...
    @winrt_commethod(7)
    def get_ConfigurationDescriptor(self) -> win32more.Windows.Devices.Usb.UsbConfigurationDescriptor: ...
    @winrt_commethod(8)
    def get_Descriptors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbDescriptor]: ...
    UsbInterfaces = property(get_UsbInterfaces, None)
    ConfigurationDescriptor = property(get_ConfigurationDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class IUsbConfigurationDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbConfigurationDescriptor'
    _iid_ = Guid('{f2176d92-b442-407a-8207-7d646c0385f3}')
    @winrt_commethod(6)
    def get_ConfigurationValue(self) -> Byte: ...
    @winrt_commethod(7)
    def get_MaxPowerMilliamps(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_SelfPowered(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_RemoteWakeup(self) -> Boolean: ...
    ConfigurationValue = property(get_ConfigurationValue, None)
    MaxPowerMilliamps = property(get_MaxPowerMilliamps, None)
    SelfPowered = property(get_SelfPowered, None)
    RemoteWakeup = property(get_RemoteWakeup, None)
class IUsbConfigurationDescriptorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbConfigurationDescriptorStatics'
    _iid_ = Guid('{424ced93-e740-40a1-92bd-da120ea04914}')
    @winrt_commethod(6)
    def TryParse(self, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(win32more.Windows.Devices.Usb.UsbConfigurationDescriptor)) -> Boolean: ...
    @winrt_commethod(7)
    def Parse(self, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor) -> win32more.Windows.Devices.Usb.UsbConfigurationDescriptor: ...
class IUsbControlRequestType(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbControlRequestType'
    _iid_ = Guid('{8e9465a6-d73d-46de-94be-aae7f07c0f5c}')
    @winrt_commethod(6)
    def get_Direction(self) -> win32more.Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_commethod(7)
    def put_Direction(self, value: win32more.Windows.Devices.Usb.UsbTransferDirection) -> Void: ...
    @winrt_commethod(8)
    def get_ControlTransferType(self) -> win32more.Windows.Devices.Usb.UsbControlTransferType: ...
    @winrt_commethod(9)
    def put_ControlTransferType(self, value: win32more.Windows.Devices.Usb.UsbControlTransferType) -> Void: ...
    @winrt_commethod(10)
    def get_Recipient(self) -> win32more.Windows.Devices.Usb.UsbControlRecipient: ...
    @winrt_commethod(11)
    def put_Recipient(self, value: win32more.Windows.Devices.Usb.UsbControlRecipient) -> Void: ...
    @winrt_commethod(12)
    def get_AsByte(self) -> Byte: ...
    @winrt_commethod(13)
    def put_AsByte(self, value: Byte) -> Void: ...
    Direction = property(get_Direction, put_Direction)
    ControlTransferType = property(get_ControlTransferType, put_ControlTransferType)
    Recipient = property(get_Recipient, put_Recipient)
    AsByte = property(get_AsByte, put_AsByte)
class IUsbDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDescriptor'
    _iid_ = Guid('{0a89f216-5f9d-4874-8904-da9ad3f5528f}')
    @winrt_commethod(6)
    def get_Length(self) -> Byte: ...
    @winrt_commethod(7)
    def get_DescriptorType(self) -> Byte: ...
    @winrt_commethod(8)
    def ReadDescriptorBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Length = property(get_Length, None)
    DescriptorType = property(get_DescriptorType, None)
class IUsbDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDevice'
    _iid_ = Guid('{5249b992-c456-44d5-ad5e-24f5a089f63b}')
    @winrt_commethod(6)
    def SendControlOutTransferAsync(self, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(7)
    def SendControlOutTransferAsyncNoBuffer(self, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(8)
    def SendControlInTransferAsync(self, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def SendControlInTransferAsyncNoBuffer(self, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(10)
    def get_DefaultInterface(self) -> win32more.Windows.Devices.Usb.UsbInterface: ...
    @winrt_commethod(11)
    def get_DeviceDescriptor(self) -> win32more.Windows.Devices.Usb.UsbDeviceDescriptor: ...
    @winrt_commethod(12)
    def get_Configuration(self) -> win32more.Windows.Devices.Usb.UsbConfiguration: ...
    DefaultInterface = property(get_DefaultInterface, None)
    DeviceDescriptor = property(get_DeviceDescriptor, None)
    Configuration = property(get_Configuration, None)
class IUsbDeviceClass(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceClass'
    _iid_ = Guid('{051942f9-845e-47eb-b12a-38f2f617afe7}')
    @winrt_commethod(6)
    def get_ClassCode(self) -> Byte: ...
    @winrt_commethod(7)
    def put_ClassCode(self, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def get_SubclassCode(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(9)
    def put_SubclassCode(self, value: win32more.Windows.Foundation.IReference[Byte]) -> Void: ...
    @winrt_commethod(10)
    def get_ProtocolCode(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(11)
    def put_ProtocolCode(self, value: win32more.Windows.Foundation.IReference[Byte]) -> Void: ...
    ClassCode = property(get_ClassCode, put_ClassCode)
    SubclassCode = property(get_SubclassCode, put_SubclassCode)
    ProtocolCode = property(get_ProtocolCode, put_ProtocolCode)
class IUsbDeviceClasses(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceClasses'
    _iid_ = Guid('{686f955d-9b92-4b30-9781-c22c55ac35cb}')
class IUsbDeviceClassesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceClassesStatics'
    _iid_ = Guid('{b20b0527-c580-4599-a165-981b4fd03230}')
    @winrt_commethod(6)
    def get_CdcControl(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(7)
    def get_Physical(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(8)
    def get_PersonalHealthcare(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(9)
    def get_ActiveSync(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(10)
    def get_PalmSync(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(11)
    def get_DeviceFirmwareUpdate(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(12)
    def get_Irda(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(13)
    def get_Measurement(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(14)
    def get_VendorSpecific(self) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    CdcControl = property(get_CdcControl, None)
    Physical = property(get_Physical, None)
    PersonalHealthcare = property(get_PersonalHealthcare, None)
    ActiveSync = property(get_ActiveSync, None)
    PalmSync = property(get_PalmSync, None)
    DeviceFirmwareUpdate = property(get_DeviceFirmwareUpdate, None)
    Irda = property(get_Irda, None)
    Measurement = property(get_Measurement, None)
    VendorSpecific = property(get_VendorSpecific, None)
class IUsbDeviceDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceDescriptor'
    _iid_ = Guid('{1f48d1f6-ba97-4322-b92c-b5b189216588}')
    @winrt_commethod(6)
    def get_BcdUsb(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MaxPacketSize0(self) -> Byte: ...
    @winrt_commethod(8)
    def get_VendorId(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ProductId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_BcdDeviceRevision(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_NumberOfConfigurations(self) -> Byte: ...
    BcdUsb = property(get_BcdUsb, None)
    MaxPacketSize0 = property(get_MaxPacketSize0, None)
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    BcdDeviceRevision = property(get_BcdDeviceRevision, None)
    NumberOfConfigurations = property(get_NumberOfConfigurations, None)
class IUsbDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceStatics'
    _iid_ = Guid('{066b85a2-09b7-4446-8502-6fe6dcaa7309}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, vendorId: UInt32, productId: UInt32, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorGuidOnly(self, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorVidPidOnly(self, vendorId: UInt32, productId: UInt32) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceClassSelector(self, usbClass: win32more.Windows.Devices.Usb.UsbDeviceClass) -> WinRT_String: ...
    @winrt_commethod(10)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Usb.UsbDevice]: ...
class IUsbEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbEndpointDescriptor'
    _iid_ = Guid('{6b4862d9-8df7-4b40-ac83-578f139f0575}')
    @winrt_commethod(6)
    def get_EndpointNumber(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Direction(self) -> win32more.Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_commethod(8)
    def get_EndpointType(self) -> win32more.Windows.Devices.Usb.UsbEndpointType: ...
    @winrt_commethod(9)
    def get_AsBulkInEndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_commethod(10)
    def get_AsInterruptInEndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_commethod(11)
    def get_AsBulkOutEndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_commethod(12)
    def get_AsInterruptOutEndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    EndpointNumber = property(get_EndpointNumber, None)
    Direction = property(get_Direction, None)
    EndpointType = property(get_EndpointType, None)
    AsBulkInEndpointDescriptor = property(get_AsBulkInEndpointDescriptor, None)
    AsInterruptInEndpointDescriptor = property(get_AsInterruptInEndpointDescriptor, None)
    AsBulkOutEndpointDescriptor = property(get_AsBulkOutEndpointDescriptor, None)
    AsInterruptOutEndpointDescriptor = property(get_AsInterruptOutEndpointDescriptor, None)
class IUsbEndpointDescriptorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbEndpointDescriptorStatics'
    _iid_ = Guid('{c890b201-9a6a-495e-a82c-295b9e708106}')
    @winrt_commethod(6)
    def TryParse(self, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(win32more.Windows.Devices.Usb.UsbEndpointDescriptor)) -> Boolean: ...
    @winrt_commethod(7)
    def Parse(self, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor) -> win32more.Windows.Devices.Usb.UsbEndpointDescriptor: ...
class IUsbInterface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterface'
    _iid_ = Guid('{a0322b95-7f47-48ab-a727-678c25be2112}')
    @winrt_commethod(6)
    def get_BulkInPipes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkInPipe]: ...
    @winrt_commethod(7)
    def get_InterruptInPipes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptInPipe]: ...
    @winrt_commethod(8)
    def get_BulkOutPipes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkOutPipe]: ...
    @winrt_commethod(9)
    def get_InterruptOutPipes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptOutPipe]: ...
    @winrt_commethod(10)
    def get_InterfaceSettings(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterfaceSetting]: ...
    @winrt_commethod(11)
    def get_InterfaceNumber(self) -> Byte: ...
    @winrt_commethod(12)
    def get_Descriptors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInPipes = property(get_BulkInPipes, None)
    InterruptInPipes = property(get_InterruptInPipes, None)
    BulkOutPipes = property(get_BulkOutPipes, None)
    InterruptOutPipes = property(get_InterruptOutPipes, None)
    InterfaceSettings = property(get_InterfaceSettings, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
    Descriptors = property(get_Descriptors, None)
class IUsbInterfaceDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterfaceDescriptor'
    _iid_ = Guid('{199670c7-b7ee-4f90-8cd5-94a2e257598a}')
    @winrt_commethod(6)
    def get_ClassCode(self) -> Byte: ...
    @winrt_commethod(7)
    def get_SubclassCode(self) -> Byte: ...
    @winrt_commethod(8)
    def get_ProtocolCode(self) -> Byte: ...
    @winrt_commethod(9)
    def get_AlternateSettingNumber(self) -> Byte: ...
    @winrt_commethod(10)
    def get_InterfaceNumber(self) -> Byte: ...
    ClassCode = property(get_ClassCode, None)
    SubclassCode = property(get_SubclassCode, None)
    ProtocolCode = property(get_ProtocolCode, None)
    AlternateSettingNumber = property(get_AlternateSettingNumber, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
class IUsbInterfaceDescriptorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterfaceDescriptorStatics'
    _iid_ = Guid('{e34a9ff5-77d6-48b6-b0be-16c6422316fe}')
    @winrt_commethod(6)
    def TryParse(self, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(win32more.Windows.Devices.Usb.UsbInterfaceDescriptor)) -> Boolean: ...
    @winrt_commethod(7)
    def Parse(self, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor) -> win32more.Windows.Devices.Usb.UsbInterfaceDescriptor: ...
class IUsbInterfaceSetting(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterfaceSetting'
    _iid_ = Guid('{1827bba7-8da7-4af7-8f4c-7f3032e781f5}')
    @winrt_commethod(6)
    def get_BulkInEndpoints(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkInEndpointDescriptor]: ...
    @winrt_commethod(7)
    def get_InterruptInEndpoints(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptInEndpointDescriptor]: ...
    @winrt_commethod(8)
    def get_BulkOutEndpoints(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkOutEndpointDescriptor]: ...
    @winrt_commethod(9)
    def get_InterruptOutEndpoints(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor]: ...
    @winrt_commethod(10)
    def get_Selected(self) -> Boolean: ...
    @winrt_commethod(11)
    def SelectSettingAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def get_InterfaceDescriptor(self) -> win32more.Windows.Devices.Usb.UsbInterfaceDescriptor: ...
    @winrt_commethod(13)
    def get_Descriptors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInEndpoints = property(get_BulkInEndpoints, None)
    InterruptInEndpoints = property(get_InterruptInEndpoints, None)
    BulkOutEndpoints = property(get_BulkOutEndpoints, None)
    InterruptOutEndpoints = property(get_InterruptOutEndpoints, None)
    Selected = property(get_Selected, None)
    InterfaceDescriptor = property(get_InterfaceDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class IUsbInterruptInEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor'
    _iid_ = Guid('{c0528967-c911-4c3a-86b2-419c2da89039}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Interval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Pipe(self) -> win32more.Windows.Devices.Usb.UsbInterruptInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class IUsbInterruptInEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptInEventArgs'
    _iid_ = Guid('{b7b04092-1418-4936-8209-299cf5605583}')
    @winrt_commethod(6)
    def get_InterruptData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    InterruptData = property(get_InterruptData, None)
class IUsbInterruptInPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptInPipe'
    _iid_ = Guid('{fa007116-84d7-48c7-8a3f-4c0b235f2ea6}')
    @winrt_commethod(6)
    def get_EndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_commethod(7)
    def ClearStallAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def add_DataReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Usb.UsbInterruptInPipe, win32more.Windows.Devices.Usb.UsbInterruptInEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DataReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
class IUsbInterruptOutEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor'
    _iid_ = Guid('{cc9fed81-10ca-4533-952d-9e278341e80f}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Interval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Pipe(self) -> win32more.Windows.Devices.Usb.UsbInterruptOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class IUsbInterruptOutPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptOutPipe'
    _iid_ = Guid('{e984c8a9-aaf9-49d0-b96c-f661ab4a7f95}')
    @winrt_commethod(6)
    def get_EndpointDescriptor(self) -> win32more.Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    @winrt_commethod(7)
    def ClearStallAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def put_WriteOptions(self, value: win32more.Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_commethod(9)
    def get_WriteOptions(self) -> win32more.Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_commethod(10)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
class IUsbSetupPacket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbSetupPacket'
    _iid_ = Guid('{104ba132-c78f-4c51-b654-e49d02f2cb03}')
    @winrt_commethod(6)
    def get_RequestType(self) -> win32more.Windows.Devices.Usb.UsbControlRequestType: ...
    @winrt_commethod(7)
    def put_RequestType(self, value: win32more.Windows.Devices.Usb.UsbControlRequestType) -> Void: ...
    @winrt_commethod(8)
    def get_Request(self) -> Byte: ...
    @winrt_commethod(9)
    def put_Request(self, value: Byte) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_Value(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_Index(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_Index(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_Length(self) -> UInt32: ...
    @winrt_commethod(15)
    def put_Length(self, value: UInt32) -> Void: ...
    RequestType = property(get_RequestType, put_RequestType)
    Request = property(get_Request, put_Request)
    Value = property(get_Value, put_Value)
    Index = property(get_Index, put_Index)
    Length = property(get_Length, put_Length)
class IUsbSetupPacketFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbSetupPacketFactory'
    _iid_ = Guid('{c9257d50-1b2e-4a41-a2a7-338f0cef3c14}')
    @winrt_commethod(6)
    def CreateWithEightByteBuffer(self, eightByteBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Usb.UsbSetupPacket: ...
class UsbBulkInEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbBulkInEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbBulkInEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: win32more.Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: win32more.Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Pipe(self: win32more.Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbBulkInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class UsbBulkInPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbBulkInPipe
    _classid_ = 'Windows.Devices.Usb.UsbBulkInPipe'
    @winrt_mixinmethod
    def get_MaxTransferSizeBytes(self: win32more.Windows.Devices.Usb.IUsbBulkInPipe) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbBulkInPipe) -> win32more.Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: win32more.Windows.Devices.Usb.IUsbBulkInPipe) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def put_ReadOptions(self: win32more.Windows.Devices.Usb.IUsbBulkInPipe, value: win32more.Windows.Devices.Usb.UsbReadOptions) -> Void: ...
    @winrt_mixinmethod
    def get_ReadOptions(self: win32more.Windows.Devices.Usb.IUsbBulkInPipe) -> win32more.Windows.Devices.Usb.UsbReadOptions: ...
    @winrt_mixinmethod
    def FlushBuffer(self: win32more.Windows.Devices.Usb.IUsbBulkInPipe) -> Void: ...
    @winrt_mixinmethod
    def get_InputStream(self: win32more.Windows.Devices.Usb.IUsbBulkInPipe) -> win32more.Windows.Storage.Streams.IInputStream: ...
    MaxTransferSizeBytes = property(get_MaxTransferSizeBytes, None)
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    ReadOptions = property(get_ReadOptions, put_ReadOptions)
    InputStream = property(get_InputStream, None)
class UsbBulkOutEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbBulkOutEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: win32more.Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: win32more.Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Pipe(self: win32more.Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbBulkOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class UsbBulkOutPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbBulkOutPipe
    _classid_ = 'Windows.Devices.Usb.UsbBulkOutPipe'
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbBulkOutPipe) -> win32more.Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: win32more.Windows.Devices.Usb.IUsbBulkOutPipe) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def put_WriteOptions(self: win32more.Windows.Devices.Usb.IUsbBulkOutPipe, value: win32more.Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_mixinmethod
    def get_WriteOptions(self: win32more.Windows.Devices.Usb.IUsbBulkOutPipe) -> win32more.Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Devices.Usb.IUsbBulkOutPipe) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
class UsbConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbConfiguration
    _classid_ = 'Windows.Devices.Usb.UsbConfiguration'
    @winrt_mixinmethod
    def get_UsbInterfaces(self: win32more.Windows.Devices.Usb.IUsbConfiguration) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterface]: ...
    @winrt_mixinmethod
    def get_ConfigurationDescriptor(self: win32more.Windows.Devices.Usb.IUsbConfiguration) -> win32more.Windows.Devices.Usb.UsbConfigurationDescriptor: ...
    @winrt_mixinmethod
    def get_Descriptors(self: win32more.Windows.Devices.Usb.IUsbConfiguration) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbDescriptor]: ...
    UsbInterfaces = property(get_UsbInterfaces, None)
    ConfigurationDescriptor = property(get_ConfigurationDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class UsbConfigurationDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbConfigurationDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbConfigurationDescriptor'
    @winrt_mixinmethod
    def get_ConfigurationValue(self: win32more.Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_MaxPowerMilliamps(self: win32more.Windows.Devices.Usb.IUsbConfigurationDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelfPowered(self: win32more.Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def get_RemoteWakeup(self: win32more.Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Boolean: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Devices.Usb.IUsbConfigurationDescriptorStatics, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(win32more.Windows.Devices.Usb.UsbConfigurationDescriptor)) -> Boolean: ...
    @winrt_classmethod
    def Parse(cls: win32more.Windows.Devices.Usb.IUsbConfigurationDescriptorStatics, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor) -> win32more.Windows.Devices.Usb.UsbConfigurationDescriptor: ...
    ConfigurationValue = property(get_ConfigurationValue, None)
    MaxPowerMilliamps = property(get_MaxPowerMilliamps, None)
    SelfPowered = property(get_SelfPowered, None)
    RemoteWakeup = property(get_RemoteWakeup, None)
UsbControlRecipient = Int32
UsbControlRecipient_Device: UsbControlRecipient = 0
UsbControlRecipient_SpecifiedInterface: UsbControlRecipient = 1
UsbControlRecipient_Endpoint: UsbControlRecipient = 2
UsbControlRecipient_Other: UsbControlRecipient = 3
UsbControlRecipient_DefaultInterface: UsbControlRecipient = 4
class UsbControlRequestType(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbControlRequestType
    _classid_ = 'Windows.Devices.Usb.UsbControlRequestType'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Usb.UsbControlRequestType: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.Devices.Usb.IUsbControlRequestType) -> win32more.Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Windows.Devices.Usb.IUsbControlRequestType, value: win32more.Windows.Devices.Usb.UsbTransferDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ControlTransferType(self: win32more.Windows.Devices.Usb.IUsbControlRequestType) -> win32more.Windows.Devices.Usb.UsbControlTransferType: ...
    @winrt_mixinmethod
    def put_ControlTransferType(self: win32more.Windows.Devices.Usb.IUsbControlRequestType, value: win32more.Windows.Devices.Usb.UsbControlTransferType) -> Void: ...
    @winrt_mixinmethod
    def get_Recipient(self: win32more.Windows.Devices.Usb.IUsbControlRequestType) -> win32more.Windows.Devices.Usb.UsbControlRecipient: ...
    @winrt_mixinmethod
    def put_Recipient(self: win32more.Windows.Devices.Usb.IUsbControlRequestType, value: win32more.Windows.Devices.Usb.UsbControlRecipient) -> Void: ...
    @winrt_mixinmethod
    def get_AsByte(self: win32more.Windows.Devices.Usb.IUsbControlRequestType) -> Byte: ...
    @winrt_mixinmethod
    def put_AsByte(self: win32more.Windows.Devices.Usb.IUsbControlRequestType, value: Byte) -> Void: ...
    Direction = property(get_Direction, put_Direction)
    ControlTransferType = property(get_ControlTransferType, put_ControlTransferType)
    Recipient = property(get_Recipient, put_Recipient)
    AsByte = property(get_AsByte, put_AsByte)
UsbControlTransferType = Int32
UsbControlTransferType_Standard: UsbControlTransferType = 0
UsbControlTransferType_Class: UsbControlTransferType = 1
UsbControlTransferType_Vendor: UsbControlTransferType = 2
class UsbDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbDescriptor'
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.Devices.Usb.IUsbDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_DescriptorType(self: win32more.Windows.Devices.Usb.IUsbDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def ReadDescriptorBuffer(self: win32more.Windows.Devices.Usb.IUsbDescriptor, buffer: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Length = property(get_Length, None)
    DescriptorType = property(get_DescriptorType, None)
class UsbDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbDevice
    _classid_ = 'Windows.Devices.Usb.UsbDevice'
    @winrt_mixinmethod
    def SendControlOutTransferAsync(self: win32more.Windows.Devices.Usb.IUsbDevice, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def SendControlOutTransferAsyncNoBuffer(self: win32more.Windows.Devices.Usb.IUsbDevice, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def SendControlInTransferAsync(self: win32more.Windows.Devices.Usb.IUsbDevice, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def SendControlInTransferAsyncNoBuffer(self: win32more.Windows.Devices.Usb.IUsbDevice, setupPacket: win32more.Windows.Devices.Usb.UsbSetupPacket) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def get_DefaultInterface(self: win32more.Windows.Devices.Usb.IUsbDevice) -> win32more.Windows.Devices.Usb.UsbInterface: ...
    @winrt_mixinmethod
    def get_DeviceDescriptor(self: win32more.Windows.Devices.Usb.IUsbDevice) -> win32more.Windows.Devices.Usb.UsbDeviceDescriptor: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Devices.Usb.IUsbDevice) -> win32more.Windows.Devices.Usb.UsbConfiguration: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Usb.IUsbDeviceStatics, vendorId: UInt32, productId: UInt32, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorGuidOnly(cls: win32more.Windows.Devices.Usb.IUsbDeviceStatics, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorVidPidOnly(cls: win32more.Windows.Devices.Usb.IUsbDeviceStatics, vendorId: UInt32, productId: UInt32) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceClassSelector(cls: win32more.Windows.Devices.Usb.IUsbDeviceStatics, usbClass: win32more.Windows.Devices.Usb.UsbDeviceClass) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Usb.IUsbDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Usb.UsbDevice]: ...
    DefaultInterface = property(get_DefaultInterface, None)
    DeviceDescriptor = property(get_DeviceDescriptor, None)
    Configuration = property(get_Configuration, None)
class UsbDeviceClass(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbDeviceClass
    _classid_ = 'Windows.Devices.Usb.UsbDeviceClass'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_mixinmethod
    def get_ClassCode(self: win32more.Windows.Devices.Usb.IUsbDeviceClass) -> Byte: ...
    @winrt_mixinmethod
    def put_ClassCode(self: win32more.Windows.Devices.Usb.IUsbDeviceClass, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_SubclassCode(self: win32more.Windows.Devices.Usb.IUsbDeviceClass) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def put_SubclassCode(self: win32more.Windows.Devices.Usb.IUsbDeviceClass, value: win32more.Windows.Foundation.IReference[Byte]) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolCode(self: win32more.Windows.Devices.Usb.IUsbDeviceClass) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def put_ProtocolCode(self: win32more.Windows.Devices.Usb.IUsbDeviceClass, value: win32more.Windows.Foundation.IReference[Byte]) -> Void: ...
    ClassCode = property(get_ClassCode, put_ClassCode)
    SubclassCode = property(get_SubclassCode, put_SubclassCode)
    ProtocolCode = property(get_ProtocolCode, put_ProtocolCode)
class _UsbDeviceClasses_Meta_(ComPtr.__class__):
    pass
class UsbDeviceClasses(ComPtr, metaclass=_UsbDeviceClasses_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbDeviceClasses
    _classid_ = 'Windows.Devices.Usb.UsbDeviceClasses'
    @winrt_classmethod
    def get_CdcControl(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_Physical(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_PersonalHealthcare(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_ActiveSync(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_PalmSync(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_DeviceFirmwareUpdate(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_Irda(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_Measurement(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_VendorSpecific(cls: win32more.Windows.Devices.Usb.IUsbDeviceClassesStatics) -> win32more.Windows.Devices.Usb.UsbDeviceClass: ...
    _UsbDeviceClasses_Meta_.CdcControl = property(get_CdcControl.__wrapped__, None)
    _UsbDeviceClasses_Meta_.Physical = property(get_Physical.__wrapped__, None)
    _UsbDeviceClasses_Meta_.PersonalHealthcare = property(get_PersonalHealthcare.__wrapped__, None)
    _UsbDeviceClasses_Meta_.ActiveSync = property(get_ActiveSync.__wrapped__, None)
    _UsbDeviceClasses_Meta_.PalmSync = property(get_PalmSync.__wrapped__, None)
    _UsbDeviceClasses_Meta_.DeviceFirmwareUpdate = property(get_DeviceFirmwareUpdate.__wrapped__, None)
    _UsbDeviceClasses_Meta_.Irda = property(get_Irda.__wrapped__, None)
    _UsbDeviceClasses_Meta_.Measurement = property(get_Measurement.__wrapped__, None)
    _UsbDeviceClasses_Meta_.VendorSpecific = property(get_VendorSpecific.__wrapped__, None)
class UsbDeviceDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbDeviceDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbDeviceDescriptor'
    @winrt_mixinmethod
    def get_BcdUsb(self: win32more.Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxPacketSize0(self: win32more.Windows.Devices.Usb.IUsbDeviceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_VendorId(self: win32more.Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_BcdDeviceRevision(self: win32more.Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_NumberOfConfigurations(self: win32more.Windows.Devices.Usb.IUsbDeviceDescriptor) -> Byte: ...
    BcdUsb = property(get_BcdUsb, None)
    MaxPacketSize0 = property(get_MaxPacketSize0, None)
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    BcdDeviceRevision = property(get_BcdDeviceRevision, None)
    NumberOfConfigurations = property(get_NumberOfConfigurations, None)
class UsbEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbEndpointDescriptor'
    @winrt_mixinmethod
    def get_EndpointNumber(self: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_mixinmethod
    def get_EndpointType(self: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbEndpointType: ...
    @winrt_mixinmethod
    def get_AsBulkInEndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_mixinmethod
    def get_AsInterruptInEndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_mixinmethod
    def get_AsBulkOutEndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_mixinmethod
    def get_AsInterruptOutEndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Devices.Usb.IUsbEndpointDescriptorStatics, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(win32more.Windows.Devices.Usb.UsbEndpointDescriptor)) -> Boolean: ...
    @winrt_classmethod
    def Parse(cls: win32more.Windows.Devices.Usb.IUsbEndpointDescriptorStatics, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor) -> win32more.Windows.Devices.Usb.UsbEndpointDescriptor: ...
    EndpointNumber = property(get_EndpointNumber, None)
    Direction = property(get_Direction, None)
    EndpointType = property(get_EndpointType, None)
    AsBulkInEndpointDescriptor = property(get_AsBulkInEndpointDescriptor, None)
    AsInterruptInEndpointDescriptor = property(get_AsInterruptInEndpointDescriptor, None)
    AsBulkOutEndpointDescriptor = property(get_AsBulkOutEndpointDescriptor, None)
    AsInterruptOutEndpointDescriptor = property(get_AsInterruptOutEndpointDescriptor, None)
UsbEndpointType = Int32
UsbEndpointType_Control: UsbEndpointType = 0
UsbEndpointType_Isochronous: UsbEndpointType = 1
UsbEndpointType_Bulk: UsbEndpointType = 2
UsbEndpointType_Interrupt: UsbEndpointType = 3
class UsbInterface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterface
    _classid_ = 'Windows.Devices.Usb.UsbInterface'
    @winrt_mixinmethod
    def get_BulkInPipes(self: win32more.Windows.Devices.Usb.IUsbInterface) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkInPipe]: ...
    @winrt_mixinmethod
    def get_InterruptInPipes(self: win32more.Windows.Devices.Usb.IUsbInterface) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptInPipe]: ...
    @winrt_mixinmethod
    def get_BulkOutPipes(self: win32more.Windows.Devices.Usb.IUsbInterface) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkOutPipe]: ...
    @winrt_mixinmethod
    def get_InterruptOutPipes(self: win32more.Windows.Devices.Usb.IUsbInterface) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptOutPipe]: ...
    @winrt_mixinmethod
    def get_InterfaceSettings(self: win32more.Windows.Devices.Usb.IUsbInterface) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterfaceSetting]: ...
    @winrt_mixinmethod
    def get_InterfaceNumber(self: win32more.Windows.Devices.Usb.IUsbInterface) -> Byte: ...
    @winrt_mixinmethod
    def get_Descriptors(self: win32more.Windows.Devices.Usb.IUsbInterface) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInPipes = property(get_BulkInPipes, None)
    InterruptInPipes = property(get_InterruptInPipes, None)
    BulkOutPipes = property(get_BulkOutPipes, None)
    InterruptOutPipes = property(get_InterruptOutPipes, None)
    InterfaceSettings = property(get_InterfaceSettings, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
    Descriptors = property(get_Descriptors, None)
class UsbInterfaceDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbInterfaceDescriptor'
    @winrt_mixinmethod
    def get_ClassCode(self: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_SubclassCode(self: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_ProtocolCode(self: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_AlternateSettingNumber(self: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_InterfaceNumber(self: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptorStatics, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(win32more.Windows.Devices.Usb.UsbInterfaceDescriptor)) -> Boolean: ...
    @winrt_classmethod
    def Parse(cls: win32more.Windows.Devices.Usb.IUsbInterfaceDescriptorStatics, descriptor: win32more.Windows.Devices.Usb.UsbDescriptor) -> win32more.Windows.Devices.Usb.UsbInterfaceDescriptor: ...
    ClassCode = property(get_ClassCode, None)
    SubclassCode = property(get_SubclassCode, None)
    ProtocolCode = property(get_ProtocolCode, None)
    AlternateSettingNumber = property(get_AlternateSettingNumber, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
class UsbInterfaceSetting(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterfaceSetting
    _classid_ = 'Windows.Devices.Usb.UsbInterfaceSetting'
    @winrt_mixinmethod
    def get_BulkInEndpoints(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkInEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_InterruptInEndpoints(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptInEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_BulkOutEndpoints(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbBulkOutEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_InterruptOutEndpoints(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_Selected(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> Boolean: ...
    @winrt_mixinmethod
    def SelectSettingAsync(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_InterfaceDescriptor(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> win32more.Windows.Devices.Usb.UsbInterfaceDescriptor: ...
    @winrt_mixinmethod
    def get_Descriptors(self: win32more.Windows.Devices.Usb.IUsbInterfaceSetting) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInEndpoints = property(get_BulkInEndpoints, None)
    InterruptInEndpoints = property(get_InterruptInEndpoints, None)
    BulkOutEndpoints = property(get_BulkOutEndpoints, None)
    InterruptOutEndpoints = property(get_InterruptOutEndpoints, None)
    Selected = property(get_Selected, None)
    InterfaceDescriptor = property(get_InterfaceDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class UsbInterruptInEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbInterruptInEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: win32more.Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: win32more.Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Pipe(self: win32more.Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbInterruptInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class UsbInterruptInEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterruptInEventArgs
    _classid_ = 'Windows.Devices.Usb.UsbInterruptInEventArgs'
    @winrt_mixinmethod
    def get_InterruptData(self: win32more.Windows.Devices.Usb.IUsbInterruptInEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
    InterruptData = property(get_InterruptData, None)
class UsbInterruptInPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterruptInPipe
    _classid_ = 'Windows.Devices.Usb.UsbInterruptInPipe'
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbInterruptInPipe) -> win32more.Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: win32more.Windows.Devices.Usb.IUsbInterruptInPipe) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_DataReceived(self: win32more.Windows.Devices.Usb.IUsbInterruptInPipe, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Usb.UsbInterruptInPipe, win32more.Windows.Devices.Usb.UsbInterruptInEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataReceived(self: win32more.Windows.Devices.Usb.IUsbInterruptInPipe, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
class UsbInterruptOutEndpointDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: win32more.Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: win32more.Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Pipe(self: win32more.Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> win32more.Windows.Devices.Usb.UsbInterruptOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class UsbInterruptOutPipe(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbInterruptOutPipe
    _classid_ = 'Windows.Devices.Usb.UsbInterruptOutPipe'
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: win32more.Windows.Devices.Usb.IUsbInterruptOutPipe) -> win32more.Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: win32more.Windows.Devices.Usb.IUsbInterruptOutPipe) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def put_WriteOptions(self: win32more.Windows.Devices.Usb.IUsbInterruptOutPipe, value: win32more.Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_mixinmethod
    def get_WriteOptions(self: win32more.Windows.Devices.Usb.IUsbInterruptOutPipe) -> win32more.Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Devices.Usb.IUsbInterruptOutPipe) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
UsbReadOptions = UInt32
UsbReadOptions_None: UsbReadOptions = 0
UsbReadOptions_AutoClearStall: UsbReadOptions = 1
UsbReadOptions_OverrideAutomaticBufferManagement: UsbReadOptions = 2
UsbReadOptions_IgnoreShortPacket: UsbReadOptions = 4
UsbReadOptions_AllowPartialReads: UsbReadOptions = 8
class UsbSetupPacket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Usb.IUsbSetupPacket
    _classid_ = 'Windows.Devices.Usb.UsbSetupPacket'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Usb.UsbSetupPacket: ...
    @winrt_factorymethod
    def CreateWithEightByteBuffer(cls: win32more.Windows.Devices.Usb.IUsbSetupPacketFactory, eightByteBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Usb.UsbSetupPacket: ...
    @winrt_mixinmethod
    def get_RequestType(self: win32more.Windows.Devices.Usb.IUsbSetupPacket) -> win32more.Windows.Devices.Usb.UsbControlRequestType: ...
    @winrt_mixinmethod
    def put_RequestType(self: win32more.Windows.Devices.Usb.IUsbSetupPacket, value: win32more.Windows.Devices.Usb.UsbControlRequestType) -> Void: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.Usb.IUsbSetupPacket) -> Byte: ...
    @winrt_mixinmethod
    def put_Request(self: win32more.Windows.Devices.Usb.IUsbSetupPacket, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Index(self: win32more.Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_mixinmethod
    def put_Index(self: win32more.Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_mixinmethod
    def put_Length(self: win32more.Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    RequestType = property(get_RequestType, put_RequestType)
    Request = property(get_Request, put_Request)
    Value = property(get_Value, put_Value)
    Index = property(get_Index, put_Index)
    Length = property(get_Length, put_Length)
UsbTransferDirection = Int32
UsbTransferDirection_Out: UsbTransferDirection = 0
UsbTransferDirection_In: UsbTransferDirection = 1
UsbWriteOptions = UInt32
UsbWriteOptions_None: UsbWriteOptions = 0
UsbWriteOptions_AutoClearStall: UsbWriteOptions = 1
UsbWriteOptions_ShortPacketTerminate: UsbWriteOptions = 2
make_ready(__name__)
