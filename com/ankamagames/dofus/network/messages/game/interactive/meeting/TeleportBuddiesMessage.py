from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportBuddiesMessage(NetworkMessage):
    protocolId = 9150
    dungeonId:int
    
    
