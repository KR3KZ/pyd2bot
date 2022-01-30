from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
    protocolId = 6947
    target:int
    skillId:int
    
    
