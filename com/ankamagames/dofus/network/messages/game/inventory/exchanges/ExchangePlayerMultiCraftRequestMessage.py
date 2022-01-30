from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
    protocolId = 6947
    target:float
    skillId:int
    
