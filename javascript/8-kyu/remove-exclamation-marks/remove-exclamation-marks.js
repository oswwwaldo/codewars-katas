function removeExclamationMarks(s) {
  let output = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] != "!") {
      output += s[i];
    }
  }
  return output;
}