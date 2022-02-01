from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarRefreshMessage(INetworkMessage):
    protocolId = 4458
    barType:int
    shortcut:Shortcut
    
    
