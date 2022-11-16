/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let low=1
    let high=n
    while(low<=high){
        mid=Math.floor(low+(high-low)/2)
        answer=guess(mid)
        if(answer==0){
            return mid
        }
        else if(answer<0){
            high=mid-1
        }
        else{
            low=mid+1
        }
    }
    return -1
};
