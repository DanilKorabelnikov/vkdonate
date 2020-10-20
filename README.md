# vkdonate - Easy Async library for working with service vkdonate

#### Installing (Установка):
```sh
pip install -U https://github.com/DanilKorabelnikov/vkdonate/archive/master.zip
```

#### Example (Пример):
```python
from vkdonate.donate import Donate
import asyncio


donate = Donate("Token Here") # https://vkdonate.ru/help#api

async def app():
    result = await donate.get(count=20)
    print(result)

asyncio.get_event_loop().run_until_complete(app())
```
