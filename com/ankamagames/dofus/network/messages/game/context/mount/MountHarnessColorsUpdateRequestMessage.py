from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountHarnessColorsUpdateRequestMessage(NetworkMessage):
    useHarnessColors:bool
    

    def init(self, useHarnessColors:bool):
        self.useHarnessColors = useHarnessColors
        
        super().__init__()
    
    