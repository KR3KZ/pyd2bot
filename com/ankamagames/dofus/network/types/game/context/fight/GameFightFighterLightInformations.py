from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightFighterLightInformations(NetworkMessage):
    id:int
    wave:int
    level:int
    breed:int
    sex:bool
    alive:bool
    
    
