from com.ankamagames.dofus.network.types.game.data.items.Item import Item


class SpellItem(Item):
    spellId:int
    spellLevel:int
    

    def init(self, spellId:int, spellLevel:int):
        self.spellId = spellId
        self.spellLevel = spellLevel
        
        super().__init__()
    
    