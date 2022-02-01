from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class GuildFightPlayersHelpersJoinMessage(NetworkMessage):
    fightId:int
    playerInfo:CharacterMinimalPlusLookInformations
    
    
