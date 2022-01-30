from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


class CharacterSelectedSuccessMessage(INetworkMessage):
    protocolId = 9833
    infos:CharacterBaseInformations
    isCollectingStats:bool
    
    
