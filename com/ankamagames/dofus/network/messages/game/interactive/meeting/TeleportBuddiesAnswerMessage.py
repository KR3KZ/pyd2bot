from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportBuddiesAnswerMessage(INetworkMessage):
    protocolId = 3499
    accept:bool
    
    
