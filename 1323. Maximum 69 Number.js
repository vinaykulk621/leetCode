/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    if(num.length==1){ 
        return num 
    }

    num=num.toString().split("")
    for(let i=0;i<num.length;i++){
        if(num[i]==="6"){
            num[i]="9"
            break
        }
    }
    num=num.join("")
    return parseInt(num)
};
