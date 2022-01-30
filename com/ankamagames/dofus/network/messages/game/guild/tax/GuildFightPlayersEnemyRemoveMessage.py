from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildFightPlayersEnemyRemoveMessage(NetworkMessage):
    protocolId = 4301
    fightId:int
    playerId:int
    
