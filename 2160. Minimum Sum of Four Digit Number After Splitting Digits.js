/**
 * @param {number} num
 * @return {number}
 */
 var minimumSum = function(num) {
    const numArray = num.toString().split('');
    const n = numArray.length;
    let result = 0;
    numArray.sort();
    for (let i = 0; i < n / 2; i++) {
        const pair = numArray[i] + numArray[n - 1 - i];
        result += +pair;
    }
    return result;
}
