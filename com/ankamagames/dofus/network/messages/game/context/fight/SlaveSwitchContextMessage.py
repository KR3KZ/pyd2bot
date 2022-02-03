from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
    from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut
    


class SlaveSwitchContextMessage(NetworkMessage):
    masterId:int
    slaveId:int
    slaveTurn:int
    slaveSpells:list['SpellItem']
    slaveStats:'CharacterCharacteristicsInformations'
    shortcuts:list['Shortcut']
    

    def init(self, masterId:int, slaveId:int, slaveTurn:int, slaveSpells:list['SpellItem'], slaveStats:'CharacterCharacteristicsInformations', shortcuts:list['Shortcut']):
        self.masterId = masterId
        self.slaveId = slaveId
        self.slaveTurn = slaveTurn
        self.slaveSpells = slaveSpells
        self.slaveStats = slaveStats
        self.shortcuts = shortcuts
        
        super().__init__()
    
    