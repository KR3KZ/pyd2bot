from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportHavenBagAnswerMessage(INetworkMessage):
    protocolId = 597
    accept:bool
    
    
