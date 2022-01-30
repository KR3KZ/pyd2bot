from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarReplacedMessage(NetworkMessage):
    protocolId = 5103
    barType:int
    shortcut:Shortcut
    
    
