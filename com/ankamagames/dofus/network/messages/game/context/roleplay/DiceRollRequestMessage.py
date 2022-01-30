from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DiceRollRequestMessage(INetworkMessage):
    protocolId = 932
    dice:int
    faces:int
    channel:int
    
    
