/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    let n,ans
    for(n=0;n<=s.length;n++){
        if(ans==goal){
            return true
        }
        ans=s.slice(n) + s.slice(0, n);
    }
    return false
};
