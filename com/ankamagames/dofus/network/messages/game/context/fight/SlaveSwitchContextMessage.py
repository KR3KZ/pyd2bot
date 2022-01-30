from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class SlaveSwitchContextMessage(INetworkMessage):
    protocolId = 6013
    masterId:int
    slaveId:int
    slaveTurn:int
    slaveSpells:SpellItem
    slaveStats:CharacterCharacteristicsInformations
    shortcuts:Shortcut
    
    
