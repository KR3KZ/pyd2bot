from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightFighterLightInformations(NetworkMessage):
    protocolId = 6482
    id:float
    wave:int
    level:int
    breed:int
    
