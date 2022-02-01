from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NpcDialogCreationMessage(INetworkMessage):
    protocolId = 5848
    mapId:int
    npcId:int
    
    
