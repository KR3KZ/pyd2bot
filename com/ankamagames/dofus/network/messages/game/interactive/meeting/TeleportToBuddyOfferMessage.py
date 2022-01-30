from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportToBuddyOfferMessage(NetworkMessage):
    protocolId = 4009
    dungeonId:int
    buddyId:int
    timeLeft:int
    
