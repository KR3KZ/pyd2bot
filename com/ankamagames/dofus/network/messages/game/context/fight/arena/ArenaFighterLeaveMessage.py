from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations


class ArenaFighterLeaveMessage(NetworkMessage):
    leaver:CharacterBasicMinimalInformations
    
    
