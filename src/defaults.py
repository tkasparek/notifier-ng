
from pathlib import Path


class Singleton(type):
    """Singleton object."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Defaults(metaclass=Singleton):
    def __init__(self) -> None:
        self.cfg_locations = ('./notifier.conf', './.notifier.conf', '{}/.notifier.conf'.format(str(Path.home())), '/etc/notifier.conf')
