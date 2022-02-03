from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PauseDialogMessage(NetworkMessage):
    dialogType:int
    

    def init(self, dialogType:int):
        self.dialogType = dialogType
        
        super().__init__()
    
    