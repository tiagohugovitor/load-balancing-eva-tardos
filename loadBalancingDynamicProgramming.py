def loadBalancingDynamicProgramming(machines, tasks):
    dp = {}
    dp[(0,) * machines] = 0

    for task in tasks:
        newDp = {}
        for state in dp:
            for i in range(machines):
                newState = list(state)
                newState[i] += task
                newState = tuple(newState)
                newDp[newState] = max(newState)
        dp = newDp

    return min(max(state) for state in dp.keys())
