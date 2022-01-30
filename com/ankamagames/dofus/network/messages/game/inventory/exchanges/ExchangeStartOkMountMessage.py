from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMountWithOutPaddockMessage import ExchangeStartOkMountWithOutPaddockMessage
from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData


class ExchangeStartOkMountMessage(ExchangeStartOkMountWithOutPaddockMessage):
    protocolId = 9690
    paddockedMountsDescription:MountClientData
    
