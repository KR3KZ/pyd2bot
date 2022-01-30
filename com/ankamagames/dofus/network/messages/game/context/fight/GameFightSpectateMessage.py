from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


class GameFightSpectateMessage(INetworkMessage):
    protocolId = 8991
    effects:FightDispellableEffectExtendedInformations
    marks:GameActionMark
    gameTurn:int
    fightStart:int
    idols:Idol
    fxTriggerCounts:GameFightEffectTriggerCount
    
    
