from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
    target:int
    skillId:int
    

    def init(self, target:int, skillId:int, exchangeType:int):
        self.target = target
        self.skillId = skillId
        
        super().__init__(exchangeType)
    
    