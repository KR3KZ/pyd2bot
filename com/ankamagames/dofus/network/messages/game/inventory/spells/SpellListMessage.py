from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem


class SpellListMessage(INetworkMessage):
    protocolId = 4091
    spellPrevisualization:bool
    spells:SpellItem
    
    
