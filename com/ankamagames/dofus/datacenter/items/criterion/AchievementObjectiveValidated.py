               
   class AchievementObjectiveValidated(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         achievementObjective:AchievementObjective = AchievementObjective.getAchievementObjectiveById(_criterionValue)
         return I18n.getUiText("ui.achievement.objectiveValidated",[achievementObjective.name,Achievement.getAchievementById(achievementObjective.achievementId).name])
      
      def clone(self) -> IItemCriterion:
         return AchievementObjectiveValidated(self.basicText)
