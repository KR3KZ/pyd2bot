from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismFightersInformation import PrismFightersInformation


class PrismFightAddedMessage(NetworkMessage):
    protocolId = 5778
    fight:PrismFightersInformation
    
