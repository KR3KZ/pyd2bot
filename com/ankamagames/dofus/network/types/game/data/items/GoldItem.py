from com.ankamagames.dofus.network.types.game.data.items.Item import Item


class GoldItem(Item):
    sum:int
    

    def init(self, sum:int):
        self.sum = sum
        
        super().__init__()
    
    