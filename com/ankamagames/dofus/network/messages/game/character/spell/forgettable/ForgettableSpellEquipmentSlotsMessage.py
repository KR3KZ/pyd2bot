from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ForgettableSpellEquipmentSlotsMessage(INetworkMessage):
    protocolId = 7772
    quantity:int
    
    
