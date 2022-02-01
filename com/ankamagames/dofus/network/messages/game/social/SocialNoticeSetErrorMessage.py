from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SocialNoticeSetErrorMessage(INetworkMessage):
    protocolId = 3378
    reason:int
    
    
