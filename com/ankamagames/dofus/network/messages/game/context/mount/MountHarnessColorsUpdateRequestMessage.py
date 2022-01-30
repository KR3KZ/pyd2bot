from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountHarnessColorsUpdateRequestMessage(INetworkMessage):
    protocolId = 7947
    useHarnessColors:bool
    
    
