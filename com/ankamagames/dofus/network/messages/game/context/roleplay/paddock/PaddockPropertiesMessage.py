from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInstancesInformations import PaddockInstancesInformations


class PaddockPropertiesMessage(INetworkMessage):
    protocolId = 3194
    properties:PaddockInstancesInformations
    
    
