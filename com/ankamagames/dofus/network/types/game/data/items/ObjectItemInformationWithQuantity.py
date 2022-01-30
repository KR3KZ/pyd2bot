from com.ankamagames.dofus.network.types.game.data.items.ObjectItemMinimalInformation import ObjectItemMinimalInformation


class ObjectItemInformationWithQuantity(ObjectItemMinimalInformation):
    protocolId = 4715
    quantity:int
    
    
