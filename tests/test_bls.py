from brownie import TestBLS, accounts

from py_ecc.optimized_bn128 import *
from eth_hash.auto import keccak
from typing import Tuple
from eth_utils import encode_hex


def get_public_key(secret_key: int):
    return multiply(G2, secret_key)


def sign(message: Tuple[FQ, FQ, FQ], secret_key: int):
    return multiply(message, secret_key)


def aggregate_signature(signatures):
    pass


def aggregate_public_keys(signatures):
    pass


def hash_to_point(data: str):
    return map_to_point(keccak(data))


def map_to_point(x):
    pass


def sqrt(x_sqaure: int) -> Tuple[int, bool]:
    pass


def parse_solc_G1(solc_G1: Tuple[int, int]):
    x, y = solc_G1
    return FQ(x), FQ(y), FQ(1)


def format_G1(g1_element: Tuple[FQ, FQ, FQ]) -> Tuple[FQ, FQ]:
    x, y = normalize(g1_element)
    return (str(x), str(y))


def format_G2(g2_element: Tuple[FQ2, FQ2, FQ2]) -> Tuple[FQ2, FQ2]:
    x, y = normalize(g2_element)
    x1, x2 = x.coeffs
    y1, y2 = y.coeffs
    return x1, x2, y1, y2


def test_main():
    test_bls = accounts[0].deploy(TestBLS)

    secret_key = 123

    public_key = get_public_key(secret_key)
    data = encode_hex("fooooo")
    message_solc = tuple(test_bls.hashToPoint(data))
    message = parse_solc_G1(message_solc)
    sig = sign(message, secret_key)
    message_solc_2 = format_G1(message)
    assert message_solc_2 == message_solc
    pubkey_solc = format_G2(public_key)
    sig_solc = format_G1(sig)

    assert test_bls.verifySingle(sig_solc, pubkey_solc, message_solc_2)

def test_internal():
    test_bls = accounts[0].deploy(TestBLS)
    N = 21888242871839275222246405745257275088696311157297823662689037894645226208583;

    # test submod with a>b
    a = 16892529993056482552485669957863612836432816989509464843349488177090397978789
    b = 10547156594123983059799308138658569114243770050893198291525700850739309859937
    assert (a-b % N) ==  test_bls.submod(a,b,N)

    # test submod with a<b
    a = 2887636117557138566317124683879803668620536475764517791345341369549693202511
    b = 10444549903735524959536677150525069990060091594425138117547036643047941623085
    assert ((a-b) % N) ==  test_bls.submod(a,b,N)