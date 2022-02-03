from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableShowCodeDialogMessage(NetworkMessage):
    changeOrUse:bool
    codeSize:int
    

    def init(self, changeOrUse:bool, codeSize:int):
        self.changeOrUse = changeOrUse
        self.codeSize = codeSize
        
        super().__init__()
    
    