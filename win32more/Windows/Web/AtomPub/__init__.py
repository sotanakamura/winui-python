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
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Credentials
import win32more.Windows.Storage.Streams
import win32more.Windows.Web.AtomPub
import win32more.Windows.Web.Syndication
class AtomPubClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.AtomPub.IAtomPubClient
    _classid_ = 'Windows.Web.AtomPub.AtomPubClient'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.AtomPub.AtomPubClient: ...
    @winrt_factorymethod
    def CreateAtomPubClientWithCredentials(cls: win32more.Windows.Web.AtomPub.IAtomPubClientFactory, serverCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.Web.AtomPub.AtomPubClient: ...
    @winrt_mixinmethod
    def RetrieveServiceDocumentAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.AtomPub.ServiceDocument, win32more.Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_mixinmethod
    def RetrieveMediaResourceAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, win32more.Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_mixinmethod
    def RetrieveResourceAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Syndication.SyndicationItem, win32more.Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_mixinmethod
    def CreateResourceAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri, description: WinRT_String, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Syndication.SyndicationItem, win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def CreateMediaResourceAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri, mediaType: WinRT_String, description: WinRT_String, mediaStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Syndication.SyndicationItem, win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def UpdateMediaResourceAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri, mediaType: WinRT_String, mediaStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def UpdateResourceAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def UpdateResourceItemAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def DeleteResourceAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def DeleteResourceItemAsync(self: win32more.Windows.Web.AtomPub.IAtomPubClient, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_mixinmethod
    def CancelAsyncOperations(self: win32more.Windows.Web.AtomPub.IAtomPubClient) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: win32more.Windows.Web.Syndication.ISyndicationClient) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: win32more.Windows.Web.Syndication.ISyndicationClient, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: win32more.Windows.Web.Syndication.ISyndicationClient) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: win32more.Windows.Web.Syndication.ISyndicationClient, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_MaxResponseBufferSize(self: win32more.Windows.Web.Syndication.ISyndicationClient) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxResponseBufferSize(self: win32more.Windows.Web.Syndication.ISyndicationClient, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Timeout(self: win32more.Windows.Web.Syndication.ISyndicationClient) -> UInt32: ...
    @winrt_mixinmethod
    def put_Timeout(self: win32more.Windows.Web.Syndication.ISyndicationClient, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BypassCacheOnRetrieve(self: win32more.Windows.Web.Syndication.ISyndicationClient) -> Boolean: ...
    @winrt_mixinmethod
    def put_BypassCacheOnRetrieve(self: win32more.Windows.Web.Syndication.ISyndicationClient, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: win32more.Windows.Web.Syndication.ISyndicationClient, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RetrieveFeedAsync(self: win32more.Windows.Web.Syndication.ISyndicationClient, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Syndication.SyndicationFeed, win32more.Windows.Web.Syndication.RetrievalProgress]: ...
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    MaxResponseBufferSize = property(get_MaxResponseBufferSize, put_MaxResponseBufferSize)
    Timeout = property(get_Timeout, put_Timeout)
    BypassCacheOnRetrieve = property(get_BypassCacheOnRetrieve, put_BypassCacheOnRetrieve)
class IAtomPubClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IAtomPubClient'
    _iid_ = Guid('{35392c38-cded-4d4c-9637-05f15c1c9406}')
    @winrt_commethod(6)
    def RetrieveServiceDocumentAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.AtomPub.ServiceDocument, win32more.Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_commethod(7)
    def RetrieveMediaResourceAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IInputStream, win32more.Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_commethod(8)
    def RetrieveResourceAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Syndication.SyndicationItem, win32more.Windows.Web.Syndication.RetrievalProgress]: ...
    @winrt_commethod(9)
    def CreateResourceAsync(self, uri: win32more.Windows.Foundation.Uri, description: WinRT_String, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Syndication.SyndicationItem, win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(10)
    def CreateMediaResourceAsync(self, uri: win32more.Windows.Foundation.Uri, mediaType: WinRT_String, description: WinRT_String, mediaStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Web.Syndication.SyndicationItem, win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(11)
    def UpdateMediaResourceAsync(self, uri: win32more.Windows.Foundation.Uri, mediaType: WinRT_String, mediaStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(12)
    def UpdateResourceAsync(self, uri: win32more.Windows.Foundation.Uri, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(13)
    def UpdateResourceItemAsync(self, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(14)
    def DeleteResourceAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(15)
    def DeleteResourceItemAsync(self, item: win32more.Windows.Web.Syndication.SyndicationItem) -> win32more.Windows.Foundation.IAsyncActionWithProgress[win32more.Windows.Web.Syndication.TransferProgress]: ...
    @winrt_commethod(16)
    def CancelAsyncOperations(self) -> Void: ...
class IAtomPubClientFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IAtomPubClientFactory'
    _iid_ = Guid('{49d55012-57cb-4bde-ab9f-2610b172777b}')
    @winrt_commethod(6)
    def CreateAtomPubClientWithCredentials(self, serverCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.Web.AtomPub.AtomPubClient: ...
class IResourceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IResourceCollection'
    _iid_ = Guid('{7f5fd609-bc88-41d4-88fa-3de6704d428e}')
    @winrt_commethod(6)
    def get_Title(self) -> win32more.Windows.Web.Syndication.ISyndicationText: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Categories(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Syndication.SyndicationCategory]: ...
    @winrt_commethod(9)
    def get_Accepts(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Title = property(get_Title, None)
    Uri = property(get_Uri, None)
    Categories = property(get_Categories, None)
    Accepts = property(get_Accepts, None)
class IServiceDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IServiceDocument'
    _iid_ = Guid('{8b7ec771-2ab3-4dbe-8bcc-778f92b75e51}')
    @winrt_commethod(6)
    def get_Workspaces(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.AtomPub.Workspace]: ...
    Workspaces = property(get_Workspaces, None)
class IWorkspace(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.AtomPub.IWorkspace'
    _iid_ = Guid('{b41da63b-a4b8-4036-89c5-83c31266ba49}')
    @winrt_commethod(6)
    def get_Title(self) -> win32more.Windows.Web.Syndication.ISyndicationText: ...
    @winrt_commethod(7)
    def get_Collections(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.AtomPub.ResourceCollection]: ...
    Title = property(get_Title, None)
    Collections = property(get_Collections, None)
class ResourceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.AtomPub.IResourceCollection
    _classid_ = 'Windows.Web.AtomPub.ResourceCollection'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Web.AtomPub.IResourceCollection) -> win32more.Windows.Web.Syndication.ISyndicationText: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.AtomPub.IResourceCollection) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Categories(self: win32more.Windows.Web.AtomPub.IResourceCollection) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.Syndication.SyndicationCategory]: ...
    @winrt_mixinmethod
    def get_Accepts(self: win32more.Windows.Web.AtomPub.IResourceCollection) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_NodeName(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeName(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeNamespace(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeNamespace(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeValue(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeValue(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_BaseUri(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AttributeExtensions(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Syndication.SyndicationAttribute]: ...
    @winrt_mixinmethod
    def get_ElementExtensions(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Syndication.ISyndicationNode]: ...
    @winrt_mixinmethod
    def GetXmlDocument(self: win32more.Windows.Web.Syndication.ISyndicationNode, format: win32more.Windows.Web.Syndication.SyndicationFormat) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    Title = property(get_Title, None)
    Uri = property(get_Uri, None)
    Categories = property(get_Categories, None)
    Accepts = property(get_Accepts, None)
    NodeName = property(get_NodeName, put_NodeName)
    NodeNamespace = property(get_NodeNamespace, put_NodeNamespace)
    NodeValue = property(get_NodeValue, put_NodeValue)
    Language = property(get_Language, put_Language)
    BaseUri = property(get_BaseUri, put_BaseUri)
    AttributeExtensions = property(get_AttributeExtensions, None)
    ElementExtensions = property(get_ElementExtensions, None)
class ServiceDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.AtomPub.IServiceDocument
    _classid_ = 'Windows.Web.AtomPub.ServiceDocument'
    @winrt_mixinmethod
    def get_Workspaces(self: win32more.Windows.Web.AtomPub.IServiceDocument) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.AtomPub.Workspace]: ...
    @winrt_mixinmethod
    def get_NodeName(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeName(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeNamespace(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeNamespace(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeValue(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeValue(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_BaseUri(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AttributeExtensions(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Syndication.SyndicationAttribute]: ...
    @winrt_mixinmethod
    def get_ElementExtensions(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Syndication.ISyndicationNode]: ...
    @winrt_mixinmethod
    def GetXmlDocument(self: win32more.Windows.Web.Syndication.ISyndicationNode, format: win32more.Windows.Web.Syndication.SyndicationFormat) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    Workspaces = property(get_Workspaces, None)
    NodeName = property(get_NodeName, put_NodeName)
    NodeNamespace = property(get_NodeNamespace, put_NodeNamespace)
    NodeValue = property(get_NodeValue, put_NodeValue)
    Language = property(get_Language, put_Language)
    BaseUri = property(get_BaseUri, put_BaseUri)
    AttributeExtensions = property(get_AttributeExtensions, None)
    ElementExtensions = property(get_ElementExtensions, None)
class Workspace(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.AtomPub.IWorkspace
    _classid_ = 'Windows.Web.AtomPub.Workspace'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Web.AtomPub.IWorkspace) -> win32more.Windows.Web.Syndication.ISyndicationText: ...
    @winrt_mixinmethod
    def get_Collections(self: win32more.Windows.Web.AtomPub.IWorkspace) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.AtomPub.ResourceCollection]: ...
    @winrt_mixinmethod
    def get_NodeName(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeName(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeNamespace(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeNamespace(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NodeValue(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NodeValue(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BaseUri(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_BaseUri(self: win32more.Windows.Web.Syndication.ISyndicationNode, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AttributeExtensions(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Syndication.SyndicationAttribute]: ...
    @winrt_mixinmethod
    def get_ElementExtensions(self: win32more.Windows.Web.Syndication.ISyndicationNode) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.Syndication.ISyndicationNode]: ...
    @winrt_mixinmethod
    def GetXmlDocument(self: win32more.Windows.Web.Syndication.ISyndicationNode, format: win32more.Windows.Web.Syndication.SyndicationFormat) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    Title = property(get_Title, None)
    Collections = property(get_Collections, None)
    NodeName = property(get_NodeName, put_NodeName)
    NodeNamespace = property(get_NodeNamespace, put_NodeNamespace)
    NodeValue = property(get_NodeValue, put_NodeValue)
    Language = property(get_Language, put_Language)
    BaseUri = property(get_BaseUri, put_BaseUri)
    AttributeExtensions = property(get_AttributeExtensions, None)
    ElementExtensions = property(get_ElementExtensions, None)
make_ready(__name__)
