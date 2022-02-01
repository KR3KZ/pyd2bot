from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightPlayersHelpersLeaveMessage(NetworkMessage):
    fightId:int
    playerId:int
    
    
