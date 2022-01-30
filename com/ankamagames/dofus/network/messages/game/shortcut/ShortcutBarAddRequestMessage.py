from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarAddRequestMessage(INetworkMessage):
    protocolId = 9513
    barType:int
    shortcut:Shortcut
    
    
