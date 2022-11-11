/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    for(i=nums.length;i>=0;--i){
        if(nums[i]!=0){
            continue
        }
        nums.push(nums.splice(i,1))
    }
};
