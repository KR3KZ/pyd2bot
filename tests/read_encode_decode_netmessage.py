
from time import perf_counter
from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import IdentificationMessage
from com.ankamagames.dofus.network.types.version.Version import Version
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.jerakine.network.parser.NetworkMessageEncoder import NetworkMessageEncoder

t = perf_counter()
version = Version()
version.init(
    build_=11,
    buildType_=0,
    code_=5,
    major_=2,
    minor_=62
)
imsg = IdentificationMessage()
imsg.init(
    autoconnect_=False,
    credentials_=[11, -11],
    failedAttempts_=[],
    lang_='fr',
    serverId_=0,
    sessionOptionalSalt_=0,
    useCertificate_=False,
    useLoginToken_=False,
    version_=version
)
print("init took {}".format(perf_counter() - t))

t = perf_counter()
data = imsg.pack()
print("pack took {}".format(perf_counter() - t))


data.position = 0

t= perf_counter()
imsg = IdentificationMessage.unpack(data)
print("unpack took {}".format(perf_counter() - t))

t = perf_counter()
msg_jspn = imsg.to_json()
print("json message is {}".format(msg_jspn))
print("to_json took {}".format(perf_counter() - t))

t = perf_counter()
r = NetworkMessageEncoder.decodeFromJson(msg_jspn)
print("decodeFromJson took {}".format(perf_counter() - t))

a = NetworkMessage.from_json({
            '__type__': 'IdentificationMessage',
            'autoconnect': True,
            'credentials': [121, 54, 8],
            'failedAttempts': [],
            'lang': 'fr',
            'serverId': 0,
            'sessionOptionalSalt': 0,
            'useCertificate': True,
            'useLoginToken': False,
            'version': {
                '__type__': 'Version',
                'build': 13,
                'buildType': 0,
                'code': 5,
                'major': 2,
                'minor': 62
            }
        })