# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MessageSignature(p.MessageType):
    MESSAGE_WIRE_TYPE = 40

    def __init__(
        self,
        *,
        address: str,
        signature: bytes,
    ) -> None:
        self.address = address
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address', p.UnicodeType, p.FLAG_REQUIRED),
            2: ('signature', p.BytesType, p.FLAG_REQUIRED),
        }
