from com.ankamagames.dofus.network.types.game.data.items.ObjectItemMinimalInformation import ObjectItemMinimalInformation


class ObjectItemToSellInNpcShop(ObjectItemMinimalInformation):
    protocolId = 6097
    objectPrice:float
    buyCriterion:str
    
