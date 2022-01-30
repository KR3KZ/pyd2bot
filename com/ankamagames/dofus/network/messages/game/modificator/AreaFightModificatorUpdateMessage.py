from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AreaFightModificatorUpdateMessage(INetworkMessage):
    protocolId = 4779
    spellPairId:int
    
    
