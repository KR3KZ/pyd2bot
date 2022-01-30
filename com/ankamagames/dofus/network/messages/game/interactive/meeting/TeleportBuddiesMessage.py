from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportBuddiesMessage(INetworkMessage):
    protocolId = 9150
    dungeonId:int
    
    
