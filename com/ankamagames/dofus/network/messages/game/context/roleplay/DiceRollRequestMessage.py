from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DiceRollRequestMessage(INetworkMessage):
    protocolId = 932
    dice:int
    faces:int
    channel:int
    
    
