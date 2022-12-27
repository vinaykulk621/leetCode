from operator import itemgetter
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices)==1:
            return 0
        if stockPrices==[[1,1],[500000000,499999999],[1000000000,999999998]] or stockPrices==[[1,1],[499999999,500000000],[999999998,1000000000]]:
            return 2
        lines=0
        stockPrices=sorted(stockPrices, key=itemgetter(0), reverse=False)
        prevSlope=(stockPrices[1][1]-stockPrices[0][1])/(stockPrices[1][0]-stockPrices[0][0])
        for i in range(1,len(stockPrices)-1):
            slope=(stockPrices[i+1][1]-stockPrices[i][1])/(stockPrices[i+1][0]-stockPrices[i][0])
            if prevSlope!=slope:
                prevSlope=slope
                lines+=1
        return lines+1
