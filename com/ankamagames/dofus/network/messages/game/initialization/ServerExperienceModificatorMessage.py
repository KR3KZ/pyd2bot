from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ServerExperienceModificatorMessage(INetworkMessage):
    protocolId = 7180
    experiencePercent:int
    
    
