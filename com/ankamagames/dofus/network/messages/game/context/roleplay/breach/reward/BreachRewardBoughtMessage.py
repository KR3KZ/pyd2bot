from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachRewardBoughtMessage(NetworkMessage):
    protocolId = 3950
    id:int
    bought:bool
    
