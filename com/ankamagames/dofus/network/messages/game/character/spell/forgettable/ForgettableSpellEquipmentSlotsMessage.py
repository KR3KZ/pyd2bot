from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ForgettableSpellEquipmentSlotsMessage(NetworkMessage):
    protocolId = 7772
    quantity:int
    
    
