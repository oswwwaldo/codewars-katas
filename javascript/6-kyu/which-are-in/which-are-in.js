function inArray(array1,array2){
  
  let matchingResults = [];
  
  for(const str1 of array1) {
    for(const str2 of array2) {
      if (str2.includes(str1)) {
        matchingResults.push(str1);
      }
    }
  }
  
  return [... new Set(matchingResults.sort())];
}