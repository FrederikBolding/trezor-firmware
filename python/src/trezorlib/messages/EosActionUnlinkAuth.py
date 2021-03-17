# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionUnlinkAuth(p.MessageType):

    def __init__(
        self,
        *,
        account: Optional[int] = None,
        code: Optional[int] = None,
        type: Optional[int] = None,
    ) -> None:
        self.account = account
        self.code = code
        self.type = type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('account', p.UVarintType, None),
            2: ('code', p.UVarintType, None),
            3: ('type', p.UVarintType, None),
        }
