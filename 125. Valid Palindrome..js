/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    if(s===" "){
        return true
    }
    const original = s.split("").join("").replaceAll(/[^0-9a-z]/gi, '').toLowerCase()
    const palindrome = s.split("").reverse().join("").replaceAll(/[^0-9a-z]/gi, '').toLowerCase()
    return (original===palindrome)
};
