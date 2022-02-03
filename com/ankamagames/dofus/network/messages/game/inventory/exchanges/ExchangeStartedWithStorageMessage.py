from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithStorageMessage(ExchangeStartedMessage):
    storageMaxSlot:int
    

    def init(self, storageMaxSlot:int, exchangeType:int):
        self.storageMaxSlot = storageMaxSlot
        
        super().__init__(exchangeType)
    
    