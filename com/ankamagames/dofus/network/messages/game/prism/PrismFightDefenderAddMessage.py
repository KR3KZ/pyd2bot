from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class PrismFightDefenderAddMessage(NetworkMessage):
    protocolId = 58
    subAreaId:int
    fightId:int
    defender:CharacterMinimalPlusLookInformations
    
    
