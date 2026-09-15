function toWeirdCase(string){
  // "Weird string case"
  
  let result = "";
  let space = " ";
  let words = string.split(" ");
  
  // ["Weird", "string", "case"]
  
  words.forEach((word, i) => {
    word.split("").forEach((char, j) => {
      // ["w", "e", "i", "r", "d"]
      
      if (j % 2 == 0) {
        result += char.toUpperCase();
      } 
      else {
        result += char.toLowerCase();
      }
      
      // Add a space at the end of each word, check if the word is the last in string
      if (j === word.length - 1 && i != words.length - 1) {
        result += `\u0020`;
      }
    })
  });
  
  return result;
}