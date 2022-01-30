from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MoodSmileyResultMessage(INetworkMessage):
    protocolId = 6000
    resultCode:int
    smileyId:int
    
    
