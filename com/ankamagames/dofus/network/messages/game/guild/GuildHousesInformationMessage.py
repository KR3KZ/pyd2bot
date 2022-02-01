from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


class GuildHousesInformationMessage(NetworkMessage):
    housesInformations:list[HouseInformationsForGuild]
    
    
