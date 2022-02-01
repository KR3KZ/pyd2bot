from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportToBuddyCloseMessage(INetworkMessage):
    protocolId = 2991
    dungeonId:int
    buddyId:int
    
    
