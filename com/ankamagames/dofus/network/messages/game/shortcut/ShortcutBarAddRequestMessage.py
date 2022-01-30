from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarAddRequestMessage(NetworkMessage):
    protocolId = 9513
    barType:int
    shortcut:Shortcut
    
    
