from com.ankamagames.dofus.network.messages.game.context.roleplay.GameRolePlayShowActorMessage import GameRolePlayShowActorMessage


class GameRolePlayShowActorWithEventMessage(GameRolePlayShowActorMessage):
    protocolId = 2684
    actorEventId:int
    
    
