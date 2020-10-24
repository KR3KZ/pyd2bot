from sikuli.Sikuli import *

PATTERNS = {
    "kralamoure": [
            Pattern("kralamoure001.png").similar(0.41), 
            Pattern("kralamoure002.png").similar(0.52), 
            Pattern("kralamoure003.png").similar(0.61),
            "1603456433365.png"
            ],
    "poissonPane": [Pattern("poissonPane001.png").similar(0.57)],
    "poisskaille": [Pattern("poisskaille001.png").similar(0.51)],
    "sardineBrillante": [
            Pattern("sardineBrillante001.png").similar(0.45),
            Pattern("sardineBrillante002.png").similar(0.56)
            ],
    "greuvette": Pattern("greuvette.png").similar(0.50),
    "crabe": "crabe.png",
    "espadon": "1603321953298.png"
    
}
