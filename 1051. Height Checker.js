/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    let expected=[...heights]
    expected.sort((a,b)=>a-b)
    let count=0
    for(let i=0;i<heights.length;i++){
        heights[i]!=expected[i] ? count+=1 : count+=0
    }
    return count
};
