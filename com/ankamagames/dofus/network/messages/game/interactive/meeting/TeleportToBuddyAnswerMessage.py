from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportToBuddyAnswerMessage(INetworkMessage):
    protocolId = 5687
    dungeonId:int
    buddyId:int
    accept:bool
    
    
