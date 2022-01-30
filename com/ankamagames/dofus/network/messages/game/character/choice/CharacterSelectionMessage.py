from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterSelectionMessage(NetworkMessage):
    protocolId = 3123
    id:int
    
    
