from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import ForgettableSpellItem


class ForgettableSpellListUpdateMessage(NetworkMessage):
    protocolId = 9946
    action:int
    spells:ForgettableSpellItem
    
    
