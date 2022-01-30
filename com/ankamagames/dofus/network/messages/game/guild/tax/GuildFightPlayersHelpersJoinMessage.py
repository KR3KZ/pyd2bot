from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class GuildFightPlayersHelpersJoinMessage(INetworkMessage):
    protocolId = 4751
    fightId:int
    playerInfo:CharacterMinimalPlusLookInformations
    
    
