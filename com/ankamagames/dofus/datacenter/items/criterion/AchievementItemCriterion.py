                  
   class AchievementItemCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def isRespected(self) -> bool:
         id:int = 0
         achievementFinishedList:list = Kernel.getWorker().getFrame(QuestFrame)
         for id in achievementFinishedList:
            if id == _criterionValue:
               return True
         return False
      
      @property
      def text(self) -> str:
         readableValue = " \'" + Achievement.getAchievementById(_criterionValue).name + "\'"
         readableCriterion:str = I18n.getUiText("ui.tooltip.unlockAchievement",[readableValue])
         if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText("ui.tooltip.dontUnlockAchievement",[readableValue])
         return readableCriterion
      
      def clone(self) -> IItemCriterion:
         return AchievementItemCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         id:int = 0
         achievementFinishedList:list = Kernel.getWorker().getFrame(QuestFrame)
         for id in achievementFinishedList:
            if id == _criterionValue:
               return 1
         return 0
