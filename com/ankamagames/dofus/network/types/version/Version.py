from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class Version(NetworkMessage):
    major:int
    minor:int
    code:int
    build:int
    buildType:int
    
    
