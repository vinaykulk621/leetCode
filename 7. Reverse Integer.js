/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let final= parseInt(x.toString().split("").reverse().join(""))
    x<0 ? final=-final : final=+final
    if(-Number(2**31)<=final && final<=(Number(2**31)-1)){
        return final;
    }
    return 0
};
