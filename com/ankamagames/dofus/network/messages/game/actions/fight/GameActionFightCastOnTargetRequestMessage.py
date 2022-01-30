from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameActionFightCastOnTargetRequestMessage(INetworkMessage):
    protocolId = 8001
    spellId:int
    targetId:int
    
    
