from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class SlaveSwitchContextMessage(NetworkMessage):
    masterId:int
    slaveId:int
    slaveTurn:int
    slaveSpells:list[SpellItem]
    slaveStats:CharacterCharacteristicsInformations
    shortcuts:list[Shortcut]
    
    
