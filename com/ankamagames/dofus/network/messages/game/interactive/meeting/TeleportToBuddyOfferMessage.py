from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportToBuddyOfferMessage(INetworkMessage):
    protocolId = 4009
    dungeonId:int
    buddyId:int
    timeLeft:int
    
    
