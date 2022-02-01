from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportBuddiesAnswerMessage(INetworkMessage):
    protocolId = 3499
    accept:bool
    
    
