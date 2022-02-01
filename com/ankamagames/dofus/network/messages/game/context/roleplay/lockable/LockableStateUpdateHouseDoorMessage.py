from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
    houseId:int
    instanceId:int
    secondHand:bool
    
    
