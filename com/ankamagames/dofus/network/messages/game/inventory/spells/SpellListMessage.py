from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem


class SpellListMessage(NetworkMessage):
    protocolId = 4091
    spellPrevisualization:bool
    spells:SpellItem
    
