from aiovkdonate.const import const
from aiovkdonate.http.http import request
from aiovkdonate.types.models import Model


class Donate:
	def __init__(self, token: str):
		self._token = token

	async def get(self, count: int) -> Model:
		response = await request(
				const.donate_api, {
					'key': self._token,
					'count': count,
				}
		)
		return Model(**response)