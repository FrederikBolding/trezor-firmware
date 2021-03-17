# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionDeleteAuth(p.MessageType):

    def __init__(
        self,
        *,
        account: Optional[int] = None,
        permission: Optional[int] = None,
    ) -> None:
        self.account = account
        self.permission = permission

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('account', p.UVarintType, None),
            2: ('permission', p.UVarintType, None),
        }
