from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifePointsLostMessage import GameActionFightLifePointsLostMessage


class GameActionFightLifeAndShieldPointsLostMessage(GameActionFightLifePointsLostMessage):
    shieldLoss:int
    
    
