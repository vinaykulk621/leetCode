/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    nums.sort()
    i=0
    while(i<nums.length){
        if(nums[i]!=nums[i+1]){return nums[i]}
        i=i+2
    }
};
