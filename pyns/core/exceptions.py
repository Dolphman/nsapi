from nationstates.NScore.exceptions import CollectError, NSError, ConnectionError

class BaseNSError(NSError):
    pass

class InvalidShard(KeyError, AttributeError, NSError):
    pass

class InvalidTag(NSError):
    pass

