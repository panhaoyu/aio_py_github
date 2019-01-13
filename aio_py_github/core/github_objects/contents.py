from core.utils.requester import Requester as _Requester
from .github_object import GithubObject as _GithubObject
from .github_object import NotSet as _NotSet
from .repository import Repository


class Content(_GithubObject):
    def __init__(self, requester: _Requester, repository: Repository, path):
        super(Content, self).__init__(requester)
        self.repository = repository
        self.type = _NotSet
        self.encoding = _NotSet
        self.size = _NotSet
        self.name = _NotSet
        self.path = path
        self.sha = _NotSet
        self.url = _NotSet
        self.git_url = _NotSet
        self.html_url = _NotSet
        self.download_url = _NotSet

    async def load(self):
        endpoint = 'repos/{owner}/{repo}/contents/{path}'.format(
            owner=self.repository.owner, repo=self.repository.name, path=self.path)
        response = await self._requester.get(endpoint)
        self._feed_as_directory(response)

    def _feed_as_directory(self, response):
        self.type = response['type']
        self.size = response['size']
        self.name = response['name']
        self.sha = response['sha']
