from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class Version(NetworkMessage):
    major:int
    minor:int
    code:int
    build:int
    buildType:int
    

    def init(self, major:int, minor:int, code:int, build:int, buildType:int):
        self.major = major
        self.minor = minor
        self.code = code
        self.build = build
        self.buildType = buildType
        
        super().__init__()
    
    