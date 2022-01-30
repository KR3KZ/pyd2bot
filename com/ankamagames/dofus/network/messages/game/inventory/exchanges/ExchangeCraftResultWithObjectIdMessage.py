from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage


class ExchangeCraftResultWithObjectIdMessage(ExchangeCraftResultMessage):
    protocolId = 7556
    objectGenericId:int
    
