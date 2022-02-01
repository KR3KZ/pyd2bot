from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportToBuddyOfferMessage(INetworkMessage):
    protocolId = 4009
    dungeonId:int
    buddyId:int
    timeLeft:int
    
    
