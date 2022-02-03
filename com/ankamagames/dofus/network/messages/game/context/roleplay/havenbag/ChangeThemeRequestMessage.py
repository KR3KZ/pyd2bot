from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChangeThemeRequestMessage(NetworkMessage):
    theme:int
    

    def init(self, theme:int):
        self.theme = theme
        
        super().__init__()
    
    