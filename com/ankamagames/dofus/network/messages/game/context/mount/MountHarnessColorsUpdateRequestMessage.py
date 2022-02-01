from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountHarnessColorsUpdateRequestMessage(INetworkMessage):
    protocolId = 7947
    useHarnessColors:bool
    
    
