from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutSpell(Shortcut):
    spellId:int
    

    def init(self, spellId:int, slot:int):
        self.spellId = spellId
        
        super().__init__(slot)
    
    