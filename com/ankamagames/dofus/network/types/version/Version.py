from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class Version(NetworkMessage):
    protocolId = 3781
    major:int
    minor:int
    code:int
    build:int
    buildType:int
    
    
