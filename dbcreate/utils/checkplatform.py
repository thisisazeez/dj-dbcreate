import platform
from enum import Enum

class OperatingSystem(Enum):
    LINUX = 'Linux'
    WINDOWS = 'Windows'
    OTHER = 'Other'

def get_operating_system():
    system_name = platform.system()
    if system_name == 'Linux':
        return OperatingSystem.LINUX
    elif system_name == 'Windows':
        return OperatingSystem.WINDOWS
    else:
        return OperatingSystem.OTHER
