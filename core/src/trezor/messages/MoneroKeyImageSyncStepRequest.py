# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .MoneroTransferDetails import MoneroTransferDetails

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroKeyImageSyncStepRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 532

    def __init__(
        self,
        *,
        tdis: Optional[List[MoneroTransferDetails]] = None,
    ) -> None:
        self.tdis = tdis if tdis is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('tdis', MoneroTransferDetails, p.FLAG_REPEATED),
        }
