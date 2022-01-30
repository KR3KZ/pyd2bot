from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightFighterLightInformations(INetworkMessage):
    protocolId = 6482
    id:int
    wave:int
    level:int
    breed:int
    sex:bool
    alive:bool
    
    
