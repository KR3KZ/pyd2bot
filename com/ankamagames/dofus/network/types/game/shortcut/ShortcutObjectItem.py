from com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject


class ShortcutObjectItem(ShortcutObject):
    itemUID:int
    itemGID:int
    

    def init(self, itemUID:int, itemGID:int, slot:int):
        self.itemUID = itemUID
        self.itemGID = itemGID
        
        super().__init__(slot)
    
    