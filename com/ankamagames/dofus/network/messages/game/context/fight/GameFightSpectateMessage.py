from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


class GameFightSpectateMessage(NetworkMessage):
    protocolId = 8991
    effects:FightDispellableEffectExtendedInformations
    marks:GameActionMark
    gameTurn:int
    fightStart:int
    idols:Idol
    fxTriggerCounts:GameFightEffectTriggerCount
    
    
