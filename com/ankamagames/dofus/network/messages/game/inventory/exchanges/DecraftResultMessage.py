from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.DecraftedItemStackInfo import DecraftedItemStackInfo


class DecraftResultMessage(NetworkMessage):
    protocolId = 7257
    results:DecraftedItemStackInfo
    
