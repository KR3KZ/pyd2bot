from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountHarnessColorsUpdateRequestMessage(NetworkMessage):
    protocolId = 7947
    useHarnessColors:bool
    
