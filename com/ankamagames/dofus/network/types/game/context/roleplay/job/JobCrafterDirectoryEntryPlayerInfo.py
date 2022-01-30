from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class JobCrafterDirectoryEntryPlayerInfo(INetworkMessage):
    protocolId = 4905
    playerId:int
    playerName:str
    alignmentSide:int
    breed:int
    sex:bool
    isInWorkshop:bool
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    canCraftLegendary:bool
    status:PlayerStatus
    
    
