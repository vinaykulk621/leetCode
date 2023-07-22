/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const toBe=(anotherVal)=>{
        if(anotherVal===val){
            return true
        }
        throw new Error('Not Equal')
    }
    const notToBe=(anotherAnotherVal)=>{
        if(anotherAnotherVal!==val){
            return true
        }
        throw new Error('Equal')
    }
    return {toBe,notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
