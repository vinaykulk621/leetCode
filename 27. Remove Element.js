/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    if(nums.length==0){
        return nums
    }
    let originalLen=nums.length
    nums.sort((a,b)=>a-b);
    for(let i=0;i<nums.length;i++){
        if(nums[i]==val){
            nums.splice(i,1)
            i==0 ? i=i-1 : i=i-2
        }
        if(nums[i]>val){
            break;
        }
    }

    const ans=nums.length

    for(let i=0;i<originalLen-ans;i++){
        nums.push(51)
    }
    return ans
};
