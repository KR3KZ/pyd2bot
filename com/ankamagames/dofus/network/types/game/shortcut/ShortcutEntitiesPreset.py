from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


class ShortcutEntitiesPreset(Shortcut):
    presetId:int
    

    def init(self, presetId:int, slot:int):
        self.presetId = presetId
        
        super().__init__(slot)
    
    