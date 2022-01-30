from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


class QuestStepInfoMessage(NetworkMessage):
    protocolId = 7690
    infos:QuestActiveInformations
    
