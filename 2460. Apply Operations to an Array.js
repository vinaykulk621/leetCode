/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
    if(nums.length==2 && nums[0]==0){
        temp=nums.shift()
        nums.push(temp)
        return nums
    }
    
    for(let i=0;i<nums.length;i++){
        if(nums[i]==nums[i+1]){
            nums[i]=nums[i]*2
            nums[i+1]=0
        }
    }
    
    let stack=[]

    for(let i=0;i<nums.length;i++){
        if(nums[i]!=0){
            stack.push(nums[i])
        }
    }

    const count=nums.length-stack.length
    
    for(let i=1;i<=count;i++){
        stack.push(0)
    }
    return stack
};
