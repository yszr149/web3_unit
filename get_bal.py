from web3 import Web3
import sys

from web3_common.rpc import RPC_BSC, RPC_OP
from web3_common.util import get_bal, get_eth_bal

address = sys.argv[1]
w3 = Web3(Web3.HTTPProvider(RPC_BSC))
BUSD_ADDRESS = "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
print(f"{address} busd bal:{Web3.fromWei(get_bal(w3, address, BUSD_ADDRESS), 'ether')} ")
print(f"{address} bnb bal:{get_eth_bal(w3, address)} ")

w3 = Web3(Web3.HTTPProvider(RPC_OP))
print(f"{address} op eth bal:{get_eth_bal(w3, address)} ")


