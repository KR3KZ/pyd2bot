from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


class PrismFightAttackerAddMessage(INetworkMessage):
    protocolId = 3086
    subAreaId:int
    fightId:int
    attacker:CharacterMinimalPlusLookInformations
    
    
