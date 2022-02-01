from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRenameRequestMessage(NetworkMessage):
    name:str
    mountId:int
    
    
