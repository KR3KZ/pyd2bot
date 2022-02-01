from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagFurnituresRequestMessage(NetworkMessage):
    cellIds:list[int]
    funitureIds:list[int]
    orientations:list[int]
    
    
