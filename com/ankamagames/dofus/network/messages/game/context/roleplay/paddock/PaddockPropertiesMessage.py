from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInstancesInformations import PaddockInstancesInformations


class PaddockPropertiesMessage(NetworkMessage):
    properties:PaddockInstancesInformations
    
    
