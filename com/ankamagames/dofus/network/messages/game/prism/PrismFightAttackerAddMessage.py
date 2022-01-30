from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class PrismFightAttackerAddMessage(NetworkMessage):
    protocolId = 3086
    subAreaId:int
    fightId:int
    attacker:CharacterMinimalPlusLookInformations
    
    
