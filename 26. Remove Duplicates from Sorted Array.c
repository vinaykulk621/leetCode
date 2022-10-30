

int removeDuplicates(int* nums, int numsSize){
    int j,r,k=numsSize;
    if(numsSize==1)
        return 1;
    for(int i=0;i<numsSize;i++){
        if((i+1)==numsSize)
            break;
        if(nums[i]==nums[i+1]){
            for(j=i+1;j<numsSize;j++){
                nums[j-1]=nums[j];
                r=j;
            }
            nums[r]=101;
            numsSize-=1;
            if(nums[i]==nums[i+1]){
                i=i-1;
            }
            if(nums[i+1]==101)
                break;
        }
    }
    return numsSize;
}
