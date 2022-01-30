from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.HavenBagFurnitureInformation import HavenBagFurnitureInformation


class HavenBagFurnituresMessage(NetworkMessage):
    protocolId = 6373
    furnituresInfos:HavenBagFurnitureInformation
    
