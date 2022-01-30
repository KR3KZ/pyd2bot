from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


class QuestStepInfoMessage(INetworkMessage):
    protocolId = 7690
    infos:QuestActiveInformations
    
    
