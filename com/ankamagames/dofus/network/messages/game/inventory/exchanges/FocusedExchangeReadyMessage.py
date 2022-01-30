from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeReadyMessage import ExchangeReadyMessage


class FocusedExchangeReadyMessage(ExchangeReadyMessage):
    protocolId = 2904
    focusActionId:int
    
    
