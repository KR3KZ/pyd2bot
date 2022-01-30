from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameActionAcknowledgementMessage(INetworkMessage):
    protocolId = 3561
    valid:bool
    actionId:int
    
    
