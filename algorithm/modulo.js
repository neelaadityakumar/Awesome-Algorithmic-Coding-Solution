function modInverse(a, mod) {
  let result = 1;
  let power = mod - 2; // Fermat's: a^(mod-2) mod mod
  while (power > 0) {
    if (power % 2 === 1) result = (result * a) % mod;
    a = (a * a) % mod;
    power = Math.floor(power / 2);
  }
  return result;
}
