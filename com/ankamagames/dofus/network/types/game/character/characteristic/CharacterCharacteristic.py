from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterCharacteristic(NetworkMessage):
    protocolId = 4565
    characteristicId:int
    
