from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkCraftMessage import ExchangeStartOkCraftMessage


class ExchangeStartOkCraftWithInformationMessage(ExchangeStartOkCraftMessage):
    skillId:int
    

    def init(self, skillId:int):
        self.skillId = skillId
        
        super().__init__()
    
    