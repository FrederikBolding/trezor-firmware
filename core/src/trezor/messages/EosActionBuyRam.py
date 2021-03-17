# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .EosAsset import EosAsset

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionBuyRam(p.MessageType):

    def __init__(
        self,
        *,
        payer: Optional[int] = None,
        receiver: Optional[int] = None,
        quantity: Optional[EosAsset] = None,
    ) -> None:
        self.payer = payer
        self.receiver = receiver
        self.quantity = quantity

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('payer', p.UVarintType, None),
            2: ('receiver', p.UVarintType, None),
            3: ('quantity', EosAsset, None),
        }
