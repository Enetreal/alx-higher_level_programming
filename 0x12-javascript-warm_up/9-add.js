#!/usr/bin/node

// Define a function 'add' that takes two parameters 'a' and 'b' and returns the sum
function add(a, b) {
    return a + b;
  }
  
  // Extract command line arguments and convert them to numbers
  const arg1 = Number(process.argv[2]);
  const arg2 = Number(process.argv[3]);
  
  // Call the 'add' function with the provided arguments and log the result
  console.log(add(arg1, arg2));