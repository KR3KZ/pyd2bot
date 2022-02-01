from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


class ServerSessionConstantsMessage(NetworkMessage):
    variables:list[ServerSessionConstant]
    
    
