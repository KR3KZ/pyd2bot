from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameServerInformations(NetworkMessage):
    id:int
    type:int
    status:int
    completion:int
    charactersCount:int
    charactersSlots:int
    date:int
    isMonoAccount:bool
    isSelectable:bool
    
    
