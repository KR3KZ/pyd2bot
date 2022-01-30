from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.house.AccountHouseInformations import AccountHouseInformations


class AccountHouseMessage(INetworkMessage):
    protocolId = 7236
    houses:AccountHouseInformations
    
    
