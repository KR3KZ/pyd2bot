from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class Version(INetworkMessage):
    protocolId = 3781
    major:int
    minor:int
    code:int
    build:int
    buildType:int
    
    
