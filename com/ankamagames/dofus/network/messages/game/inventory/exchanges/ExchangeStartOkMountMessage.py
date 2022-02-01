from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMountWithOutPaddockMessage import ExchangeStartOkMountWithOutPaddockMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeStartOkMountMessage(ExchangeStartOkMountWithOutPaddockMessage):
    paddockedMountsDescription:list[MountClientData]
    
    
