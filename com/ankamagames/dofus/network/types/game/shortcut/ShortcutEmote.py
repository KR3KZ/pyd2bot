from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutEmote(Shortcut):
    emoteId:int
    

    def init(self, emoteId:int, slot:int):
        self.emoteId = emoteId
        
        super().__init__(slot)
    
    