from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ForgettableSpellEquipmentSlotsMessage(INetworkMessage):
    protocolId = 7772
    quantity:int
    
    
