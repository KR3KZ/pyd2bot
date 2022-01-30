from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


class GuildHousesInformationMessage(NetworkMessage):
    protocolId = 9308
    housesInformations:list[HouseInformationsForGuild]
    
