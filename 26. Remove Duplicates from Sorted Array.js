/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if(nums.length==1){ return nums}

    originalLen=nums.length

    for(let i=0;i<nums.length-1;i++){
        if(nums[i]==nums[i+1]){
            nums.splice(i,1)
            i==0 ? i=i-1 : i=i-2
        }
    }

    ans=nums.length

    for(let i=0;i<originalLen-nums.length;i++){
        nums.push(101)
    }

    return ans
};
