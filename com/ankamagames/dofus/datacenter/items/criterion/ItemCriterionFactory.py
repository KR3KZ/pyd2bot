from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import IItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.UnusableItemCriterion import UnusableItemCriterion
logger = Logger(__name__)        


class ItemCriterionFactory:
   def __init__(self):
      super().__init__()
   
   def create(self, pServerCriterionForm:str) -> IItemCriterion:
      criterion = None
      s:str = pServerCriterionForm[0:2]
      if s == "BI":
         criterion = UnusableItemCriterion(pServerCriterionForm)
      elif s == "Ca":
         pass 
      elif s == "CA":
         pass 
      elif s == "ca":
         pass 
      elif s == "Cc":
         pass 
      elif s == "CC":
         pass 
      elif s == "cc":
         pass 
      elif s == "CD":
         pass 
      elif s == "Ce":
         pass 
      elif s == "CE":
         pass 
      elif s == "CH":
         pass 
      elif s == "Ci":
         pass 
      elif s == "CI":
         pass 
      elif s == "ci":
         pass 
      elif s == "CL":
         pass 
      elif s == "CM":
         pass 
      elif s == "CP":
         pass 
      elif s == "Cs":
         pass 
      elif s == "CS":
         pass 
      elif s == "cs":
         pass 
      elif s == "Ct":
         pass 
      elif s == "CT":
         pass 
      elif s == "Cv":
         pass 
      elif s == "CV":
         pass 
      elif s == "cv":
         pass 
      elif s == "Cw":
         pass 
      elif s == "CW":
         pass 
      elif s == "cw":
         pass 
         criterion = ItemCriterion(pServerCriterionForm)
         
      elif s == "EA":
         pass 
         criterion = MonsterGroupChallengeCriterion(pServerCriterionForm)
         
      elif s == "EB":
         pass 
         criterion = floatOfMountBirthedCriterion(pServerCriterionForm)
         
      elif s == "Ec":
         pass 
         criterion = floatOfItemMadeCriterion(pServerCriterionForm)
         
      elif s == "Eu":
         pass 
         criterion = RuneByingItemCriterion(pServerCriterionForm)
         
      elif s == "Kd":
         pass 
         criterion = ArenaDuelRankCriterion(pServerCriterionForm)
         
      elif s == "KD":
         pass 
         criterion = ArenaMaxDuelRankCriterion(pServerCriterionForm)
         
      elif s == "Ks":
         pass 
         criterion = ArenaSoloRankCriterion(pServerCriterionForm)
         
      elif s == "KS":
         pass 
         criterion = ArenaMaxSoloRankCriterion(pServerCriterionForm)
         
      elif s == "Kt":
         pass 
         criterion = ArenaTeamRankCriterion(pServerCriterionForm)
         
      elif s == "KT":
         pass 
         criterion = ArenaMaxTeamRankCriterion(pServerCriterionForm)
         
      elif s == "MK":
         pass 
         criterion = MapCharactersItemCriterion(pServerCriterionForm)
         
      elif s == "Oa":
         pass 
         criterion = AchievementPointsItemCriterion(pServerCriterionForm)
         
      elif s == "OA":
         pass 
         criterion = AchievementItemCriterion(pServerCriterionForm)
         
      elif s == "Ob":
         pass 
         criterion = AchievementAccountItemCriterion(pServerCriterionForm)
         
      elif s == "Of":
         pass 
         criterion = MountFamilyItemCriterion(pServerCriterionForm)
         
      elif s == "OH":
         pass 
         criterion = NewHavenbagItemCriterion(pServerCriterionForm)
         
      elif s == "OO":
         pass 
         criterion = AchievementObjectiveValidated(pServerCriterionForm)
         
      elif s == "Os":
         pass 
         criterion = SmileyPackItemCriterion(pServerCriterionForm)
         
      elif s == "OV":
         pass 
         criterion = SubscriptionDurationItemCriterion(pServerCriterionForm)
         
      elif s == "Ow":
         pass 
         criterion = AllianceItemCriterion(pServerCriterionForm)
         
      elif s == "Ox":
         pass 
         criterion = AllianceRightsItemCriterion(pServerCriterionForm)
         
      elif s == "Oz":
         pass 
         criterion = AllianceAvAItemCriterion(pServerCriterionForm)
         
      elif s == "Pa":
         pass 
         criterion = AlignmentLevelItemCriterion(pServerCriterionForm)
         
      elif s == "PA":
         pass 
         criterion = SoulStoneItemCriterion(pServerCriterionForm)
         
      elif s == "Pb":
         pass 
         criterion = FriendlistItemCriterion(pServerCriterionForm)
         
      elif s == "PB":
         pass 
         criterion = SubareaItemCriterion(pServerCriterionForm)
         
      elif s == "Pe":
         pass 
         criterion = PremiumAccountItemCriterion(pServerCriterionForm)
         
      elif s == "PE":
         pass 
         criterion = EmoteItemCriterion(pServerCriterionForm)
         
      elif s == "Pf":
         pass 
         criterion = RideItemCriterion(pServerCriterionForm)
         
      elif s == "Pg":
         pass 
         criterion = GiftItemCriterion(pServerCriterionForm)
         
      elif s == "PG":
         pass 
         criterion = BreedItemCriterion(pServerCriterionForm)
         
      elif s == "Pi":
         pass 
      elif s == "PI":
         pass 
         criterion = SkillItemCriterion(pServerCriterionForm)
         
      elif s == "PJ":
         pass 
      elif s == "Pj":
         pass 
         criterion = JobItemCriterion(pServerCriterionForm)
         
      elif s == "Pk":
         pass 
         criterion = BonusSetItemCriterion(pServerCriterionForm)
         
      elif s == "PK":
         pass 
         criterion = KamaItemCriterion(pServerCriterionForm)
         
      elif s == "PL":
         pass 
         criterion = LevelItemCriterion(pServerCriterionForm)
         
      elif s == "Pl":
         pass 
         criterion = PrestigeLevelItemCriterion(pServerCriterionForm)
         
      elif s == "Pm":
         pass 
         criterion = MapItemCriterion(pServerCriterionForm)
         
      elif s == "PN":
         pass 
         criterion = NameItemCriterion(pServerCriterionForm)
         
      elif s == "PO":
         pass 
         criterion = ObjectItemCriterion(pServerCriterionForm)
         
      elif s == "Po":
         pass 
         criterion = AreaItemCriterion(pServerCriterionForm)
         
      elif s == "Pp":
         pass 
      elif s == "PP":
         pass 
         criterion = PVPRankItemCriterion(pServerCriterionForm)
         
      elif s == "Pr":
         pass 
         criterion = SpecializationItemCriterion(pServerCriterionForm)
         
      elif s == "PR":
         pass 
         criterion = MariedItemCriterion(pServerCriterionForm)
         
      elif s == "Ps":
         pass 
         criterion = AlignmentItemCriterion(pServerCriterionForm)
         
      elif s == "PS":
         pass 
         criterion = SexItemCriterion(pServerCriterionForm)
         
      elif s == "PT":
         pass 
         criterion = SpellItemCriterion(pServerCriterionForm)
         
      elif s == "PU":
         pass 
         criterion = BonesItemCriterion(pServerCriterionForm)
         
      elif s == "Pw":
         pass 
         criterion = GuildItemCriterion(pServerCriterionForm)
         
      elif s == "PW":
         pass 
         criterion = WeightItemCriterion(pServerCriterionForm)
         
      elif s == "Px":
         pass 
         criterion = GuildRightsItemCriterion(pServerCriterionForm)
         
      elif s == "PX":
         pass 
         criterion = AccountRightsItemCriterion(pServerCriterionForm)
         
      elif s == "Py":
         pass 
         criterion = GuildLevelItemCriterion(pServerCriterionForm)
         
      elif s == "Pz":
         pass 
         
      elif s == "PZ":
         pass 
         criterion = SubscribeItemCriterion(pServerCriterionForm)
         
      elif s == "Qa":
         pass 
      elif s == "Qc":
         pass 
      elif s == "Qf":
         pass 
         criterion = QuestItemCriterion(pServerCriterionForm)
         
      elif s == "Qo":
         pass 
         criterion = QuestObjectiveItemCriterion(pServerCriterionForm)
         
      elif s == "SC":
         pass 
         criterion = ServerTypeItemCriterion(pServerCriterionForm)
         
      elif s == "Sc":
         pass 
         criterion = StaticCriterionItemCriterion(pServerCriterionForm)
         
      elif s == "Sd":
         pass 
         criterion = DayItemCriterion(pServerCriterionForm)
         
      elif s == "SG":
         pass 
         criterion = MonthItemCriterion(pServerCriterionForm)
         
      elif s == "SI":
         pass 
         criterion = ServerItemCriterion(pServerCriterionForm)
         
      elif s == "ST":
         pass 
         criterion = ServerSeasonTemporisCriterion(pServerCriterionForm)
         
      elif s == "Sy":
         pass 
         criterion = CommunityItemCriterion(pServerCriterionForm)
         
      else:
         logger.warn("Criterion \'" + s + "\' unknow or unused (" + pServerCriterionForm + ")")

      return criterion
