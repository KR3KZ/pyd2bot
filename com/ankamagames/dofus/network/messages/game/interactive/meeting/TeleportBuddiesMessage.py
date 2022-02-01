from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportBuddiesMessage(INetworkMessage):
    protocolId = 9150
    dungeonId:int
    
    
