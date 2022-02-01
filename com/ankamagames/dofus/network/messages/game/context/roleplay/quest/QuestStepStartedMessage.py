from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestStepStartedMessage(NetworkMessage):
    questId:int
    stepId:int
    
    
