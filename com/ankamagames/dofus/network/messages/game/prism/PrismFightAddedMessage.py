from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.prism.PrismFightersInformation import PrismFightersInformation


class PrismFightAddedMessage(INetworkMessage):
    protocolId = 5778
    fight:PrismFightersInformation
    
    
