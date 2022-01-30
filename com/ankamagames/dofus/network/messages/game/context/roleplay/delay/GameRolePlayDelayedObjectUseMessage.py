from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionMessage import GameRolePlayDelayedActionMessage


class GameRolePlayDelayedObjectUseMessage(GameRolePlayDelayedActionMessage):
    protocolId = 1157
    objectGID:int
    
    
