from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HouseSellRequestMessage import HouseSellRequestMessage


class HouseSellFromInsideRequestMessage(HouseSellRequestMessage):
    

    def init(self, instanceId:int, amount:int, forSale:bool):
        
        super().__init__(instanceId, amount, forSale)
    
    