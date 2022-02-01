from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import CharacterSpellModification


class UpdateSpellModifierMessage(INetworkMessage):
    protocolId = 1672
    actorId:int
    spellModifier:CharacterSpellModification
    
    
