# vkdonate - Easy Async library for working with service vkdonate

#### Installing (Установка):
```sh
pip install -U https://github.com/DanilKorabelnikov/vkdonate/archive/master.zip
```

#### Example (Пример):
```python
from vkdonate.donate import Donate
import asyncio


donate = Donate("Token Here")

async def app():
    result = await donate.get(city=20)
    print(result)

asyncio.run(app())
```
