from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AnomalySubareaInformation import AnomalySubareaInformation


class AnomalySubareaInformationResponseMessage(NetworkMessage):
    protocolId = 6030
    subareas:list[AnomalySubareaInformation]
    
