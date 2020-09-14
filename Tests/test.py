from census import Census
from temp import payload
import requests

c = Census()

print(payload)

print(requests.post(c.base + "/census", data=payload, headers=c.headers).json())
