# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class DebugLinkWatchLayout(p.MessageType):
    MESSAGE_WIRE_TYPE = 9006

    def __init__(
        self,
        *,
        watch: Optional[bool] = None,
    ) -> None:
        self.watch = watch

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('watch', p.BoolType, None),
        }
