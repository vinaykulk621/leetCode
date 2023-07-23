/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let oldInit=init
    const increment=()=>{
        return ++oldInit 
    }
    const decrement=()=>{
        return --oldInit    
    }
    const reset=()=>{
        return (oldInit=init)
    }
    return {increment,decrement,reset}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
