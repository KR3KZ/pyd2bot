from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportToBuddyCloseMessage(NetworkMessage):
    protocolId = 2991
    dungeonId:int
    buddyId:int
    
    
