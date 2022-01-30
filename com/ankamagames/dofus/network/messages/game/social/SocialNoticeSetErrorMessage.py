from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SocialNoticeSetErrorMessage(NetworkMessage):
    protocolId = 3378
    reason:int
    
