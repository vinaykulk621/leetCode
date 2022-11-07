/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    answer=[]
    for(i=1;i<=n;i++){
        outPut=""
        if(i%3==0 && i%5==0){
            outPut="FizzBuzz"
        }
        else if(i%3==0){
            outPut="Fizz"
        }
        else if(i%5==0){
            outPut="Buzz"
        }
        else{
            outPut=i.toString()
        }
        answer.push(outPut)
    }
    return answer
};
