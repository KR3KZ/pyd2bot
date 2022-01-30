from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightLeaveMessage(INetworkMessage):
    protocolId = 4663
    charId:int
    
    
