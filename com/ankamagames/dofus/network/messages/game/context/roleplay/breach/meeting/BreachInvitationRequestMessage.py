from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachInvitationRequestMessage(NetworkMessage):
    guests:list[int]
    

    def init(self, guests:list[int]):
        self.guests = guests
        
        super().__init__()
    
    