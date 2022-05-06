from web3 import Web3
import json

# https://etherscan.io/tx/0xbede5e44cc631303a22d066cc269f989469742b5bb6d9a74185e146dab9211e4
# https://mainnet.infura.io/v3/8a264f274fd94de48eb290d35db030ab
# contract address is 0x0632aDCab8F12edD3b06F99Dc6078FE1FEDD32B0 

from web3 import Web3
my_provider = Web3.HTTPProvider('https://mainnet.infura.io/v3/8a264f274fd94de48eb290d35db030ab')
w3 = Web3(my_provider)

def main():
    
    contract_address = '0x0632aDCab8F12edD3b06F99Dc6078FE1FEDD32B0'
    contract_abi = json.load(open('surge.abi', 'r'))
    # print(contract_abi)

    mycontract = w3.eth.contract(address=contract_address, abi=contract_abi)
    name = mycontract.functions.name().call()
    print(name)

    symbol = mycontract.functions.symbol().call()
    print(symbol)

    tokenURI = mycontract.functions.tokenURI(1802).call()
    print(tokenURI)

    pass

if __name__ == '__main__':
    main()
    