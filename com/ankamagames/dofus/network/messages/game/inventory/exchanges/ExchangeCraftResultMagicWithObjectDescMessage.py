from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultWithObjectDescMessage import ExchangeCraftResultWithObjectDescMessage


class ExchangeCraftResultMagicWithObjectDescMessage(ExchangeCraftResultWithObjectDescMessage):
    protocolId = 6242
    magicPoolStatus:int
    
