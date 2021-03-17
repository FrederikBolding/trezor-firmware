# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MultisigRedeemScriptType import MultisigRedeemScriptType

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeInputScriptType = Literal[0, 1, 2, 3, 4]
        EnumTypeDecredStakingSpendType = Literal[0, 1]
    except ImportError:
        pass


class TxInputType(p.MessageType):

    def __init__(
        self,
        *,
        prev_hash: bytes,
        prev_index: int,
        address_n: Optional[List[int]] = None,
        script_sig: Optional[bytes] = None,
        sequence: int = 4294967295,
        script_type: EnumTypeInputScriptType = 0,
        multisig: Optional[MultisigRedeemScriptType] = None,
        amount: Optional[int] = None,
        decred_tree: Optional[int] = None,
        witness: Optional[bytes] = None,
        ownership_proof: Optional[bytes] = None,
        commitment_data: Optional[bytes] = None,
        orig_hash: Optional[bytes] = None,
        orig_index: Optional[int] = None,
        decred_staking_spend: Optional[EnumTypeDecredStakingSpendType] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.prev_hash = prev_hash
        self.prev_index = prev_index
        self.script_sig = script_sig
        self.sequence = sequence
        self.script_type = script_type
        self.multisig = multisig
        self.amount = amount
        self.decred_tree = decred_tree
        self.witness = witness
        self.ownership_proof = ownership_proof
        self.commitment_data = commitment_data
        self.orig_hash = orig_hash
        self.orig_index = orig_index
        self.decred_staking_spend = decred_staking_spend

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('prev_hash', p.BytesType, p.FLAG_REQUIRED),
            3: ('prev_index', p.UVarintType, p.FLAG_REQUIRED),
            4: ('script_sig', p.BytesType, None),
            5: ('sequence', p.UVarintType, 4294967295),  # default=4294967295
            6: ('script_type', p.EnumType("InputScriptType", (0, 1, 2, 3, 4)), 0),  # default=SPENDADDRESS
            7: ('multisig', MultisigRedeemScriptType, None),
            8: ('amount', p.UVarintType, None),
            9: ('decred_tree', p.UVarintType, None),
            13: ('witness', p.BytesType, None),
            14: ('ownership_proof', p.BytesType, None),
            15: ('commitment_data', p.BytesType, None),
            16: ('orig_hash', p.BytesType, None),
            17: ('orig_index', p.UVarintType, None),
            18: ('decred_staking_spend', p.EnumType("DecredStakingSpendType", (0, 1)), None),
        }
