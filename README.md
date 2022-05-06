# 深入分析NFT合约源码——以Surge Women为例


- Surge Women合约地址：0x0632aDCab8F12edD3b06F99Dc6078FE1FEDD32B0
- 智能合约源码：surge.sol
- tokenId: 1802
- opensea链接：https://opensea.io/assets/0x0632adcab8f12edd3b06f99dc6078fe1fedd32b0/1802
- token mint 交易链接：https://etherscan.io/tx/0xbede5e44cc631303a22d066cc269f989469742b5bb6d9a74185e146dab9211e4



问题1：NFT(non-fungible token)，即非同质化代币，如何理解“非同质化”？在代码层面如何实现的？

答：fungible中文意思是“可互换的”，可互换的东西是没有特殊性的，如果是独一无二的东西则具有了“不可互换的”属性。例如，1元钱的硬币和1元钱的纸钞则可以互换，虽然在形态上不同，但是在作为货币的属性上本质相同，都是代表1元。

至于如何编码实现，前面说了non-fungible的东西必须具备“独一无二”的属性，在编程领域什么东西独一无二呢？
答案很简单，就是唯一的id，用一个整数即可，在solidity中uint256能够表示的整数完全够用。

问题2：NFT的图片（或者音频、视频等）是怎样和智能中tokenId一一对应起来的？

图片等资源文件放在IPFS，智能合约中只存储每个token对应的IPFS上的URI即可。每个NFT项目有一个目录，目录下可以放很多资源文件，在构造合约的时候将目录在IPFS上的URI设置为baseURI，那么每个token的资源文件在IPFS的URI就确定了。例如，某个NFT项目在IPFS上总目录的URI为`ipfs://QmYVsw73haPgm9jK9BopsuKtzuxLANjYn75xeHLpht13D5`，tokenId为`1802`的token在IPFS上的URI则为`ipfs://QmYVsw73haPgm9jK9BopsuKtzuxLANjYn75xeHLpht13D5/1802`。



```py
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

```


打印的结果是：

```
Surge Women Passport
SURGE
ipfs://QmYVsw73haPgm9jK9BopsuKtzuxLANjYn75xeHLpht13D5/1802
```


但是从ipfs浏览器中的链接却是：`ipfs/Qmaseu2BbetLjA6eU7mQ2THEkjdBum5wq1EfuLAY2AoiEA/1802.png`


分析tokenURI函数的代码

```solidity
function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
    if (!_exists(tokenId)) revert URIQueryForNonexistentToken();

    // baseURI是目录的URI
    string memory baseURI = _baseURI();
    // 将目录的URI和tokenId拼接在一起就是token的URI
    return bytes(baseURI).length != 0 ? string(abi.encodePacked(baseURI, tokenId.toString())) : '';
}
```

而 _baseURI由 Surge合约重写了父合约的_baseURI函数。Surge合约在构造函数中设置了baseURI，也就是在构造合约时已经设置了baseURI

```
constructor(
    string memory _name,
    string memory _symbol,
    string memory _baseTokenURI,
    uint128 _price,
    address _receiver,
    uint256 _royalties
) payable ERC721A(_name, _symbol) {
    setBaseURI(_baseTokenURI);
    setPrice(_price);
    setRoyalties(_receiver, _royalties);
}
```



https://ipfs.io/ipfs/QmYVsw73haPgm9jK9BopsuKtzuxLANjYn75xeHLpht13D5

https://tth-ipfs.com/ipfs/QmYVsw73haPgm9jK9BopsuKtzuxLANjYn75xeHLpht13D5

