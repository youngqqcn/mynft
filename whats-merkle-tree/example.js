const { MerkleTree } = require('merkletreejs')
const SHA256 = require('crypto-js/sha256')


// 求
const leaves = ['a', 'b', 'c'].map(x => SHA256(x))
ha = SHA256('a')
hb = SHA256('b')
hc = SHA256('c')
console.log(ha.toString())
console.log(hb.toString())
console.log(hc.toString())

// 将a，b的hash连接在一起
hab = SHA256( ha.concat(hb) )
console.log(hab.toString())

// merkle root
habc = SHA256( hab.concat(hc) )
console.log(habc.toString())


const tree = new MerkleTree(leaves, SHA256)
console.log('-----------------------------')
console.log(tree.toString())

const root = tree.getRoot().toString('hex')
const leaf = SHA256('a')
const proof = tree.getProof(leaf)
console.log(tree.verify(proof, leaf, root)) // true


const badLeaves = ['a', 'x', 'c'].map(x => SHA256(x))
const badTree = new MerkleTree(badLeaves, SHA256)
const badLeaf = SHA256('x')
const badProof = tree.getProof(badLeaf)
console.log(tree.verify(badProof, leaf, root)) // false
