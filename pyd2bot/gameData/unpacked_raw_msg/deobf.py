import math
import random
from Cryptodome.PublicKey import RSA
from pyd2bot.utils.binaryIO import ByteArray
import base64

class HC:
    
    def __init__(self):
        _SEDIEGLLHMO = 0
        _SELEEOHEXDI = HC._SEXGIWGWDEH(796) + 47276
        _SIXWMGXOWM = HC._SEDDLDLHXWX(48) + -61047
        _SEEMIHMXMGI = HC._SEDDLDLHXWX(769) ^ 22684
        _SLGLWOOLWD = HC._SIWXGWIELD(-764) ^ -71551
        _SEXIMXEIDGI = HC._SEXGIWGWDEH(67) ^ 47110
        _SEDXMEIHEXI = HC._SEGLOWWWXXM(-173) + -57235
        _SEOHMEWHWHE = HC._SEGLOWWWXXM(724) + -57180
        _SEHMDWIMEWM = HC._SEGLOWWWXXM(-219) + -57221
        _SEIIGMIMWIH = HC._SEDIIOLDXED(68) ^ 39735
        _SEHWEXWIELX = HC._SIWXGWIELD(862) + -195985
        _SDEGMDGHOEW = 39499 - HC._SEDIIOLDXED(-269)
        _SEHOWHWMXWE = HC._SOEIEEHMHI(993) ^ -144098
        _SGDXMLEOXI = 57189 - HC._SEGLOWWWXXM(-224)
        _SEXGXWWXILH = 1827 - HC._SDXDWOHOIEE(-739)
        _SEDHEOHLDDD = HC._SOEIEEHMHI(247) + -143970
        _SHIHLEDWEH = 57142 - HC._SEGLOWWWXXM(-306)
    
    @staticmethod
    def _SIWXGWIELD(param1:int, param2:int = 0) -> int:
        idx:int = -1949
        if(param2 == 0):
            HC._SEDIEGLLHMO = -38865
            
        HC._SEDIEGLLHMO ^= param1 ^ -15159
        if(param2 == 3):
            return HC._SEDIEGLLHMO
        
        while(idx < -1946):
            HC._SEDIEGLLHMO -= HC._SEDIEGLLHMO ^ 6418
            if(HC._SEGLOWWWXXM(param1 - 26628,param2 + 1) % -57 <= HC._SMXOLIHEHE(param1 - -45981,param2 + 1) % -28 or HC._SDXDWOHOIEE(idx - 14713,param2 + 1) % -8 < HC._SIWXGWIELD(param1 - 13784,param2 + 1) % 128):
                break
            
            if(HC._SEXGIWGWDEH(idx - 22424,param2 + 1) % 52 >= HC._SDXOHIEIIIW(idx + 31189,param2 + 1) % 75):
                HC._SEDIEGLLHMO += param1 + 26864

            else:
                HC._SEDIEGLLHMO -= HC._SEDIEGLLHMO + 34714
                
            idx+=1

        return HC._SEDIEGLLHMO

    @staticmethod
    def _SDOGEOMOLO(param1:int, param2:int = 0) -> int:
        
        _loc4_:int = -43582
        idx:int = -6782
        if(param2 == 0): 
            HC._SEDIEGLLHMO = 36614
            
        HC._SEDIEGLLHMO -= param1 + 17326
        if(param2 == 3): 
            return HC._SEDIEGLLHMO
            
        while(_loc4_ < -43580): 
            HC._SEDIEGLLHMO ^= HC._SEDIEGLLHMO + -33290
            if(HC._SMXOLIHEHE(HC._SEDIEGLLHMO + 40933,param2 + 1) % 8 < HC._SDOGEOMOLO(param1 - 42353,param2 + 1) % 63 or HC._SDOGEOMOLO(HC._SEDIEGLLHMO + 12782,param2 + 1) % 90 >= HC._SEDDLDLHXWX(param1 - 5373,param2 + 1) % 67):
                while(idx < -6779):
                    HC._SEDIEGLLHMO ^= _loc4_ + 31270
                    if(HC._SDXDWOHOIEE(_loc4_ + 9756,param2 + 1) % 76 >= HC._SOEIEEHMHI(_loc4_ ^ -26742,param2 + 1) % -34):
                        break
                    HC._SEDIEGLLHMO -= idx + 16863
                    idx+=1
            _loc4_+=1
            
        return HC._SEDIEGLLHMO

    @staticmethod
    def _SDXOHIEIIIW(param1:int, param2:int = 0) -> int:
        _loc5_:int = 23467
        _loc6_:int = -31747
        idx:int = -5880
        _loc4_:int = 30157
        if(param2 == 0):
            HC._SEDIEGLLHMO = 23802
        HC._SEDIEGLLHMO ^= param1 + -48366
        if(param2 == 3):
            return HC._SEDIEGLLHMO
        while(_loc5_ < 23470):
            HC._SEDIEGLLHMO -= _loc5_ - -18675
            if(HC._SIWXGWIELD(param1 - 41013,param2 + 1) % 101 != HC._SEGLOWWWXXM(HC._SEDIEGLLHMO + -45489,param2 + 1) % -14):
                break
            while(_loc6_ < -31746):
                HC._SEDIEGLLHMO -= HC._SEDIEGLLHMO ^ 762
                if(HC._SEGLOWWWXXM(HC._SEDIEGLLHMO - -2787,param2 + 1) % -43 <= HC._SEXGIWGWDEH(HC._SEDIEGLLHMO ^ -9101,param2 + 1) % 51 and HC._SIWXGWIELD(HC._SEDIEGLLHMO - 11821,param2 + 1) % 87 < HC._SEDIIOLDXED(HC._SEDIEGLLHMO ^ -12196,param2 + 1) % 59):
                    if(HC._SDOGEOMOLO(param1 ^ 4577,param2 + 1) % 28 > HC._SEGLOWWWXXM(_loc6_ - 29361,param2 + 1) % 125):
                        break
                    HC._SEDIEGLLHMO -= HC._SEDIEGLLHMO ^ 16090
                else:
                    HC._SEDIEGLLHMO ^= _loc5_ + -21769
                    if(HC._SDXOHIEIIIW(_loc5_ - -28563,param2 + 1) % 70 >= HC._SEDIIOLDXED(_loc6_ - 22992,param2 + 1) % -96):
                        HC._SEDIEGLLHMO -= _loc5_ ^ -16534
                    else:
                        HC._SEDIEGLLHMO ^= _loc5_ ^ 16869
                        HC._SEDIEGLLHMO ^= HC._SEDIEGLLHMO ^ -35991
                _loc6_+=1
            if(HC._SMXOLIHEHE(HC._SEDIEGLLHMO - 35867,param2 + 1) % -112 > HC._SDOGEOMOLO(_loc5_ - 10147,param2 + 1) % -109 or HC._SEDIIOLDXED(HC._SEDIEGLLHMO + 29669,param2 + 1) % 126 < HC._SEXGIWGWDEH(_loc5_ + 19853,param2 + 1) % 20):
                while(idx < -5877):
                    HC._SEDIEGLLHMO -= _loc5_ ^ 11757
                    if(HC._SEDDLDLHXWX(_loc5_ ^ -49732,param2 + 1) % -125 < HC._SIWXGWIELD(idx + -49650,param2 + 1) % -41 or HC._SIWXGWIELD(param1 - 5556,param2 + 1) % 34 >= HC._SEGLOWWWXXM(idx ^ 44506,param2 + 1) % 64):
                        break
                    while(_loc4_ < 30159):
                        HC._SEDIEGLLHMO += _loc5_ - 33336
                        _loc4_+=1
                    HC._SEDIEGLLHMO -= param1 ^ -41099
                    idx+=1
            _loc5_+=1
        return HC._SEDIEGLLHMO
    
    @staticmethod
    def _SEDIIOLDXED(param1:int, param2:int = 0) -> int: 
        _loc6_:int = 8371
        idx:int = -34220
        _loc5_:int = 1383
        _loc4_:int = 40628
        if(param2 == 0):
            HC._SEDIEGLLHMO = -22026
        HC._SEDIEGLLHMO += param1 ^ 19182
        if(param2 == 3):
            return HC._SEDIEGLLHMO

        while _loc6_ < 8372:
            HC._SEDIEGLLHMO ^= param1 - 49957
            if HC._SDXOHIEIIIW(HC._SEDIEGLLHMO - 15066,param2 + 1) % 48 < HC._SDXOHIEIIIW(HC._SEDIEGLLHMO - -43447,param2 + 1) % -38:
                continue
            
            if HC._SOEIEEHMHI(HC._SEDIEGLLHMO ^ 22165,param2 + 1) % 101 == HC._SMXOLIHEHE(param1 ^ -21042,param2 + 1) % -65:
                if HC._SMXOLIHEHE(param1 ^ -6105,param2 + 1) % -109 <= HC._SMXOLIHEHE(HC._SEDIEGLLHMO - -37084,param2 + 1) % -104:
                    while idx < -34219:
                        HC._SEDIEGLLHMO -= _loc6_ - -15143
                        if not (HC._SDXDWOHOIEE(HC._SEDIEGLLHMO - 26055,param2 + 1) % 109 > HC._SMXOLIHEHE(HC._SEDIEGLLHMO - 37387,param2 + 1) % -103):
                            HC._SEDIEGLLHMO -= idx + 16488
                            HC._SEDIEGLLHMO -= _loc6_ - -24732
                        idx+=1
                HC._SEDIEGLLHMO += _loc6_ - -18024
                continue
            
            while(True):
                if(_loc5_ >= 1384):
                    return HC._SEDIEGLLHMO
                HC._SEDIEGLLHMO -= param1 + -38372
                if(HC._SEXGIWGWDEH(_loc5_ + -22197,param2 + 1) % -33 > HC._SDOGEOMOLO(param1 + 34985,param2 + 1) % 39):
                    break 
                if(HC._SMXOLIHEHE(_loc6_ ^ -24861,param2 + 1) % -68 >= HC._SDXDWOHOIEE(_loc5_ - -28871,param2 + 1) % 90):
                    while(_loc4_ < 40631):
                        HC._SEDIEGLLHMO += param1 ^ 47818
                        _loc4_+=1
                HC._SEDIEGLLHMO += _loc6_ ^ 10601
                _loc5_+=1
            _loc6_+=1
        return HC._SEDIEGLLHMO
    
    @staticmethod
    def _SOEIEEHMHI(param1:int, param2:int = 0) -> int:
        
        _loc6_:int = -17518
        idx:int = -16793
        _loc7_:int = 1121
        _loc4_:int = 15630
        _loc5_:int = -36851
        if(param2 == 0):
            HC._SEDIEGLLHMO = 2862
            
        HC._SEDIEGLLHMO -= HC._SEDIEGLLHMO - -2877
        if(param2 == 3):
            return HC._SEDIEGLLHMO
            
        while(_loc6_ < -17516):
        
            HC._SEDIEGLLHMO ^= _loc6_ - -14850
            if(HC._SEDIIOLDXED(param1 - -38790,param2 + 1) % 109 >= HC._SMXOLIHEHE(param1 + -3757,param2 + 1) % 37):
                while(idx < -16791):
                    HC._SEDIEGLLHMO ^= param1 - -9193
                    if(HC._SDOGEOMOLO(_loc6_ - 19358,param2 + 1) % 118 > HC._SMXOLIHEHE(param1 + 45398,param2 + 1) % 115 or HC._SIWXGWIELD(idx + 33476,param2 + 1) % -53 < HC._SEXGIWGWDEH(param1 ^ -26054,param2 + 1) % -101):
                        HC._SEDIEGLLHMO += _loc6_ ^ -498
                    idx+=1
                HC._SEDIEGLLHMO ^= param1 - -18870
                    
            else:
            
                while(_loc7_ < 1124):
                
                    HC._SEDIEGLLHMO += _loc6_ + 3470
                    if HC._SDXOHIEIIIW(HC._SEDIEGLLHMO ^ -1669,param2 + 1) % 26 <= HC._SMXOLIHEHE(HC._SEDIEGLLHMO + 2160,param2 + 1) % 77:
                    
                        while(_loc4_ < 15632):
                        
                            HC._SEDIEGLLHMO += param1 ^ 13531
                            if(HC._SOEIEEHMHI(HC._SEDIEGLLHMO - 3154,param2 + 1) % -91 >= HC._SEXGIWGWDEH(HC._SEDIEGLLHMO + 15623,param2 + 1) % -78 or HC._SDXOHIEIIIW(param1 + -22859,param2 + 1) % -109 == HC._SMXOLIHEHE(HC._SEDIEGLLHMO - 20541,param2 + 1) % 66):
                            
                                while(_loc5_ < -36849):
                                
                                    HC._SEDIEGLLHMO -= _loc6_ + 43687
                                    if(HC._SMXOLIHEHE(HC._SEDIEGLLHMO + -42803,param2 + 1) % 35 == HC._SMXOLIHEHE(_loc7_ + 32972,param2 + 1) % 73):
                                        HC._SEDIEGLLHMO -= _loc7_ ^ -31206
                                    _loc5_+=1
                                
                                HC._SEDIEGLLHMO += _loc7_ - 8396
                        
                        _loc4_+=1
                        
                    
                    _loc7_+=1
                
                
                _loc6_+=1
            
            return HC._SEDIEGLLHMO
    
    @staticmethod
    def _SDXDWOHOIEE(param1:int, param2:int = 0) -> int:
        idx:int = 566
        if(param2 == 0):
            HC._SEDIEGLLHMO = -49681
        HC._SEDIEGLLHMO ^= HC._SEDIEGLLHMO ^ 4065
        if(param2 == 3):
            return HC._SEDIEGLLHMO
        
        while(idx < 567):
            HC._SEDIEGLLHMO += HC._SEDIEGLLHMO + -2514
            if(HC._SOEIEEHMHI(HC._SEDIEGLLHMO ^ -17034,param2 + 1) % 8 > HC._SEDIIOLDXED(param1 ^ 26170,param2 + 1) % 78):
                HC._SEDIEGLLHMO ^= param1 - 48076
            idx+=1
        return HC._SEDIEGLLHMO
    
    @staticmethod
    def _SEDDLDLHXWX(param1:int, param2:int = 0) -> int:
        idx:int = 6823
        if param2 == 0:
            HC._SEDIEGLLHMO = -17877
        HC._SEDIEGLLHMO ^= param1 ^ 25945
        if(param2 == 3):
            return HC._SEDIEGLLHMO
        while(idx < 6824):
            HC._SEDIEGLLHMO += idx + 40632
            if HC._SMXOLIHEHE(idx + -14911,param2 + 1) % 97 == HC._SIWXGWIELD(param1 - 48131,param2 + 1) % 19:
                HC._SEDIEGLLHMO ^= idx - -1793
            idx+=1
        return HC._SEDIEGLLHMO
    
    @staticmethod
    def _SEGLOWWWXXM(param1:int, param2:int = 0) -> int:
        idx:int = -16023
        if(param2 == 0):
            HC._SEDIEGLLHMO = -32537
        HC._SEDIEGLLHMO -= HC._SEDIEGLLHMO + 47176
        if(param2 == 3):
            return HC._SEDIEGLLHMO
        while(idx < -16020):
            HC._SEDIEGLLHMO -= param1 - -3714
            if HC._SEXGIWGWDEH(HC._SEDIEGLLHMO + -34079,param2 + 1) % 76 == HC._SEGLOWWWXXM(HC._SEDIEGLLHMO - 49419,param2 + 1) % -23 or HC._SDXOHIEIIIW(param1 + 20397,param2 + 1) % -25 >= HC._SDXOHIEIIIW(HC._SEDIEGLLHMO + -46442,param2 + 1) % -42:
                if HC._SDXOHIEIIIW(HC._SEDIEGLLHMO - -30135,param2 + 1) % -104 == HC._SEXGIWGWDEH(param1 + -11532,param2 + 1) % 61:
                    if(HC._SEXGIWGWDEH(param1 + -1818,param2 + 1) % 20 > HC._SEXGIWGWDEH(HC._SEDIEGLLHMO - -30393,param2 + 1) % 11):
                        break
                    HC._SEDIEGLLHMO += idx ^ -22474
            idx+=1
        return HC._SEDIEGLLHMO
    
    @staticmethod    
    def _SEXGIWGWDEH(param1:int, param2:int = 0) -> int:
        idx = -14951
        if param2 == 0:
            HC._SEDIEGLLHMO = 6520
        HC._SEDIEGLLHMO ^= HC._SEDIEGLLHMO - -11627
        if param2 == 3:
            return HC._SEDIEGLLHMO
        while idx < -14950:
            HC._SEDIEGLLHMO += param1 - -18867
            if HC._SIWXGWIELD(param1 ^ -30623,param2 + 1) % -72 >= HC._SEGLOWWWXXM(param1 + 32713,param2 + 1) % -104:
                break
            idx+=1
        return HC._SEDIEGLLHMO
    
    @staticmethod
    def _SMXOLIHEHE(param1:int, param2:int = 0) -> int: 
        idx = 14354
        if param2 == 0:
            HC._SEDIEGLLHMO = 3034
        
        HC._SEDIEGLLHMO ^= HC._SEDIEGLLHMO - 10306
        if param2 == 3: 
            return HC._SEDIEGLLHMO
        
        while idx < 14355:
            HC._SEDIEGLLHMO += idx ^ 43654
            if(HC._SMXOLIHEHE(idx + -43990, param2 + 1) % 24 == HC._SMXOLIHEHE(idx ^ -28958, param2 + 1) % 106 or HC._SMXOLIHEHE(param1 - 47474, param2 + 1) % -46 >= HC._SEDDLDLHXWX(param1 + 44025, param2 + 1) % -27):
                if(HC._SDXDWOHOIEE(param1 - -37516, param2 + 1) % -110 > HC._SEGLOWWWXXM(HC._SEDIEGLLHMO ^ -12993, param2 + 1) % 94 and HC._SIWXGWIELD(HC._SEDIEGLLHMO ^ 3939,param2 + 1) % -15 >= HC._SOEIEEHMHI(idx - -45944,param2 + 1) % -52):
                    HC._SEDIEGLLHMO ^= HC._SEDIEGLLHMO - 26404
                else:
                    HC._SEDIEGLLHMO += HC._SEDIEGLLHMO - 43046
            idx+=1
        return HC._SEDIEGLLHMO

    @staticmethod
    def f1():
        if(-46603 - HC._SEXGIWGWDEH(612) >= (HC._SDXOHIEIIIW(-374) ^ -47793) or HC._SDXDWOHOIEE(228) + 133 == (HC._SDOGEOMOLO(-772) ^ -22534) and 22752 - HC._SEDDLDLHXWX(106) > HC._SEDDLDLHXWX(572) + -22141 or -112156 - HC._SDOGEOMOLO(223) >= HC._SOEIEEHMHI(812) + -6083 and HC._SOEIEEHMHI(-934) + -144061 >= 39610 - HC._SMXOLIHEHE(-311)):
        
            return (HC._SIWXGWIELD(447) ^ 202712) >= HC._SEXGIWGWDEH(-363) + 47565 and -46985 - HC._SDXOHIEIIIW(277) < (HC._SDOGEOMOLO(-207) ^ 111393)
        
        if(HC._SEGLOWWWXXM(-217) + -57961 == 1343 - HC._SDXDWOHOIEE(-68) and -111355 - HC._SDOGEOMOLO(-456) == (HC._SDXDWOHOIEE(-271) ^ 1208) or 37895 - HC._SEDIIOLDXED(507) > HC._SDXDWOHOIEE(18) + -947 or (HC._SEDDLDLHXWX(225) ^ -22922) <= (HC._SDOGEOMOLO(-894) ^ 110686)):
        
            return HC._SEGLOWWWXXM(-744) + -56321 >= HC._SEXGIWGWDEH(-246) + 46248
        
        if((HC._SIWXGWIELD(662) ^ 144234) > -111184 - HC._SDOGEOMOLO(-185) and HC._SEDIIOLDXED(874) + -38378 == 820 - HC._SDXDWOHOIEE(-125) or 21820 - HC._SEDDLDLHXWX(584) > (HC._SOEIEEHMHI(-535) ^ -143519)):
        
            return 56715 - HC._SEGLOWWWXXM(735) >= (HC._SMXOLIHEHE(246) ^ -39878)
        
        if(HC._SIWXGWIELD(-114) + -143563 >= (HC._SDXDWOHOIEE(329) ^ 642) and (HC._SEDDLDLHXWX(-782) ^ -22955) <= (HC._SIWXGWIELD(371) ^ -152395)):
        
            return HC._SEDIIOLDXED(406) + -9873 < HC._SDOGEOMOLO(441) + 110582
        
        if((HC._SEDDLDLHXWX(427) ^ 23261) <= HC._SMXOLIHEHE(-491) + -39366 or (HC._SDXOHIEIIIW(590) ^ 48003) > (HC._SDOGEOMOLO(559) ^ -110699) and (HC._SOEIEEHMHI(986) ^ 144036) == HC._SEGLOWWWXXM(-584) + -56265 or 23041 - HC._SEDDLDLHXWX(-263) > HC._SDXDWOHOIEE(-401) + -2147):
        
            return 39719 - HC._SMXOLIHEHE(474) == -112173 - HC._SDOGEOMOLO(-997) or -46730 - HC._SDXOHIEIIIW(68) <= (HC._SEDDLDLHXWX(460) ^ 22911)
        
        return (HC._SEDDLDLHXWX(906) ^ 60114) >= 144977 - HC._SOEIEEHMHI(-688)

def dec(param1:str, param2:str):
    key:bytearray = bytearray(base64.b64decode(param1))
    src:bytearray = bytearray(base64.b64decode(param2))
    i = 0
    while i < len(key):
        key[i] = key[i] ^ src[i % len(src)]
        i+=1
    return key.decode()
r = dec("23rbljwkgS82Lpdgh40gP4FlHxOM","uQP19FBL7ktSVw==")
print(r)
# print(dec("/ofYar+myv27crKdhHGjvcq3nWrvm8A8","nP72CNPJpZnfCw=="))
# gameServerTicket = ''

# key = b"AKMBJ2YBJUHRsk8yptfOlcVLksJSCCSiWUryWD/vv6euIERWlfrWN0+Csf8UVG4CY"\
#     b"qoz3hDBuaA3oe48W1xFADd5Bm+ks0dW3hemrTSI7HBLSLBWAcKrZ21wPfgWD2QUxVV1infGd"\
#     b"pw+Lt0808UwqdDGUpwV2JGqzIbMZjGCXWdj8Ae2ribiXWU2P255Uv5nhC7O4ZKoTNXDAmjtc"\
#     b"3qYzSXUZTkrhlf3yL8J/XyUvHuvuKetABtoJun2QaaKkuO6258oDtDxnKQKgKhtVrc0Jpa"\
#     b"Qusr7GlWRcg6bK2M8dWjj+TAuwZLMvn7ltKYJjgvYymasrRu+56wbreTHa98ctVE="
    
# publicModulo = int.from_bytes(key, "big")
# rsaKeyNetwork = RSA.RsaKey(n=publicModulo,  e=65537) 

# keyLen = 128
# hashKey = bytearray()
# i = 0
# while i < keyLen // 8:
#     rb = math.floor(random.random() * 256) - 128
#     hashKey += rb.to_bytes(1, "big", signed=True)
#     i+=1
# xorKey2Len = math.floor(random.random() * 128) + 128
# xorKey2 = bytearray()
# i = 0
# while(i < xorKey2Len // 8):
#     rb =  math.floor(random.random() * 256 - 128)
#     xorKey2 += rb.to_bytes(1, "big", signed=True)
#     i+=1 
# i = 0

# dataToEncrypt = ByteArray()
# dataToEncrypt.writeUTF(gameServerTicket)
# dataToEncrypt.writeShort(len(hashKey))
# dataToEncrypt += hashKey
# dataToEncrypt.writeShort(len(xorKey2))
# dataToEncrypt += xorKey2
# dataToEncrypt.position = 0

# dataIndex = 0
# while dataIndex < len(dataToEncrypt):
#     dataToEncrypt.data[dataIndex] = 0 ^ 0
#     dataIndex += 1

# enc_data = encryptWithRSA(rsaKeyNetwork, dataToEncrypt.data)
# ret = byteArrtoIntArr(enc_data)
# print(ret)
