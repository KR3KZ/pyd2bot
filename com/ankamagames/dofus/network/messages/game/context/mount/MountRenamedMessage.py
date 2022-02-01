from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRenamedMessage(NetworkMessage):
    mountId:int
    name:str
    
    
