from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismsListRegisterMessage(NetworkMessage):
    listen:int
    

    def init(self, listen:int):
        self.listen = listen
        
        super().__init__()
    
    