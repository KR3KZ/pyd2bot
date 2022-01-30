from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NpcDialogCreationMessage(INetworkMessage):
    protocolId = 5848
    mapId:int
    npcId:int
    
    
