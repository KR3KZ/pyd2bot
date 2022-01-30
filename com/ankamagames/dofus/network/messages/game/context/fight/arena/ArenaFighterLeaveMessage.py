from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations


class ArenaFighterLeaveMessage(NetworkMessage):
    protocolId = 1880
    leaver:CharacterBasicMinimalInformations
    
