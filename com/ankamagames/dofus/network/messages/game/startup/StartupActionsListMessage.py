from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject


class StartupActionsListMessage(INetworkMessage):
    protocolId = 798
    actions:StartupActionAddObject
    
    
