from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
    target:int
    skillId:int
    
    
