from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem


class ForgettableSpellItem(SpellItem):
    available:bool
    

    def init(self, available:bool, spellId:int, spellLevel:int):
        self.available = available
        
        super().__init__(spellId, spellLevel)
    
    