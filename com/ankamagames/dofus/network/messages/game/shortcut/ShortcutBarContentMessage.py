from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutBarContentMessage(NetworkMessage):
    protocolId = 7910
    barType:int
    shortcuts:list[Shortcut]
    
