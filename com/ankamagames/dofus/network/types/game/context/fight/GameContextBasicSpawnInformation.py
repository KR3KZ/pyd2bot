from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations


class GameContextBasicSpawnInformation(NetworkMessage):
    protocolId = 2015
    teamId:int
    alive:bool
    informations:GameContextActorPositionInformations
    
    
