from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameActionFightCastRequestMessage(INetworkMessage):
    protocolId = 4946
    spellId:int
    cellId:int
    
    
