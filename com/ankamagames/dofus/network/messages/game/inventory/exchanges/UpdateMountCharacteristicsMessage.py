from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


class UpdateMountCharacteristicsMessage(NetworkMessage):
    protocolId = 9937
    rideId:int
    boostToUpdateList:list[UpdateMountCharacteristic]
    
