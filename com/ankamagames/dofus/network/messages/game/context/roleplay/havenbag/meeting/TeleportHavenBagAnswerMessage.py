from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportHavenBagAnswerMessage(INetworkMessage):
    protocolId = 597
    accept:bool
    
    
