from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


class ServerSessionConstantsMessage(INetworkMessage):
    protocolId = 646
    variables:ServerSessionConstant
    
    
