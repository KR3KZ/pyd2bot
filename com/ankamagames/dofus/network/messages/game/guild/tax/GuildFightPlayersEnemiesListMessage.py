from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class GuildFightPlayersEnemiesListMessage(INetworkMessage):
    protocolId = 9360
    fightId:int
    playerInfo:CharacterMinimalPlusLookInformations
    
    
