from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class DiceRollRequestMessage(NetworkMessage):
    protocolId = 932
    dice:int
    faces:int
    channel:int
    
