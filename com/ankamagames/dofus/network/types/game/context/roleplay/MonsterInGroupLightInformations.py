from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MonsterInGroupLightInformations(NetworkMessage):
    protocolId = 4246
    genericId:int
    grade:int
    level:int
    
    
