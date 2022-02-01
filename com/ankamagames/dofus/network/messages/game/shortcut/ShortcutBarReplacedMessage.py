from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarReplacedMessage(INetworkMessage):
    protocolId = 5103
    barType:int
    shortcut:Shortcut
    
    
