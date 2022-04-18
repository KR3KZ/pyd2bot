import os
from pathlib import Path


r = Path(os.getenv("APPDATA")) / "AnkamaCertificates/v2-RELEASE"
print(r)
