from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class GuildFightPlayersHelpersJoinMessage(NetworkMessage):
    protocolId = 4751
    fightId:int
    playerInfo:CharacterMinimalPlusLookInformations
    
