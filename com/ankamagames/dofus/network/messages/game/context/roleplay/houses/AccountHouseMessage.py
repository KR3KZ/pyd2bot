from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.AccountHouseInformations import AccountHouseInformations


class AccountHouseMessage(NetworkMessage):
    protocolId = 7236
    houses:list[AccountHouseInformations]
    
