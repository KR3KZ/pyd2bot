from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


class BasicWhoIsRequestMessage(NetworkMessage):
    verbose:bool
    target:AbstractPlayerSearchInformation
    
    
