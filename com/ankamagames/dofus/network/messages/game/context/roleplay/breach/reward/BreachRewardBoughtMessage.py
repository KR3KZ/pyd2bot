from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachRewardBoughtMessage(INetworkMessage):
    protocolId = 3950
    id:int
    bought:bool
    
    
