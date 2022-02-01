from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NpcGenericActionRequestMessage(INetworkMessage):
    protocolId = 1598
    npcId:int
    npcActionId:int
    npcMapId:int
    
    
