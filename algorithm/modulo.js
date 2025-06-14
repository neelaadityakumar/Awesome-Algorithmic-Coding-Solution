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

function modPow2(base, power, mod) {
  if (power == 0) return 1 % mod;
  let result = power(base, power / 2, mod);
  result = (result * result) % mod;
  if (power % 2 == 1) result = (result * base) % mod;
  return result;
}

//Fermat little theorem ,mode inverse
// 1/2%mod= 2**-1%mod= modInverse(2,mod)
function modInverse(base, mod) {
  return modPow(base, mod - 2, mod);
}

function modSub(a, b, mod) {
  return ((a % mod) - (b % mod) + mod) % mod;
}
