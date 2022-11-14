/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    if(word.length==0){
        return word
    }
    let i=0,flag=0
    for(;i<word.length;i++){
        if(word[i]==ch){
            flag=1
            break
        }
    }
    if(flag==0){
        return word
    }
    word=word.split("")
    first=word.slice(0,i+1).reverse().concat(word.slice(i+1))
    return first.join("")
};
