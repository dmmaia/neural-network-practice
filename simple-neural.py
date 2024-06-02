import numpy, random, os

learning_rate = 1
bias = 1
weights = [random.random(), random.random(), random.random()]

print(weights)

def Perceptron(input1, input2, output):
    outputP = input1 * weights[0] + input2 * weights[1] + bias*weights[2]

    outputP = 1/(1+numpy.exp(-outputP))

    error = output - outputP

    weights[0] += error * input1 * learning_rate
    weights[1] += error * input2 * learning_rate
    weights[2] += error * bias * learning_rate

for i in range(50) :
   Perceptron(1,1,1)
   Perceptron(1,0,1)
   Perceptron(0,1,1)
   Perceptron(0,0,0)

print(weights)

x = int(1)
y = int(0)
outputP = x*weights[0] + y*weights[1] + bias*weights[2]
if outputP > 0 :
   outputP = 1
else :
   outputP = 0
print(x, "or", y, "is : ", outputP)
