function squareSum(numbers){
  let result = 0;
  
  for(const number of numbers) {
    result = (number * number) + result;
  }
  
  return result;
}