from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarRefreshMessage(NetworkMessage):
    protocolId = 4458
    barType:int
    shortcut:Shortcut
    
