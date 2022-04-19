import json
import re
import sys
import com.ankamagames.dofus.Constants as Constants

IMPORT_REGX = "^\s*import (?P<module_prefix>\S+(?:\.\S+)*)\.(?P<cls_name>\S+);"
SHUFFLE_MAPPING_REGX = "^\s*_messagesTypes\[(?P<msgId>\d+)\] = (?P<cls_name>\S+);"


def main(msgReceiverAs):
    msgShuffle = dict()
    with open(msgReceiverAs, "r") as fp:
        for line in fp.readlines():
            m = re.match(IMPORT_REGX, line)
            if m:
                module_prefix = m.group("module_prefix")
                cls_name = m.group("cls_name")
                module_path = f"{module_prefix}.{cls_name}"
                if cls_name == "ProtocolRequired" or (
                    cls_name.endswith("Message") and cls_name not in ["INetworkMessage"]
                ):
                    msgShuffle[cls_name] = {"module": module_path, "name": cls_name}
            m = re.match(SHUFFLE_MAPPING_REGX, line)
            if m:
                msgId = m.group("msgId")
                cls_name = m.group("cls_name")
                if cls_name not in msgShuffle:
                    msgShuffle[cls_name] = {}
                msgShuffle[cls_name]["id"] = int(msgId)
    return msgShuffle


if __name__ == "__main__":
    msgReceiverAs = sys.argv[1]
    msgShuffle = main(msgReceiverAs)
    with open(Constants.PROTOCOL_MSG_SHUFFLE_PATH, "w") as fp:
        json.dump(msgShuffle, fp, indent=4, separators=(", ", ": "), sort_keys=True)
