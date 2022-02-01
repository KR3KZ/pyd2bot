from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject


class StartupActionsListMessage(NetworkMessage):
    actions:list[StartupActionAddObject]
    
    
