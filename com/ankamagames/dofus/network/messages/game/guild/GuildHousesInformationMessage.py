from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsForGuild import HouseInformationsForGuild


class GuildHousesInformationMessage(INetworkMessage):
    protocolId = 9308
    housesInformations:HouseInformationsForGuild
    
    
