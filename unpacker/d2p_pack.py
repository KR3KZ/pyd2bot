import io, sys, os, tempfile, fnmatch, json
from collections import OrderedDict
from pydofus.d2p import D2PReader, D2PBuilder, InvalidD2PFile
from pydofus.swl import SWLReader, SWLBuilder, InvalidSWLFile
from pydofus._binarystream import _BinaryStream

# python d2p_pack.py file.d2p (require original file in input folder and unpacked file in output folder)
# file output: ./output/~generated/file.d2p

path_input = "./input/"
path_output = "./output/"

try:
    file = sys.argv[1]
except:
    file = None

try:
    swl_mode = sys.argv[2]
except:
    swl_mode = None

if file is None or swl_mode is None:
    print("usage: python d2p_pack.py {file.d2p} {swl ture|false}")
else:
    print("D2P Packer for " + file)

    try:
        os.stat(path_output + "~generated")
    except:
        os.mkdir(path_output + "~generated")

    d2p_input = open(path_input + file, "rb")
    d2p_template = D2PReader(d2p_input)

    d2p_ouput = open(path_output + "~generated/" + file, "wb")
    d2p_builder = D2PBuilder(d2p_template, d2p_ouput)

    list_files = OrderedDict()

    rootPath = path_output + file

    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, "*.*"):
            path = os.path.join(root, filename).replace("\\", "/")
            file = path.replace(rootPath + "/", "")
            object_ = {}

            if "swf" in file and swl_mode == "true":
                json_input = open(path.replace("swf", "json"), "r")
                swf_input = open(path, "rb")
                swl_output = tempfile.TemporaryFile()

                swl_data = json.load(json_input)
                swl_data["SWF"] = swf_input.read()

                swl_builder = SWLBuilder(swl_data, swl_output)
                swl_builder.build()

                swl_output.seek(0)
                object_["binary"] = swl_output.read()
                list_files[file.replace("swf", "swl")] = object_

                json_input.close()
                swf_input.close()
                swl_output.close()
            elif "json" in file and swl_mode == "true":
                continue
            else:
                new_file = open(path, "rb")
                object_["binary"] = new_file.read()
                new_file.close()
                list_files[file] = object_

            print("pack file " + file)

    d2p_builder.files = list_files
    d2p_builder.build()

    d2p_input.close()
    d2p_ouput.close()
