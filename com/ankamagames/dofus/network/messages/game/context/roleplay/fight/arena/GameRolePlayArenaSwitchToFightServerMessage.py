from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToFightServerMessage(NetworkMessage):
    protocolId = 3316
    address:str
    ports:list[int]
    ticket:list[int]
    
