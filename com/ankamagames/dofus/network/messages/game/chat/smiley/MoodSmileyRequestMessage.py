from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MoodSmileyRequestMessage(INetworkMessage):
    protocolId = 610
    smileyId:int
    
    
