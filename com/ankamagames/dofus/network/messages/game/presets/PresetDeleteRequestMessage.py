from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PresetDeleteRequestMessage(INetworkMessage):
    protocolId = 3688
    presetId:int
    
    
