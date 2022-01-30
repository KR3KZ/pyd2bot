from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class PlayerSearchTagInformation(AbstractPlayerSearchInformation):
    protocolId = 3556
    tag:AccountTagInformation
    
