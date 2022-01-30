from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveDetailedInformations import QuestActiveDetailedInformations


class FollowedQuestsMessage(INetworkMessage):
    protocolId = 414
    quests:QuestActiveDetailedInformations
    
    
