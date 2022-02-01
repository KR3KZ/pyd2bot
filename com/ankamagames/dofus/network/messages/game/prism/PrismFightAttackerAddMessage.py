from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class PrismFightAttackerAddMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    attacker:CharacterMinimalPlusLookInformations
    
    
