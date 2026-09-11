function setAlarm(employed, vacation){
  
  if (employed) {
    if (!vacation) {
      return true;
    }
  }
  
  return false;
​
}