from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameServerInformations(NetworkMessage):
    protocolId = 5238
    id:int
    type:int
    status:int
    completion:int
    charactersCount:int
    charactersSlots:int
    date:int
    isMonoAccount:bool
    isSelectable:bool
    
    
