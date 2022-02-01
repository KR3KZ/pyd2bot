from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class PrismFightDefenderAddMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    defender:CharacterMinimalPlusLookInformations
    
    
