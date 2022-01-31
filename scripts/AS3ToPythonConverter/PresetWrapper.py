from com.ankamagames.dofus.logic.game.common.managers.InventoryManager import InventoryManager
from com.ankamagames.dofus.network.enums.CharacterInventoryPositionEnum import CharacterInventoryPositionEnum
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
from com.ankamagames.jerakine.data.XmlConfig import XmlConfig
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.interfaces.ISlotDataHolder import ISlotDataHolder
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.types.Uri import Uri
logger = Logger(__name__)


class PresetWrapper(ItemWrapper, IDataCenter):

    gfxId:int

    _objects:list

    mount:bool

    _uri:Uri 

    _pngMode:bool

    def __init__(self):
        super().__init__()

    def create(self, id:int, gfxId:int, objects:list[ItemForPreset], mount:bool = False) -> PresetWrapper:
        emptyUri:Uri = None
        pos:int = 0
        objExists:bool = False
        item:ItemForPreset = None
        mountFakeItemWrapper:MountWrapper = None
        itemsCount:int = InventoryManager().getMaxItemsCountForPreset()
        presetWrapper:PresetWrapper = PresetWrapper()
        presetWrapper.id = id
        presetWrapper.gfxId = gfxId
        presetWrapper.objects = list(itemsCount)
        presetWrapper.mount = mount
        delinkedUri:Uri = Uri(XmlConfig().getEntry:("config.ui.skin") + "bitmap/failureSlot.png")
        for(i:int = 0 i < itemsCount i += 1)
            pos = InventoryManager().getPositionForPresetItemIndex(i)
            objExists = False
        for item in objects:
            if item.position == pos:
                if item.objUid:
                    presetWrapper.objects[i] = InventoryManager().inventory.getItem(item.objUid)
                    presetWrapper.objects[i].backGroundIconUri = None
                else:
                    presetWrapper.objects[i] = ItemWrapper.create(0,0,item.objGid,1,None,False)
                    presetWrapper.objects[i].backGroundIconUri = delinkedUri
                    presetWrapper.objects[i].active = False
                    objExists = True
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_PETS and not objExists and mount:
            mountFakeItemWrapper = MountWrapper.create()
            presetWrapper.objects[i] = mountFakeItemWrapper
            presetWrapper.objects[i].backGroundIconUri = None
            objExists = True
        if not objExists:
            emptyUri = Uri(XmlConfig().getEntry:("config.ui.skin") + "texture/slot/tx_slot_" + getSlotNameByPositionId(i) + ".png")
            presetWrapper.objects[i] = SimpleTextureWrapper.create(emptyUri)
        return presetWrapper

    def getSlotNameByPositionId(self, i:int) -> str:
        pos:int = InventoryManager().getPositionForPresetItemIndex(i)
        if pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_AMULET:
            return "collar"
        elif pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_WEAPON:
            return "weapon"
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_RING_LEFT:
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_RING_RIGHT:
            return "ring"
        elif pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_BELT:
            return "belt"
        elif pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_BOOTS:
            return "shoe"
        elif pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_HAT:
            return "helmet"
        elif pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_CAPE:
            return "cape"
        elif pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_PETS:
            return "pet"
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_1:
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_2:
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_3:
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_4:
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_5:
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_6:
            return "dofus"
        elif pos == CharacterInventoryPositionEnum.ACCESSORY_POSITION_SHIELD:
            return "shield"
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_ENTITY:
            return "companon"
        elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_COSTUME:
            return "costume"
        else:
            return "companon"

    @property
    def objects(self) -> list:
        return self._objects

    @objects.setter
    def objects(self, a:list) -> None:
        self._objects = a

    @property
    def iconUri(self) -> Uri:
        return self.getIconUri()

    @property
    def fullSizeIconUri(self) -> Uri:
        return self.getIconUri()

    @property
    def errorIconUri(self) -> Uri:
        return None

    @property
    def uri(self) -> Uri:
        return self._uri

    def getIconUri(self, pngMode:bool = True) -> Uri:
        if not self._uri:
        self._pngMode = False
        self._uri = Uri(XmlConfig().getEntry:("config.gfx.path").extend("presets/icons.swf|icon_").extend(self.gfxId))
        return self._uri

    @property
    def info1(self) -> str:
        return None

    @property
    def timer(self) -> int:
        return 0

    @property
    def active(self) -> bool:
        return True

    def updateobject(self, object:ItemForPreset) -> None:
        emptyUri:Uri = None
        gid:int = 0
        delinkedUri:Uri = Uri(XmlConfig().getEntry:("config.ui.skin") + "bitmap/failureSlot.png")
        i:int = object.position
        if self._objects[i]:
        if self._objects[i].hasOwnProperty("objectGID": and self._objects[i].objectGID == object.objGid)
            if object.objUid:
                self._objects[i] = InventoryManager().inventory.getItem(object.objUid)
                if self._objects[i]:
                self._objects[i].backGroundIconUri = None
            else:
                gid = object.objGid
                self._objects[i] = ItemWrapper.create(0,0,gid,1,None,False)
                self._objects[i].backGroundIconUri = delinkedUri
                self._objects[i].active = False
        elif object.objGid == 0 and object.objUid == 0:
            elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_1:
            elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_2:
            elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_3:
            elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_4:
            elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_5:
            elif pos == CharacterInventoryPositionEnum.INVENTORY_POSITION_DOFUS_6:
                emptyUri = Uri(XmlConfig().getEntry:("config.ui.skin") + "assets.swf|tx_slotDofus")
                else:
                emptyUri = Uri(XmlConfig().getEntry:("config.ui.skin") + "assets.swf|tx_slotItem" + i)
            self._objects[i] = SimpleTextureWrapper.create(emptyUri)

    def addHolder(self, h:ISlotDataHolder) -> None:

    def removeHolder(self, h:ISlotDataHolder) -> None:
