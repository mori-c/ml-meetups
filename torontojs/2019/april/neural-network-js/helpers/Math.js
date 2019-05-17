const nrand = require('gauss-random')

// Samples the standard normal distribution, with 0 mean and unit standard
// deviation.
window.Math.nrand = nrand;

// Our sigmoid function that takes in an number and returns a number between 0
// and 1.
window.Math.sigmoid = function ( x ) {
  return 1 / (1 + Math.exp((-x)));
}

// Calculate the derivative sigmoid
window.Math.derivSigmoid = function ( x ) {
  let fx = window.Math.sigmoid(x);
  return fx * (1 - fx);
}

// Mean Squared Error calculation on two arrays of the same shape. (n x 1)
window.Math.meanSquaredError = function ( answers, predictions ) {
  if (answers.length !== predictions.length) {
    throw new Error('array length mismatch');
  }

  let sum = 0;

  for (let i = 0; i < answers.length; i += 1) {
    // (a - p)^2
    sum += Math.pow(answers[i] - predictions[i], 2);
  }

  return (1 / answers.length) * sum;
}
