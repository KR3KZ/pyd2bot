            
class QuestObjectiveItemCriterion(ItemCriterion, IDataCenter):
      
   
   _objId:int
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
      self._objId = _criterionValue
   
   @property
   def text(self) -> str:
      return ""
   
   @property
   def isRespected(self) -> bool:
      obj:QuestObjective = QuestObjective.getQuestObjectiveById(self._objId)
      if not obj:
         return False
      questFrame:QuestFrame =Kernel().getWorker().getFrame(QuestFrame)
      activeObjs:list[int] = questFrame.getActiveObjectives()
      completedObjs:list[int] = questFrame.getCompletedObjectives()
      s:str = _serverCriterionForm.slice(0,2)
      switch(s)
         case "Qo":
            if _operator.text == ItemCriterionOperator.EQUAL:
               return activeObjs.index(self._objId) != -1
            if _operator.text == ItemCriterionOperator.DIFFERENT:
               return activeObjs.index(self._objId) == -1
            if _operator.text == ItemCriterionOperator.INFERIOR:
               return completedObjs.index(self._objId) == -1
            if _operator.text == ItemCriterionOperator.SUPERIOR:
               return completedObjs.index(self._objId) != -1
            break
      return False
   
   def clone(self) -> IItemCriterion:
      return QuestObjectiveItemCriterion(self.basicText)
