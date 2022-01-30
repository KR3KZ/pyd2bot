from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportToBuddyCloseMessage(INetworkMessage):
    protocolId = 2991
    dungeonId:int
    buddyId:int
    
    
