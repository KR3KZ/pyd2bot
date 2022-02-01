from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


class CharacterSelectedSuccessMessage(NetworkMessage):
    infos:CharacterBaseInformations
    isCollectingStats:bool
    
    
