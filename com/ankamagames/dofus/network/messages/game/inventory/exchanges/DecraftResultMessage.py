from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.DecraftedItemStackInfo import DecraftedItemStackInfo


class DecraftResultMessage(NetworkMessage):
    results:list[DecraftedItemStackInfo]
    
    
