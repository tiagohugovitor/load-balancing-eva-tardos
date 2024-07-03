import os
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from loadBalancingDynamicProgramming import loadBalancingDynamicProgramming
from loadBalancingGreedy import loadBalancingGreedy

def generateRandomJobTimes(jobs):
    jobTimes = [random.randint(1, 5) for _ in range(jobs)]
    return jobTimes

# Define input size
machines = 3
jobs = 30
inputList = list(range(1, jobs + 1))

# Create directory for results if it doesn't exist
resultsDir = 'results'
os.makedirs(resultsDir, exist_ok=True)
dynamicProgrammingExecutionTime = [0] * jobs
greedyExecutionTime = [0] * jobs
rightAnswers = 0
worstError = 0
for i in inputList:

    jobTimes = generateRandomJobTimes(i)
    start = time.time()
    optimalAnswer = loadBalancingDynamicProgramming(machines, jobTimes)
    end = time.time()
    dynamicProgrammingExecutionTime[i-1] = end - start

    start = time.time()
    approximateAnswer = loadBalancingGreedy(machines, jobTimes)
    end = time.time()
    greedyExecutionTime[i-1] = end - start

    if optimalAnswer == approximateAnswer:
        rightAnswers += 1
    
    else:
        error = approximateAnswer / optimalAnswer
        if error > worstError:
            worstError = error

    data = {
        'Input size': inputList,
        'Dynamic Programming': dynamicProgrammingExecutionTime,
        'Greedy': greedyExecutionTime,
    }

    df = pd.DataFrame(data)

    dfName = f'{resultsDir}/dataframe-{machines}-machines-{jobs}-jobs.xlsx'
    df.to_excel(dfName, index=False)


print('Taxa de acerto: ', (rightAnswers * 100) / jobs)
print('Pior erro: ', worstError)

plt.figure(figsize=(10, 5))
plt.plot(inputList, dynamicProgrammingExecutionTime, label='Dynamic Programming')
plt.plot(inputList, greedyExecutionTime, label='Greedy')
plt.xlabel('Input size')
plt.ylabel('Time (s)')
plt.title('Algorithms execution time')
plt.legend()
plt.grid(True)

figName = f'{resultsDir}/figure-{machines}-machines-{jobs}-jobs.png'
plt.savefig(figName)

plt.show()