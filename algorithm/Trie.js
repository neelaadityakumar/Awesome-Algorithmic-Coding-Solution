class TrieNode {
  constructor(child = {}, end = false) {
    this.child = child;
    this.end = end;
  }
}
var Trie = function () {
  this.root = new TrieNode();
};

Trie.prototype.insert = function (word) {
  let current = this.root;
  for (const char of word) {
    if (!current.child[char]) {
      current.child[char] = new TrieNode();
    }
    current = current.child[char];
  }

  current.end = true;
};

Trie.prototype.search = function (word) {
  let current = this.root;
  for (const char of word) {
    if (!current.child[char]) {
      return false;
    }
    current = current.child[char];
  }

  return current.end;
};

Trie.prototype.startsWith = function (word) {
  let current = this.root;
  for (const char of word) {
    if (!current.child[char]) {
      return false;
    }
    current = current.child[char];
  }

  return true;
};

const word = "apple";
const prefix = "app";
var obj = new Trie();
obj.insert(word);
var param_2 = obj.search(word);
var param_3 = obj.startsWith(prefix);
console.log(`Search "${word}":`, param_2); // true
console.log(`Starts with "${prefix}":`, param_3); // true
console.log(`Search "app":`, obj.search(prefix)); // false
console.log(`Starts with "apple":`, obj.startsWith(word)); // true
console.log(`Search "banana":`, obj.search("banana")); // false
