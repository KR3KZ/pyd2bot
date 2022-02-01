from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.HavenBagFurnitureInformation import HavenBagFurnitureInformation


class HavenBagFurnituresMessage(NetworkMessage):
    furnituresInfos:list[HavenBagFurnitureInformation]
    
    
