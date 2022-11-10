/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
    if(s.length==1) {
        return s
    }
   
    s=s.split("")
    for(let i=0;i<s.length;i++){
        if(s[i]==s[i+1]){
            s.splice(i,2)
            i==0 ? i=i-1 : i=i-2
        }
    }
    return s.join("")
};
