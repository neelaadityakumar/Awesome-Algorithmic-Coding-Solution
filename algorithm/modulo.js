//Binary exponentiation
function modPow(base, power, mod) {
  let result = 1;
  base = base % mod;

  while (power > 0) {
    if (power % 2 === 1) {
      result = (result * base) % mod;
    }
    base = (base * base) % mod;
    power = Math.floor(power / 2);
  }

  return result;
}
//Fermat little theorem ,mode inverse
// 1/2%mod= 2**-1%mod= modInverse(2,mod)
function modInverse(base, mod) {
  return modPow(base, mod - 2, mod);
}
