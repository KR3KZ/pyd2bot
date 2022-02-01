from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcGenericActionRequestMessage(NetworkMessage):
    npcId:int
    npcActionId:int
    npcMapId:int
    
    
