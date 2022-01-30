from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateHouseDoorMessage(LockableStateUpdateAbstractMessage):
    protocolId = 7958
    houseId:int
    instanceId:int
    secondHand:bool
    
