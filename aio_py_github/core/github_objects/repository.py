from .github_object import GithubObject as _GithubObject
from .github_object import NotSet as _NotSet
from .user import User as _User
from core.utils.requester import Requester as _Requester
from core.utils import parser as _parser


class Repository(_GithubObject):
    def __init__(self, requester, owner, name):
        super(Repository, self).__init__(requester)
        self.id = _NotSet
        self.node_id = _NotSet
        self.name = name
        self.full_name = _NotSet
        self.is_private = _NotSet
        self.owner = owner
        self.description = _NotSet
        self.is_fork = _NotSet
        self.created_at = _NotSet
        self.updated_at = _NotSet
        self.pushed_at = _NotSet
        self.git_url = _NotSet
        self.ssh_url = _NotSet
        self.clone_url = _NotSet
        self.svn_url = _NotSet
        self.homepage = _NotSet
        self.size = _NotSet
        self.stargazers_count = _NotSet
        self.watchers_count = _NotSet
        self.language = _NotSet
        self.has_issues = _NotSet
        self.has_projects = _NotSet
        self.has_downloads = _NotSet
        self.has_wiki = _NotSet
        self.has_pages = _NotSet
        self.forks_count = _NotSet
        self.mirror_url = _NotSet
        self.archived = _NotSet
        self.open_issues_count = _NotSet
        self.licences = _NotSet
        self.forks = _NotSet
        self.open_issues = _NotSet
        self.watchers = _NotSet
        self.default_branch = _NotSet
        self.network_count = _NotSet
        self.subscribers_count = _NotSet

    async def load(self):
        """https://developer.github.com/v3/repos/#get"""
        endpoint = 'repos/{user}/{repository}'.format(user=self.owner, repository=self.name)
        response = await self._requester.get(endpoint)
        self.id = int(response['id'])
        self.node_id = str(response['node_id'])
        self.name = str(response['name'])
        self.full_name = str(response['full_name'])
        self.is_private = bool(response['private'])
        self.description = str(response['description'])
        # TODO: There are so many fields, and it's a boring thing to add them.

    async def get_forks(self):
        raise NotImplementedError

    async def get_keys(self, key_id):
        raise NotImplementedError

    async def get_collaborators(self, collaborator=None):
        raise NotImplementedError

    async def get_teams(self):
        raise NotImplementedError

    async def get_hooks(self):
        raise NotImplementedError

    async def get_issue_events(self, number):
        raise NotImplementedError

    async def get_events(self):
        raise NotImplementedError

    async def get_assignees(self):
        raise NotImplementedError

    async def get_branches(self):
        raise NotImplementedError

    async def get_tags(self):
        raise NotImplementedError

    async def get_blobs(self):
        raise NotImplementedError

    async def get_git_tags(self):
        raise NotImplementedError

    async def get_git_refs(self):
        raise NotImplementedError

    async def get_trees(self):
        raise NotImplementedError

    async def get_statuses(self):
        raise NotImplementedError

    async def get_languages(self):
        raise NotImplementedError

    async def get_stargazers(self):
        raise NotImplementedError

    async def get_contributors(self):
        raise NotImplementedError

    async def get_subscribers(self):
        raise NotImplementedError

    async def get_subscription(self):
        raise NotImplementedError

    async def get_git_commits(self):
        raise NotImplementedError

    async def get_comments(self):
        raise NotImplementedError

    async def get_issue_comment(self):
        raise NotImplementedError

    async def get_contents(self, path=None):
        raise NotImplementedError

    async def get_compare(self):
        raise NotImplementedError

    async def get_merges(self):
        raise NotImplementedError

    async def get_archive(self):
        raise NotImplementedError

    async def get_downloads(self):
        raise NotImplementedError

    async def get_issues(self):
        raise NotImplementedError

    async def get_pulls(self):
        raise NotImplementedError

    async def get_milestones(self):
        raise NotImplementedError

    async def get_notifications(self):
        raise NotImplementedError

    async def get_labels(self):
        raise NotImplementedError

    async def get_releases(self):
        raise NotImplementedError

    async def get_deployments(self):
        raise NotImplementedError
