/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let final=s.split(" ").filter(e=>e)
    return final[final.length-1].length
};
