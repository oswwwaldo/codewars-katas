function findOdd(arrInt) {
  const dictionary = {};
  
  for (let i = 0; i < arrInt.length; i++) {
    const num = arrInt[i];
    if (dictionary[num]) {
      dictionary[num] += 1;
    } else {
      dictionary[num] = 1;
    }
  }
​
  const entries = Object.entries(dictionary);
  for (let i = 0; i < entries.length; i++) {
    const [key, value] = entries[i];
    if (value % 2 !== 0) {
      return Number(key);
    }
  }
}