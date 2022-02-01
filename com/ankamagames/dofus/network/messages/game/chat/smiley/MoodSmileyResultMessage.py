from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MoodSmileyResultMessage(INetworkMessage):
    protocolId = 6000
    resultCode:int
    smileyId:int
    
    
