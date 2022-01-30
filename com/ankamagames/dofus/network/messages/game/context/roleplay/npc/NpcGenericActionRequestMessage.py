from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NpcGenericActionRequestMessage(NetworkMessage):
    protocolId = 1598
    npcId:int
    npcActionId:int
    npcMapId:int
    
    
