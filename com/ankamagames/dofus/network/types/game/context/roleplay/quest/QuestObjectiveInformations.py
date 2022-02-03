from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestObjectiveInformations(NetworkMessage):
    objectiveId:int
    objectiveStatus:bool
    dialogParams:list[str]
    

    def init(self, objectiveId:int, objectiveStatus:bool, dialogParams:list[str]):
        self.objectiveId = objectiveId
        self.objectiveStatus = objectiveStatus
        self.dialogParams = dialogParams
        
        super().__init__()
    
    