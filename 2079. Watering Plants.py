class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water,cost=capacity,0
        for i,plant in enumerate(plants):
            if plant>water:
                cost+=2*i
                water=capacity
            water-=plant
            cost+=1
        return cost
