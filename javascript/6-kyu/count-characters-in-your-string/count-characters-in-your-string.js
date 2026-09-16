function count(string) {
​
  result = {}
  
  const str = [...string].reduce((sum, value) => {
    result[value] = (result[value] || 0) + 1;
  }, "");
  
  return result;
}