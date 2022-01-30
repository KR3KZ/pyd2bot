from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismFightersInformation import PrismFightersInformation


class PrismsInfoValidMessage(NetworkMessage):
    protocolId = 9294
    fights:list[PrismFightersInformation]
    
