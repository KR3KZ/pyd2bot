from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


class GuildHouseUpdateInformationMessage(INetworkMessage):
    protocolId = 6703
    housesInformations:HouseInformationsForGuild
    
    
