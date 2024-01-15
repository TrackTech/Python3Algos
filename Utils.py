def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    if jug1Capacity + jug2Capacity < targetCapacity:
        return False

    def dfs(x, y):
        if x + y == targetCapacity:
            return True

        visited.add((x, y))

        # Pour water from jug1 to jug2
        if x > 0 and (x - min(x, jug2Capacity - y), y + min(x, jug2Capacity - y)) not in visited:
            if dfs(x - min(x, jug2Capacity - y), y + min(x, jug2Capacity - y)):
                return True

        # Pour water from jug2 to jug1
        if y > 0 and (x + min(jug1Capacity - x, y), y - min(jug1Capacity - x, y)) not in visited:
            if dfs(x + min(jug1Capacity - x, y), y - min(jug1Capacity - x, y)):
                return True

        # Fill jug1
        if x < jug1Capacity and (jug1Capacity, y) not in visited:
            if dfs(jug1Capacity, y):
                return True

        # Fill jug2
        if y < jug2Capacity and (x, jug2Capacity) not in visited:
            if dfs(x, jug2Capacity):
                return True

        # Empty jug1
        if x > 0 and (0, y) not in visited:
            if dfs(0, y):
                return True

        # Empty jug2
        if y > 0 and (x, 0) not in visited:
            if dfs(x, 0):
                return True

        return False

    visited = set()
    return dfs(0, 0)

# Example usage:
jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4
print(canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))  # Output: True
