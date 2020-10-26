class ObjColor:
    BOT = [Color(61, 56, 150), Color(251, 241, 191)]
    MOB = [Color(46, 54, 61)]
    FREE = [Color(150, 142, 103), Color(142, 134, 94)]
    OBSTACLE = [Color(255, 255, 255), Color(0, 0, 0), Color(88, 83, 58)]
    REACHABLE = [Color(90, 125, 62), Color(85, 121, 56)]
    INVOKE = [Color(218, 57, 45)]

print(Color(61, 56, 150) in ObjColor.BOT)