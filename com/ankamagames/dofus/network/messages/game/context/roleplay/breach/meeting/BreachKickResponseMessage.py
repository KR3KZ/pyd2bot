from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


class BreachKickResponseMessage(INetworkMessage):
    protocolId = 5114
    target:CharacterMinimalInformations
    kicked:bool
    
    
