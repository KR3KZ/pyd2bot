from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class GuildFightPlayersEnemiesListMessage(INetworkMessage):
    protocolId = 9360
    fightId:int
    playerInfo:CharacterMinimalPlusLookInformations
    
    
