from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveDetailedInformations import QuestActiveDetailedInformations


class FollowedQuestsMessage(NetworkMessage):
    protocolId = 414
    quests:list[QuestActiveDetailedInformations]
    
