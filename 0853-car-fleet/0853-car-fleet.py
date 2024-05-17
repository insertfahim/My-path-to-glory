class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[(position[i],speed[i]) for i in range(len(position))]
        fleets = curtime = 0
        for distance,car_speed in sorted(pairs,reverse=True):
            destination_time = (target-distance)/car_speed
            if curtime<destination_time:
                fleets+=1
                curtime = destination_time
        return fleets
        