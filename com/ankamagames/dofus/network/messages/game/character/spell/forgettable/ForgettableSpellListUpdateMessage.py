from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import ForgettableSpellItem


class ForgettableSpellListUpdateMessage(INetworkMessage):
    protocolId = 9946
    action:int
    spells:ForgettableSpellItem
    
    