from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from com.ankamagames.dofus.network.types.game.paddock.PaddockBuyableInformations import PaddockBuyableInformations


class PaddockInstancesInformations(PaddockInformations):
    protocolId = 3435
    paddocks:PaddockBuyableInformations
    
