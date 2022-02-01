from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


class GuildHouseUpdateInformationMessage(NetworkMessage):
    housesInformations:HouseInformationsForGuild
    
    
