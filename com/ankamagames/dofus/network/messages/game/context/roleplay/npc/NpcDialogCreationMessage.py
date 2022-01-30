from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NpcDialogCreationMessage(NetworkMessage):
    protocolId = 5848
    mapId:int
    npcId:int
    
