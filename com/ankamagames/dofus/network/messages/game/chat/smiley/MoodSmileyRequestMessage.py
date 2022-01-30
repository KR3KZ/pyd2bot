from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MoodSmileyRequestMessage(INetworkMessage):
    protocolId = 610
    smileyId:int
    
    
