from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarRefreshMessage(INetworkMessage):
    protocolId = 4458
    barType:int
    shortcut:Shortcut
    
    
