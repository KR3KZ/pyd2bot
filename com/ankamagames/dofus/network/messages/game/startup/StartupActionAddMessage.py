from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject


class StartupActionAddMessage(INetworkMessage):
    protocolId = 1592
    newAction:StartupActionAddObject
    
    
