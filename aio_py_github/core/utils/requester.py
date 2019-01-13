import aiohttp


class Requester(object):
    def __init__(self, token: str):
        self._url = 'https://api.github.com/'
        self._headers = dict()
        if token:
            self._headers['Authorization'] = 'token {}'.format(token)
        self._headers['content-type'] = 'application/json'
        self._session = aiohttp.ClientSession()

    async def close(self):
        await self._session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def get(self, endpoint: str, params: dict = None) -> dict:
        url = self._url + endpoint
        response = await self._session.get(url=url, params=params, headers=self._headers)
        response = await response.json()
        return response

    async def post(self, endpoint: str, params: dict = None, data: dict = None) -> dict:
        url = self._url + endpoint
        response = await self._session.post(url=url, params=params, data=data, headers=self._headers)
        response = await response.json()
        return response

    async def delete(self, endpoint: str, params: dict = None, data: dict = None) -> dict:
        url = self._url + endpoint
        response = await self._session.delete(url=url, params=params, data=data, headers=self._headers)
        response = await response.json()
        return response
