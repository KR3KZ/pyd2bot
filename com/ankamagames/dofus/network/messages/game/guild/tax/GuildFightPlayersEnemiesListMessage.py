from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class GuildFightPlayersEnemiesListMessage(NetworkMessage):
    fightId:int
    playerInfo:list[CharacterMinimalPlusLookInformations]
    
    
