from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


class UpdateMountCharacteristicsMessage(NetworkMessage):
    rideId:int
    boostToUpdateList:list[UpdateMountCharacteristic]
    
    
