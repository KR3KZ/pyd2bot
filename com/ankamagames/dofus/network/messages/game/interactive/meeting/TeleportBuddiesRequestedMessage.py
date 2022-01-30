from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportBuddiesRequestedMessage(INetworkMessage):
    protocolId = 9435
    dungeonId:int
    inviterId:int
    invalidBuddiesIds:int
    
    
