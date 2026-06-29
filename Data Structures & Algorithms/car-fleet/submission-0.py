class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i],speed[i]))
        pos_speed = sorted(pos_speed)
        print(pos_speed)
        stack = []
        for pos in reversed(pos_speed):
            time = (target - pos[0])/pos[1]
            print(pos)
            print(time)
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        return len(stack)