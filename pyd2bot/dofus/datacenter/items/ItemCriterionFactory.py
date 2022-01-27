               
   class ItemCriterionFactory(IDataCenter):
      
      logger = logging.getLogger("bot")
       
      
      def __init__(self):
         super().__init__()
      
      def create(self, pServerCriterionForm:str) -> ItemCriterion:
         criterion:ItemCriterion = None
         s:str = pServerCriterionForm.slice(0,2)
         switch(s)
            case "BI":
               criterion = UnusableItemCriterion(pServerCriterionForm)
               break
            case "Ca":
            case "CA":
            case "ca":
            case "Cc":
            case "CC":
            case "cc":
            case "CD":
            case "Ce":
            case "CE":
            case "CH":
            case "Ci":
            case "CI":
            case "ci":
            case "CL":
            case "CM":
            case "CP":
            case "Cs":
            case "CS":
            case "cs":
            case "Ct":
            case "CT":
            case "Cv":
            case "CV":
            case "cv":
            case "Cw":
            case "CW":
            case "cw":
               criterion = ItemCriterion(pServerCriterionForm)
               break
            case "EA":
               criterion = MonsterGroupChallengeCriterion(pServerCriterionForm)
               break
            case "EB":
               criterion = floatOfMountBirthedCriterion(pServerCriterionForm)
               break
            case "Ec":
               criterion = floatOfItemMadeCriterion(pServerCriterionForm)
               break
            case "Eu":
               criterion = RuneByBreakingItemCriterion(pServerCriterionForm)
               break
            case "Kd":
               criterion = ArenaDuelRankCriterion(pServerCriterionForm)
               break
            case "KD":
               criterion = ArenaMaxDuelRankCriterion(pServerCriterionForm)
               break
            case "Ks":
               criterion = ArenaSoloRankCriterion(pServerCriterionForm)
               break
            case "KS":
               criterion = ArenaMaxSoloRankCriterion(pServerCriterionForm)
               break
            case "Kt":
               criterion = ArenaTeamRankCriterion(pServerCriterionForm)
               break
            case "KT":
               criterion = ArenaMaxTeamRankCriterion(pServerCriterionForm)
               break
            case "MK":
               criterion = MapCharactersItemCriterion(pServerCriterionForm)
               break
            case "Oa":
               criterion = AchievementPointsItemCriterion(pServerCriterionForm)
               break
            case "OA":
               criterion = AchievementItemCriterion(pServerCriterionForm)
               break
            case "Ob":
               criterion = AchievementAccountItemCriterion(pServerCriterionForm)
               break
            case "Of":
               criterion = MountFamilyItemCriterion(pServerCriterionForm)
               break
            case "OH":
               criterion = NewHavenbagItemCriterion(pServerCriterionForm)
               break
            case "OO":
               criterion = AchievementObjectiveValidated(pServerCriterionForm)
               break
            case "Os":
               criterion = SmileyPackItemCriterion(pServerCriterionForm)
               break
            case "OV":
               criterion = SubscriptionDurationItemCriterion(pServerCriterionForm)
               break
            case "Ow":
               criterion = AllianceItemCriterion(pServerCriterionForm)
               break
            case "Ox":
               criterion = AllianceRightsItemCriterion(pServerCriterionForm)
               break
            case "Oz":
               criterion = AllianceAvAItemCriterion(pServerCriterionForm)
               break
            case "Pa":
               criterion = AlignmentLevelItemCriterion(pServerCriterionForm)
               break
            case "PA":
               criterion = SoulStoneItemCriterion(pServerCriterionForm)
               break
            case "Pb":
               criterion = FriendlistItemCriterion(pServerCriterionForm)
               break
            case "PB":
               criterion = SubareaItemCriterion(pServerCriterionForm)
               break
            case "Pe":
               criterion = PremiumAccountItemCriterion(pServerCriterionForm)
               break
            case "PE":
               criterion = EmoteItemCriterion(pServerCriterionForm)
               break
            case "Pf":
               criterion = RideItemCriterion(pServerCriterionForm)
               break
            case "Pg":
               criterion = GiftItemCriterion(pServerCriterionForm)
               break
            case "PG":
               criterion = BreedItemCriterion(pServerCriterionForm)
               break
            case "Pi":
            case "PI":
               criterion = SkillItemCriterion(pServerCriterionForm)
               break
            case "PJ":
            case "Pj":
               criterion = JobItemCriterion(pServerCriterionForm)
               break
            case "Pk":
               criterion = BonusSetItemCriterion(pServerCriterionForm)
               break
            case "PK":
               criterion = KamaItemCriterion(pServerCriterionForm)
               break
            case "PL":
               criterion = LevelItemCriterion(pServerCriterionForm)
               break
            case "Pl":
               criterion = PrestigeLevelItemCriterion(pServerCriterionForm)
               break
            case "Pm":
               criterion = MapItemCriterion(pServerCriterionForm)
               break
            case "PN":
               criterion = NameItemCriterion(pServerCriterionForm)
               break
            case "PO":
               criterion = ObjectItemCriterion(pServerCriterionForm)
               break
            case "Po":
               criterion = AreaItemCriterion(pServerCriterionForm)
               break
            case "Pp":
            case "PP":
               criterion = PVPRankItemCriterion(pServerCriterionForm)
               break
            case "Pr":
               criterion = SpecializationItemCriterion(pServerCriterionForm)
               break
            case "PR":
               criterion = MariedItemCriterion(pServerCriterionForm)
               break
            case "Ps":
               criterion = AlignmentItemCriterion(pServerCriterionForm)
               break
            case "PS":
               criterion = SexItemCriterion(pServerCriterionForm)
               break
            case "PT":
               criterion = SpellItemCriterion(pServerCriterionForm)
               break
            case "PU":
               criterion = BonesItemCriterion(pServerCriterionForm)
               break
            case "Pw":
               criterion = GuildItemCriterion(pServerCriterionForm)
               break
            case "PW":
               criterion = WeightItemCriterion(pServerCriterionForm)
               break
            case "Px":
               criterion = GuildRightsItemCriterion(pServerCriterionForm)
               break
            case "PX":
               criterion = AccountRightsItemCriterion(pServerCriterionForm)
               break
            case "Py":
               criterion = GuildLevelItemCriterion(pServerCriterionForm)
               break
            case "Pz":
               break
            case "PZ":
               criterion = SubscribeItemCriterion(pServerCriterionForm)
               break
            case "Qa":
            case "Qc":
            case "Qf":
               criterion = QuestItemCriterion(pServerCriterionForm)
               break
            case "Qo":
               criterion = QuestObjectiveItemCriterion(pServerCriterionForm)
               break
            case "SC":
               criterion = ServerTypeItemCriterion(pServerCriterionForm)
               break
            case "Sc":
               criterion = StaticCriterionItemCriterion(pServerCriterionForm)
               break
            case "Sd":
               criterion = DayItemCriterion(pServerCriterionForm)
               break
            case "SG":
               criterion = MonthItemCriterion(pServerCriterionForm)
               break
            case "SI":
               criterion = ServerItemCriterion(pServerCriterionForm)
               break
            case "ST":
               criterion = ServerSeasonTemporisCriterion(pServerCriterionForm)
               break
            case "Sy":
               criterion = CommunityItemCriterion(pServerCriterionForm)
               break
            default:
               _log.warn("Criterion \'" + s + "\' unknow or unused (" + pServerCriterionForm + ")")
         return criterion
