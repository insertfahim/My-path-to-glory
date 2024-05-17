class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i],speed[i]) for i in range(len(position))]
        fleets = currtime = 0
        for distance,car_speed in sorted(pairs,reverse=True):
            destination_time = (target-distance)/car_speed
            if destination_time>currtime:
                fleets+=1
                currtime=destination_time
        return fleets