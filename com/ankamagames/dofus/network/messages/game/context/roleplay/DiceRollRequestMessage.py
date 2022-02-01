from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DiceRollRequestMessage(NetworkMessage):
    dice:int
    faces:int
    channel:int
    
    
