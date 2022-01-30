from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkCraftMessage import ExchangeStartOkCraftMessage


class ExchangeStartOkCraftWithInformationMessage(ExchangeStartOkCraftMessage):
    protocolId = 9154
    skillId:int
    
    
