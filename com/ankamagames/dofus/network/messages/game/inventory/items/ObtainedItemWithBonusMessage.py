from com.ankamagames.dofus.network.messages.game.inventory.items.ObtainedItemMessage import ObtainedItemMessage


class ObtainedItemWithBonusMessage(ObtainedItemMessage):
    protocolId = 7390
    bonusQuantity:int
    
    
