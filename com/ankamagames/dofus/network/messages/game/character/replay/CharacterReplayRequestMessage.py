from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterReplayRequestMessage(NetworkMessage):
    protocolId = 9614
    characterId:float
    
