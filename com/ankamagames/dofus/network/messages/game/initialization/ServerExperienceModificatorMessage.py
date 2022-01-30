from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ServerExperienceModificatorMessage(NetworkMessage):
    protocolId = 7180
    experiencePercent:int
    
