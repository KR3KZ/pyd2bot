from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MonsterInGroupLightInformations(INetworkMessage):
    protocolId = 4246
    genericId:int
    grade:int
    level:int
    
    
