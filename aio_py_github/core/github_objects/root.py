from core.utils import Requester as _Requester
from .github_object import GithubObject as _GithubObject


class Root(_GithubObject):
    def __init__(self, token: str):
        super(Root, self).__init__(_Requester(token))

    async def get_current_user(self):
        raise NotImplementedError

    async def get_authorization(self):
        raise NotImplementedError

    async def get_code_search(self, query, page=None, per_page=None, sort=None, order=None):
        raise NotImplementedError

    async def get_commit_search(self, query, page=None, per_page=None, sort=None, order=None):
        raise NotImplementedError

    async def get_emails(self):
        raise NotImplementedError

    async def get_emojis(self):
        raise NotImplementedError

    async def get_events(self):
        raise NotImplementedError

    async def get_feeds(self):
        raise NotImplementedError

    async def get_followers(self):
        raise NotImplementedError

    async def get_following(self, target=None):
        raise NotImplementedError

    async def get_gists(self, gist_id=None):
        raise NotImplementedError

    async def get_hub(self):
        raise NotImplementedError

    async def get_issue_search(self, query, page=None, per_page=None, sort=None, order=None):
        raise NotImplementedError

    async def get_issues(self):
        raise NotImplementedError

    async def get_keys(self):
        raise NotImplementedError

    async def get_notifications(self):
        raise NotImplementedError

    async def get_organization_repositories(self, organization, type=None, page=None, per_page=None, sort=None):
        raise NotImplementedError

    async def get_organization(self, organization):
        raise NotImplementedError

    async def get_public_gists(self):
        raise NotImplementedError

    async def get_rate_limit(self):
        raise NotImplementedError

    async def get_repository(self, owner, repo):
        raise NotImplementedError

    async def get_repository_search(self, query, page=None, per_page=None, sort=None, order=None):
        raise NotImplementedError

    async def get_current_user_repositories(self, type=None, page=None, per_page=None, sort=None):
        raise NotImplementedError

    async def get_starred(self, owner=None, repo=None):
        raise NotImplementedError

    async def get_starred_gists(self):
        raise NotImplementedError

    async def get_team(self):
        raise NotImplementedError

    async def get_user(self, user=None):
        raise NotImplementedError

    async def get_user_organizations(self):
        raise NotImplementedError

    async def get_user_repositories(self, user, type=None, page=None, per_page=None, sort=None):
        raise NotImplementedError

    async def get_user_search(self, query, page=None, per_page=None, sort=None, order=None):
        raise NotImplementedError
