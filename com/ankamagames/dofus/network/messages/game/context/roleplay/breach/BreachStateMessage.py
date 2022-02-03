from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
    


class BreachStateMessage(NetworkMessage):
    owner:'CharacterMinimalInformations'
    bonuses:list['ObjectEffectInteger']
    bugdet:int
    saved:bool
    

    def init(self, owner:'CharacterMinimalInformations', bonuses:list['ObjectEffectInteger'], bugdet:int, saved:bool):
        self.owner = owner
        self.bonuses = bonuses
        self.bugdet = bugdet
        self.saved = saved
        
        super().__init__()
    
    