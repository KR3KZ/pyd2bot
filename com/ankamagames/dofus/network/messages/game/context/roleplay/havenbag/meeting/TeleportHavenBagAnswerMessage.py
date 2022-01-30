from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportHavenBagAnswerMessage(NetworkMessage):
    protocolId = 597
    accept:bool
    
    
