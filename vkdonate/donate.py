from vkdonate.const import const
from vkdonate.http.http import request
from vkdonate.types.models import Model


class Donate:
	def __init__(self, token: str):
		"""
		:param token: your api-key https://home.openweathermap.org/api_keys
		"""
		self._token = token

	async def get(self, count: int) -> Model:
		response = await request(
				const.donate_api, {
					'key': self._token,
					'count': count,
				}
		)
		return Model(**response)