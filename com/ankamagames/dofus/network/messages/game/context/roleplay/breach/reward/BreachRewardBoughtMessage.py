from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachRewardBoughtMessage(INetworkMessage):
    protocolId = 3950
    id:int
    bought:bool
    
    
