function doubleChar(str) {
  let output = "";
​
  for (let i = 0; i < str.length; i++) {
    output += str[i];
    output += str[i];
  }
  return output;
}
​