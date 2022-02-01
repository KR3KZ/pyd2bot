from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.job.DecraftedItemStackInfo import DecraftedItemStackInfo


class DecraftResultMessage(INetworkMessage):
    protocolId = 7257
    results:DecraftedItemStackInfo
    
    
