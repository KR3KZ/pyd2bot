from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


class CharacterSelectedSuccessMessage(NetworkMessage):
    protocolId = 9833
    infos:CharacterBaseInformations
    isCollectingStats:bool
    
