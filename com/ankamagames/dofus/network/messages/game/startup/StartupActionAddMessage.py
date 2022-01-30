from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.startup.StartupActionAddObject import StartupActionAddObject


class StartupActionAddMessage(NetworkMessage):
    protocolId = 1592
    newAction:StartupActionAddObject
    
