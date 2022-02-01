from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations


class GameContextBasicSpawnInformation(INetworkMessage):
    protocolId = 2015
    teamId:int
    alive:bool
    informations:GameContextActorPositionInformations
    
    
