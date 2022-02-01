from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.HavenBagFurnitureInformation import HavenBagFurnitureInformation


class HavenBagFurnituresMessage(INetworkMessage):
    protocolId = 6373
    furnituresInfos:HavenBagFurnitureInformation
    
    
