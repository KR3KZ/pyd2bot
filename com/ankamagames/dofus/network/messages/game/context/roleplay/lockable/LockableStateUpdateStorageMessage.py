from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage


class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
    protocolId = 5127
    mapId:int
    elementId:int
    
