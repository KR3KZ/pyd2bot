from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristics(NetworkMessage):
    protocolId = 5368
    characteristics:CharacterCharacteristic
    
