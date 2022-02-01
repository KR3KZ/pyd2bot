from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarRemoveRequestMessage(NetworkMessage):
    barType:int
    slot:int
    
    
