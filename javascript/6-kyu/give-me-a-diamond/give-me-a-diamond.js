function diamond(n) {
  let diamondResult = '';
  let diamondWidth = 0;
  let diamondPole = '';
  
  if (n % 2 === 0 | n < 0) { return null; }
  else {
    
    if (n === 1) {
      return '*\n';
    }
    
    // calculate number of steps down needed
    let steps = 0;
    for(let i = n; i > 1; i -=2 ) {
      steps++;
    }
    
    const iterations = steps;
    let spaces = steps + 1;
​
    for (let i = 0; i < iterations; i++) {
      if (i === 0) { diamondWidth = 1; }
      else { diamondWidth += 2; }
      if (spaces > 0) { spaces--; }
      
      Array(spaces).fill().forEach(() => {
        diamondResult += ' ';
      });
      
      Array(diamondWidth).fill().forEach(() => {
        diamondResult += '*';
      });
      
      diamondResult += '\n';
​
      if (i === steps - 1) {
        Array(n).fill().forEach(() => {
          diamondResult += '*';
        });
​
        diamondResult += '\n';