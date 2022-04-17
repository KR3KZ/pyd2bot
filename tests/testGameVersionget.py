import com.ankamagames.dofus.Constants as Constants
from com.ankamagames.dofus.misc.BuildTypeParser import BuildTypeParser
from com.ankamagames.dofus.network.enums.BuildTypeEnum import BuildTypeEnum
from com.ankamagames.jerakine.types.Version import Version


class BuildInfos:
    with open(Constants.GAME_VERSION_PATH, "r") as fp:
        VERSION: Version = Version(fp.read().strip(), BuildTypeEnum.RELEASE.value)
    print(VERSION)
