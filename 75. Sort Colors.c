void sortColors(int* nums, int numsSize){
    int r=0,w=0,b=0;
    for (int i = 0; i < numsSize; i++)
    {
        if(nums[i]==0){
            r++;
        }
        if(nums[i]==1){
            w++;
        }
        if(nums[i]==2){
            b++;
        }
    }
    for(int i=0;i<r;i++){
        if(i==numsSize){
            break;
        }
        nums[i]=0;
    }
    for(int i=0;i<w;i++){
        if(r==numsSize){
            break;
        }
        nums[r]=1;
        r++;
    }
    for(int i=0;i<b;i++){
        if(r==numsSize){
            break;
        }
        nums[r]=2;
        r++;
    }
}
