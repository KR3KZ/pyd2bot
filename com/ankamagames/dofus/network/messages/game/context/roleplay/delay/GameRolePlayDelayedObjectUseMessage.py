from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionMessage import GameRolePlayDelayedActionMessage


class GameRolePlayDelayedObjectUseMessage(GameRolePlayDelayedActionMessage):
    objectGID:int
    

    def init(self, objectGID:int, delayedCharacterId:int, delayTypeId:int, delayEndTime:int):
        self.objectGID = objectGID
        
        super().__init__(delayedCharacterId, delayTypeId, delayEndTime)
    
    