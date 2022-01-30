from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class GuildFightPlayersEnemiesListMessage(NetworkMessage):
    protocolId = 9360
    fightId:float
    playerInfo:list[CharacterMinimalPlusLookInformations]
    
