/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    s=s.split("")
    for(let i=0;i<s.length-1;i++){
        if(s[i].toLowerCase()==s[i+1].toLowerCase()){
            if(s[i]!==s[i+1]){
                s.splice(i,2)
                i=-1
            }
        }
    }
    return s.join("")
};
