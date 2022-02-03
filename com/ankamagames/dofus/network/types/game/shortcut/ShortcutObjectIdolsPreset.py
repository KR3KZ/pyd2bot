from com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject


class ShortcutObjectIdolsPreset(ShortcutObject):
    presetId:int
    

    def init(self, presetId:int, slot:int):
        self.presetId = presetId
        
        super().__init__(slot)
    
    