from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ServerExperienceModificatorMessage(INetworkMessage):
    protocolId = 7180
    experiencePercent:int
    
    
