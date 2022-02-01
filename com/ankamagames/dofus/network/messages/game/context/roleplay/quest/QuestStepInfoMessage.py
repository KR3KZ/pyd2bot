from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


class QuestStepInfoMessage(NetworkMessage):
    infos:QuestActiveInformations
    
    
