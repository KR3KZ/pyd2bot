from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SocialNoticeSetErrorMessage(INetworkMessage):
    protocolId = 3378
    reason:int
    
    
