from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristics(INetworkMessage):
    protocolId = 5368
    characteristics:CharacterCharacteristic
    
    
