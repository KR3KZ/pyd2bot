from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutSmiley(Shortcut):
    smileyId:int
    

    def init(self, smileyId:int, slot:int):
        self.smileyId = smileyId
        
        super().__init__(slot)
    
    