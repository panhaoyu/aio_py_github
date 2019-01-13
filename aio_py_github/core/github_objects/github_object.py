class GithubObject(object):
    def __init__(self, requester):
        self._requester = requester

    async def load(self):
        pass

    async def close(self):
        pass

    async def __aenter__(self):
        await self.load()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class NotSet(object):
    pass
