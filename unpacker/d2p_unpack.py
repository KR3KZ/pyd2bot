import io, sys, os, json
from pydofus.d2p import D2PReader, InvalidD2PFile
from pydofus.swl import SWLReader, InvalidSWLFile

# python d2p_pack.py (all files in input folder)
# folder output: ./output/{all files}.d2p

path_input = "./input/"
path_output = "./output/"

for file in os.listdir(path_input):
    if file.endswith(".d2p"):
        file_name = os.path.basename(file)
        d2p_file = open(path_input + file, "rb")

        try:
            os.stat(path_output + file_name)
        except:
            os.mkdir(path_output + file_name)

        print("D2P Unpacker for " + file_name)

        try:
            d2p_reader = D2PReader(d2p_file, False)
            d2p_reader.load()
            for name, specs in d2p_reader.files.items():
                print("extract file " + file_name + "/" + name)

                try:
                    os.stat(path_output + file_name + "/" + os.path.dirname(name))
                except:
                    os.makedirs(path_output + file_name + "/" + os.path.dirname(name))

                if "swl" in name:
                    swl = io.BytesIO(specs["binary"])
                    swl_reader = SWLReader(swl)

                    swf_output = open(path_output + file_name + "/" + name.replace("swl", "swf"), "wb")
                    json_output = open(path_output + file_name + "/" + name.replace("swl", "json"), "w")

                    swf_output.write(swl_reader.SWF)
                    swl_data = {'version':swl_reader.version, 'frame_rate':swl_reader.frame_rate, 'classes':swl_reader.classes}
                    json.dump(swl_data, json_output, indent=4)

                    swf_output.close()
                    json_output.close()
                else:
                    file_output = open(path_output + file_name + "/" + name, "wb")
                    file_output.write(specs["binary"])
                    file_output.close()
                pass
        except InvalidD2PFile:
            pass
