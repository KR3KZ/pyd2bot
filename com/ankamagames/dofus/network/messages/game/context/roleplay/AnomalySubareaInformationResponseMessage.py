from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AnomalySubareaInformation import AnomalySubareaInformation


class AnomalySubareaInformationResponseMessage(NetworkMessage):
    subareas:list[AnomalySubareaInformation]
    
    
