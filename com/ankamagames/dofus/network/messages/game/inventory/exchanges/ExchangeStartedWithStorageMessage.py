from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithStorageMessage(ExchangeStartedMessage):
    protocolId = 7302
    storageMaxSlot:int
    
    
