from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MonsterInGroupLightInformations(INetworkMessage):
    protocolId = 4246
    genericId:int
    grade:int
    level:int
    
    
