                                                            
   class Item(IPostInit, IDataCenter):
      
      MODULE:str = "Items"
      
      SUPERTYPE_NOT_EQUIPABLE:list = [DataEnum.ITEM_SUPERTYPE_RESOURCES,DataEnum.ITEM_SUPERTYPE_QUEST_ITEMS,DataEnum.ITEM_SUPERTYPE_MUTATIONS,DataEnum.ITEM_SUPERTYPE_FOODS,DataEnum.ITEM_SUPERTYPE_BLESSINGS,DataEnum.ITEM_SUPERTYPE_CURSES,DataEnum.ITEM_SUPERTYPE_CONSUMABLE,DataEnum.ITEM_SUPERTYPE_ROLEPLAY_BUFFS,DataEnum.ITEM_SUPERTYPE_FOLLOWERS,DataEnum.ITEM_SUPERTYPE_MOUNTS,DataEnum.ITEM_SUPERTYPE_CATCHING_ITEMS,DataEnum.ITEM_SUPERTYPE_LIVING_ITEMS]
      
      MAX_JOB_LEVEL_GAP:int = 100
      
      logger = logging.getLogger("bot")
      
      _censoredIcons:dict
      
      idAccessors:IdAccessors = IdAccessors(getItemById,getItems)
       
      
      id:int
      
      nameId:int
      
      typeId:int
      
      descriptionId:int
      
      iconId:int
      
      level:int
      
      realWeight:int
      
      cursed:bool
      
      useAnimationId:int
      
      usable:bool
      
      targetable:bool
      
      exchangeable:bool
      
      price:float
      
      twoHanded:bool
      
      etheral:bool
      
      itemSetId:int
      
      criteria:str
      
      criteriaTarget:str
      
      hideEffects:bool
      
      enhanceable:bool
      
      nonUsableOnAnother:bool
      
      appearanceId:int
      
      secretRecipe:bool
      
      dropMonsterIds:list[int]
      
      dropTemporisMonsterIds:list[int]
      
      recipeSlots:int
      
      recipeIds:list[int]
      
      objectIsDisplayOnWeb:bool
      
      bonusIsSecret:bool
      
      possibleEffects:list[EffectInstance]
      
      evolutiveEffectIds:list[int]
      
      favoriteSubAreas:list[int]
      
      favoriteSubAreasBonus:int
      
      craftXpRatio:int
      
      craftVisible:str
      
      craftConditional:str
      
      craftFeasible:str
      
      needUseConfirm:bool
      
      isDestructible:bool
      
      isLegendary:bool
      
      isSaleable:bool
      
      nuggetsBySubarea:list[Vector.<float>]
      
      containerIds:list[int]
      
      resourcesBySubarea:list[Vector.<int>]
      
      visibility:str
      
      importantNoticeId:int
      
      changeVersion:str
      
      tooltipExpirationDate:float = None
      
      _name:str
      
      _undiatricalName:str
      
      _description:str
      
      _type:ItemType
      
      _weight:int
      
      _itemSet:ItemSet
      
      _appearance:TiphonEntityLook
      
      _conditions:GroupItemCriterion
      
      _conditionsTarget:GroupItemCriterion
      
      _craftVisibleConditions:GroupItemCriterion
      
      _craftConditions:GroupItemCriterion
      
      _craftFeasibleConditions:GroupItemCriterion
      
      _recipes:list
      
      _craftXpByJobLevel:dict
      
      _nuggetsQuantity:float = 0
      
      _basicExperienceAsFood:float = 0
      
      _importantNotice:str = None
      
      _processedImportantNotice:str = None
      
      def __init__(self):
         super().__init__()
      
      def getItemById(self, id:int, returnDefaultItemIfNull:bool = True) -> Item:
         item:Item = GameData.getObject(MODULE,id)
         if item or not returnDefaultItemIfNull:
            return item
         logger.error("Impossible de trouver l\'objet " + id + ", remplacement par l\'objet 666")
         return GameData.getObject(MODULE,666)
      
      def getItems(self) -> list:
         return GameData.getObjects(MODULE)
      
      def getItemsByIds(self, ids:list[int]) -> list[Item]:
         id = None
         item = None
         items:list[Item] = list[Item]()
         for id in ids:
            item = GameDataFileAccessor().getObject(MODULE,id)
            if item:
               items.append(item)
         return items
      
      @property
      def name(self) -> str:
         if not self._name:
            self._name = I18n.getText(self.nameId)
         return self._name
      
      @property
      def undiatricalName(self) -> str:
         if not self._undiatricalName:
            self._undiatricalName = I18n.getUnDiacriticalText(self.nameId)
         return self._undiatricalName
      
      @property
      def description(self) -> str:
         if not self._description:
            if self.etheral:
               self._description = I18n.getUiText("ui.common.etherealWeaponDescription")
            else:
               self._description = I18n.getText(self.descriptionId)
         return self._description
      
      @property
      def importantNotice(self) -> str:
         if not self._importantNotice:
            self._importantNotice = I18n.getText(self.importantNoticeId)
         return self._importantNotice
      
      @property
      def processedImportantNotice(self) -> str:
         if self._processedImportantNotice is not None:
            return self._processedImportantNotice
         if not self.importantNotice:
            return None
         self._processedImportantNotice = HyperlinkMapPosition.parseMapLinks(self.importantNotice)
         return self._processedImportantNotice
      
      @property
      def weight(self) -> int:
         return self._weight
      
      @weight.setter
      def weight(self, n:int) -> None:
         self._weight = n
      
      @property
      def type(self) -> Object:
         if not self._type:
            self._type = ItemType.getItemTypeById(self.typeId)
         return self._type
      
      @property
      def isWeapon(self) -> bool:
         return False
      
      @property
      def itemSet(self) -> ItemSet:
         if not self._itemSet:
            self._itemSet = ItemSet.getItemSetById(self.itemSetId)
         return self._itemSet
      
      @property
      def appearance(self) -> TiphonEntityLook:
         appearance:Appearance = None
         if not self._appearance:
            appearance = Appearance.getAppearanceById(self.appearanceId)
            if appearance:
               self._appearance = TiphonEntityLook.fromstr(appearance.data)
         return self._appearance
      
      @property
      def recipes(self) -> list:
         numRecipes:int = 0
         i:int = 0
         recipe:Recipe = None
         it:Item = None
         gic:GroupItemCriterion = None
         if not self._recipes:
            numRecipes = len(self.recipeIds)
            self._recipes = list()
            for i = 0 i < numRecipes i += 1:
               recipe = Recipe.getRecipeByResultId(self.recipeIds[i])
               if recipe:
                  it = Item.getItemById(recipe.resultId)
                  gic = it.craftVisibleConditions if not not it else None
                  if not gic or gic.isRespected:
                     self._recipes.append(recipe)
         return self._recipes
      
      @property
      def category(self) -> int:
         if self.typeId == 0 or not self.type:
            return ItemCategoryEnum.OTHER_CATEGORY
         return self.type.categoryId
      
      @property
      def conditions(self) -> GroupItemCriterion:
         if not self.criteria:
            return None
         if not self._conditions:
            self._conditions = GroupItemCriterion(self.criteria)
         return self._conditions
      
      @property
      def targetConditions(self) -> GroupItemCriterion:
         if not self.criteriaTarget:
            return None
         if not self._conditionsTarget:
            self._conditionsTarget = GroupItemCriterion(self.criteriaTarget)
         return self._conditionsTarget
      
      @property
      def craftVisibleConditions(self) -> GroupItemCriterion:
         if not self.craftVisible:
            return None
         if not self._craftVisibleConditions:
            self._craftVisibleConditions = GroupItemCriterion(self.craftVisible)
         return self._craftVisibleConditions
      
      @property
      def craftConditions(self) -> GroupItemCriterion:
         if not self.craftConditional:
            return None
         if not self._craftConditions:
            self._craftConditions = GroupItemCriterion(self.craftConditional)
         return self._craftConditions
      
      @property
      def craftFeasibleConditions(self) -> GroupItemCriterion:
         if not self.craftFeasible:
            return None
         if not self._craftFeasibleConditions:
            self._craftFeasibleConditions = GroupItemCriterion(self.craftFeasible)
         return self._craftFeasibleConditions
      
      def getCraftXpByJobLevel(self, jobLevel:int) -> int:
         xpWithRatio:float = None
         basicXp:float = None
         if not self._craftXpByJobLevel:
            self._craftXpByJobLevel = dict()
         if not self._craftXpByJobLevel[jobLevel]:
            if jobLevel - MAX_JOB_LEVEL_GAP > self.level:
               self._craftXpByJobLevel[jobLevel] = 0
               return self._craftXpByJobLevel[jobLevel]
            basicXp = 20 * self.level / (Math.pow(jobLevel - self.level,1.1) / 10 + 1)
            if self.craftXpRatio > -1:
               xpWithRatio = basicXp * (self.craftXpRatio / 100)
            elif self.type.craftXpRatio > -1:
               xpWithRatio = basicXp * (self.type.craftXpRatio / 100)
            else:
               xpWithRatio = basicXp
            self._craftXpByJobLevel[jobLevel] = math.floor(xpWithRatio)
         return self._craftXpByJobLevel[jobLevel]
      
      @property
      def nuggetsQuantity(self) -> float:
         nuggets:list[float] = None
         if self._nuggetsQuantity == 0:
            for nuggets in self.nuggetsBySubarea:
               self._nuggetsQuantity += nuggets[1]
         return self._nuggetsQuantity
      
      @property
      def basicExperienceAsFood(self) -> float:
         experienceInt:int = 0
         if self._basicExperienceAsFood == 0:
            self._basicExperienceAsFood = self.nuggetsQuantity / len(self.nuggetsBySubarea)
            experienceInt = math.floor(self._basicExperienceAsFood * 100000)
            self._basicExperienceAsFood = experienceInt / 100000
         return self._basicExperienceAsFood
      
      def copy(self, from:Item, to:Item) -> None:
         to.id = from.id
         to.nameId = from.nameId
         to.typeId = from.typeId
         to.descriptionId = from.descriptionId
         to.iconId = from.iconId
         to.level = from.level
         to.realWeight = from.realWeight
         to.weight = from.weight
         to.cursed = from.cursed
         to.useAnimationId = from.useAnimationId
         to.usable = from.usable
         to.targetable = from.targetable
         to.price = from.price
         to.twoHanded = from.twoHanded
         to.etheral = from.etheral
         to.enhanceable = from.enhanceable
         to.nonUsableOnAnother = from.nonUsableOnAnother
         to.itemSetId = from.itemSetId
         to.criteria = from.criteria
         to.criteriaTarget = from.criteriaTarget
         to.hideEffects = from.hideEffects
         to.appearanceId = from.appearanceId
         to.recipeIds = from.recipeIds
         to.recipeSlots = from.recipeSlots
         to.secretRecipe = from.secretRecipe
         to.bonusIsSecret = from.bonusIsSecret
         to.objectIsDisplayOnWeb = from.objectIsDisplayOnWeb
         to.possibleEffects = from.possibleEffects
         to.evolutiveEffectIds = from.evolutiveEffectIds
         to.favoriteSubAreas = from.favoriteSubAreas
         to.favoriteSubAreasBonus = from.favoriteSubAreasBonus
         to.dropMonsterIds = from.dropMonsterIds
         to.dropTemporisMonsterIds = from.dropTemporisMonsterIds
         to.resourcesBySubarea = from.resourcesBySubarea
         to.exchangeable = from.exchangeable
         to.craftXpRatio = from.craftXpRatio
         to.needUseConfirm = from.needUseConfirm
         to.isDestructible = from.isDestructible
         to.isLegendary = from.isLegendary
         to.isSaleable = from.isSaleable
         to.craftVisible = from.craftVisible
         to.craftConditional = from.craftConditional
         to.craftFeasible = from.craftFeasible
         to.nuggetsBySubarea = from.nuggetsBySubarea
         to.containerIds = from.containerIds
         to.visibility = from.visibility
         to.importantNoticeId = from.importantNoticeId
         to.changeVersion = from.changeVersion
         to.tooltipExpirationDate = from.tooltipExpirationDate
      
      def postInit(self) -> None:
         if not _censoredIcons:
            _censoredIcons = CensoredContentManager().getCensoredIndex(1)
         if _censoredIcons[self.iconId]:
            self.iconId = _censoredIcons[self.iconId]
         self.name
         self.undiatricalName
      
      def isEvolutive(self) -> bool:
         return self.evolutiveEffectIds and len(self.evolutiveEffectIds) > 0
      
      @property
      def visible(self) -> bool:
         if not self.visibility:
            return True
         gic:GroupItemCriterion = GroupItemCriterion(self.visibility)
         return gic.isRespected
