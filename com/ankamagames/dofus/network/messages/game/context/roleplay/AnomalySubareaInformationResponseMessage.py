from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AnomalySubareaInformation import AnomalySubareaInformation


class AnomalySubareaInformationResponseMessage(INetworkMessage):
    protocolId = 6030
    subareas:AnomalySubareaInformation
    
    
