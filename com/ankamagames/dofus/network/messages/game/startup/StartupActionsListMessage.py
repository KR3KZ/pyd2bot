from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject


class StartupActionsListMessage(NetworkMessage):
    protocolId = 798
    actions:list[StartupActionAddObject]
    
