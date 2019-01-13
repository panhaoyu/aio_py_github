import asyncio
from utils import requester, base
import user as _user


class Github(base.GithubObject):
    def __init__(self, token=None):
        """
        Login github, or just get a anonymous entrypoint.
        :param token: Github token, you should get it from github website.
        """
        super(Github, self).__init__(requester.Requester(token))

    async def close(self):
        await self._requester.close()

    async def get_fields(self, entrypoint):
        response = await self._requester.get(entrypoint)
        return response

    async def get_a_single_user(self, username):
        async with _user.User(self._requester, username) as user:
            return user

    async def get_the_authenticated_user(self):
        async with _user.AuthenticatedUser(self._requester) as user:
            return user


async def get_fields():
    async with Github('f0b9fc1e7a53214409968234e7821f310d9ef238') as github:
        response = await github.get_fields('user')
        from pprint import pprint
        print(response.keys())
        pprint(response)


async def test():
    async with Github('f0b9fc1e7a53214409968234e7821f310d9ef238') as github:
        user = await github.get_the_authenticated_user()
        print(user.url)


if __name__ == '__main__':
    # asyncio.run(get_fields())
    asyncio.run(test())
