from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportBuddiesAnswerMessage(NetworkMessage):
    protocolId = 3499
    accept:bool
    
