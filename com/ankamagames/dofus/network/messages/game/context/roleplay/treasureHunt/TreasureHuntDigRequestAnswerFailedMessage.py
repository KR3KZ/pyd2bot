from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntDigRequestAnswerMessage import TreasureHuntDigRequestAnswerMessage


class TreasureHuntDigRequestAnswerFailedMessage(TreasureHuntDigRequestAnswerMessage):
    protocolId = 862
    wrongFlagCount:int
    
