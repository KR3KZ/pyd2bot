from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInstancesInformations import PaddockInstancesInformations


class PaddockPropertiesMessage(NetworkMessage):
    protocolId = 3194
    properties:PaddockInstancesInformations
    
    
