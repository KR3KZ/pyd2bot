from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightFighterLightInformations(NetworkMessage):
    protocolId = 6482
    id:int
    wave:int
    level:int
    breed:int
    
