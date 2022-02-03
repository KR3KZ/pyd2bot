from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
    mapId:int
    elementId:int
    

    def init(self, mapId:int, elementId:int, locked:bool):
        self.mapId = mapId
        self.elementId = elementId
        
        super().__init__(locked)
    
    