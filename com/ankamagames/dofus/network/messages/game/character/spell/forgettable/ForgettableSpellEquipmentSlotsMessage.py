from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellEquipmentSlotsMessage(NetworkMessage):
    quantity:int
    

    def init(self, quantity:int):
        self.quantity = quantity
        
        super().__init__()
    
    