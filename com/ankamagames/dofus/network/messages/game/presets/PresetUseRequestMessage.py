from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PresetUseRequestMessage(INetworkMessage):
    protocolId = 1855
    presetId:int
    
    
