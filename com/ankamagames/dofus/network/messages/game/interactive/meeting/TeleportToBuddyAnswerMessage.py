from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TeleportToBuddyAnswerMessage(NetworkMessage):
    protocolId = 5687
    dungeonId:int
    buddyId:int
    accept:bool
    
