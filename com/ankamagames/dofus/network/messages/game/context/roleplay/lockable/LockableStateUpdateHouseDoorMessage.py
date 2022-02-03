from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    

    def init(self, houseId:int, instanceId:int, secondHand:bool, locked:bool):
        self.houseId = houseId
        self.instanceId = instanceId
        self.secondHand = secondHand
        
        super().__init__(locked)
    
    