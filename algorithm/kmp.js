var kmp = function (string, pattern) {
  var s_Len = string.length,
    p_Len = pattern.length;
  if (!p_Len) return 0;
  var lps = calcLps(pattern);
  for (var s = 0, p = 0; s < s_Len; ) {
    if (string[s] == pattern[p]) {
      s++, p++;
      if (p == p_Len) return s - p;
    } else {
      if (p > 0) p = lps[p - 1];
      else s++;
    }
  }
  return -1;
};

function calcLps(s) {
  const lps = new Array(s.length).fill(0);
  let prefix = 0,
    suffix = 1;
  while (suffix < s.length) {
    if (s[prefix] === s[suffix]) {
      // Update LPS value for current suffix position
      lps[suffix] = prefix + 1;
      // Move both pointers forward
      prefix++;
      suffix++;
    } else {
      // If characters don't match
      if (prefix === 0) {
        // If prefix pointer is at the start, set LPS value for suffix to 0
        lps[suffix] = 0;
        suffix++;
      } else {
        // Update prefix pointer based on previously computed LPS values
        prefix = lps[prefix - 1];
        //since element till prefix-1 & suffix-1 is equal then we go in
        //prefix longest pref=suffix before current in prefex & go to next element
        //when 2nd D & C is not equal,find longest prefix that is suffix that
        //is at index 1 AB
        //ABCDEABDE
      }
    }
  }

  // Return the last element of the LPS array
  return lps;
}

console.log(kmp("ABABDABACDABABC", "ABABC"));
