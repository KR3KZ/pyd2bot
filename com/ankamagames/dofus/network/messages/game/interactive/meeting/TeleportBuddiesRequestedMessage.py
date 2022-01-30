from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportBuddiesRequestedMessage(NetworkMessage):
    protocolId = 9435
    dungeonId:int
    inviterId:float
    invalidBuddiesIds:list[float]
    
