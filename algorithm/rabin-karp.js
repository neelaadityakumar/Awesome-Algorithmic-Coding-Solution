// Function to implement Rabin-Karp algorithm for string searching
function rabinKarp(text, pattern) {
  const prime = 101; // A prime number used for hashing

  // Function to calculate the hash value of a string
  function calculateHash(str, length) {
    let hash = 0;
    for (let i = 0; i < length; i++) {
      hash += str.charCodeAt(i) * Math.pow(prime, i);
    }
    return hash;
  }

  // Function to re-calculate the hash value based on
  //the rolling hash technique
  function recalculateHash(oldHash, oldIndex, newIndex, patternLength) {
    let newHash = oldHash - text.charCodeAt(oldIndex); //-num*101^0
    newHash /= prime; //subtract one power from every sum of power of prime
    newHash += text.charCodeAt(newIndex) * Math.pow(prime, patternLength - 1);
    return newHash;
  }

  const textLength = text.length;
  const patternLength = pattern.length;
  const patternHash = calculateHash(pattern, patternLength);
  let textHash = calculateHash(text, patternLength);

  const indices = []; // Array to store the indices of pattern occurrences

  // Iterate through the text to find pattern matches
  for (let i = 0; i <= textLength - patternLength; i++) {
    if (
      textHash === patternHash &&
      text.substring(i, i + patternLength) === pattern
    ) {
      // If the hash values match and substring also matches, add index to the result
      indices.push(i);
    }

    // Recalculate hash value for the next window
    if (i < textLength - patternLength) {
      textHash = recalculateHash(textHash, i, i + patternLength, patternLength);
    }
  }

  return indices;
}

// Example usage:
const text = "AABAACAADAABAABA";
const pattern = "AABA";
console.log("Indices of pattern occurrences:", rabinKarp(text, pattern));
