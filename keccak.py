import web3
from web3 import Web3


def main():
    ret = Web3.solidityKeccak(['address'], [Web3.toChecksumAddress("0xc3746825f13c07dcd7e6fdb9c0c80a9affb18952")])
    print(Web3.toHex(ret))
    ret = Web3.keccak(hexstr='0xc3746825f13c07dcd7e6fdb9c0c80a9affb18952')
    print(Web3.toHex(ret))
    
    pass

if __name__ == '__main__':
    main()
    