from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MoodSmileyRequestMessage(NetworkMessage):
    protocolId = 610
    smileyId:int
    
