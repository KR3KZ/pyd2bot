from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


class GuildHouseUpdateInformationMessage(NetworkMessage):
    protocolId = 6703
    housesInformations:HouseInformationsForGuild
    
