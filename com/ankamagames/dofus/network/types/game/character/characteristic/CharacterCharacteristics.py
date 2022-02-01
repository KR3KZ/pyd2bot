from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristics(NetworkMessage):
    characteristics:list[CharacterCharacteristic]
    
    
