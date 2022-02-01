from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveDetailedInformations import QuestActiveDetailedInformations


class FollowedQuestsMessage(NetworkMessage):
    quests:list[QuestActiveDetailedInformations]
    
    
