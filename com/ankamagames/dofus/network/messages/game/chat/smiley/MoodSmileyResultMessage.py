from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MoodSmileyResultMessage(NetworkMessage):
    protocolId = 6000
    resultCode:int
    smileyId:int
    
