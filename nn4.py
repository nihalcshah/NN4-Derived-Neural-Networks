import sys; args = sys.argv[1:]
squaringweights = open(args[0], "r").read().splitlines()
# squaringweights = [w.split(" ") for w in squaringweights]
# squaringweights = [[float(w) for w in ws] for ws in squaringweights]

# args = ["test.txt"]

def processWeightsfile(weights):
    weights = [w for w in weights if w[0].isdigit() or w[0] == "-" or w[0] == "."]
    weights = [w.replace(",","").split(" ") for w in weights]
    weights = [[float(w) for w in ws if w!="" and w[-1].isdigit()] for ws in weights]
    return weights

squaringweights = processWeightsfile(squaringweights)

import math, random
def createNodes(weights):
    weightLengths = [len(weights[i]) for i in range(len(weights))][::-1]
    previousnodelength = weightLengths[0]
    nodeslengths = [previousnodelength]
    for i in range(len(weightLengths)):
        nodeslengths.append(weightLengths[i]//previousnodelength)
        previousnodelength = weightLengths[i]//previousnodelength
    nodelengths = nodeslengths[::-1]
    nodes = [[0]*nodelengths[i] for i in range(len(nodelengths))]
    return nodes

nodes = createNodes(squaringweights)[:-1]

for i in range(len(nodes)):
    nodes[i]+=nodes[i]
nodes+=[[0],[0]]
nodes[0] = [0,0,0]
for i in range(len(squaringweights)):
    squaringweights[i]+=squaringweights[i]

# print("Weight Counts: " + " ".join([str(len(i)) for i in squaringweights]))

# print(nodes)
# print(squaringweights)

# def arrangeWeights(weights, baseNodes):
#     # baseNodes.append(len())
#     newWeights = []
#     for layerIndex in range(1, len(baseNodes)):
#         inputCount = len(baseNodes[layerIndex-1])
#         outputCount = len(baseNodes[layerIndex])
#         copiedWeightLayer = weights[layerIndex-1][:]
#         additionaladder = 0
#         for i in range(outputCount):
#             if i<outputCount/2:
#                 ind = i*(inputCount//2)+(inputCount//2)+additionaladder
#                 for j in range(inputCount//2):
#                     # print(ind+j+additionaladder)
#                     copiedWeightLayer.insert(ind+j, 0)
#                 additionaladder+=inputCount//2
#             else:
#                 ind = i*(inputCount//2)+additionaladder
#                 for j in range(inputCount//2):
#                     copiedWeightLayer.insert(ind+j, 0)
#                 additionaladder+=inputCount//2
#         weights[layerIndex-1] = copiedWeightLayer    

#     return weights

def arrangeWeights(weights, baseNodes):
    newweights = []
    #first layer connections
    firstlayer = []
    for w in range(len(weights[0])):
        if w<len(weights[0])//2:
            firstlayer.append(weights[0][w])
            if w%2==0:
                firstlayer.append(0)
        else:
            if w%2==0:
                firstlayer.append(0)
            firstlayer.append(weights[0][w])
    newweights.append(firstlayer)
    
    #Future Layers
    for layerIndex in range(1, len(weights)-1):
        inputCount = len(baseNodes[layerIndex])
        outputCount = len(baseNodes[layerIndex+1])
        newlayer = []
        mcount = len(baseNodes[layerIndex])//2
        for w in range(len(weights[layerIndex])):
            if w<len(weights[layerIndex])//2:
                newlayer.append(weights[layerIndex][w])
                if (w+1)%mcount==0 and w!=0:
                    newlayer+=[0]*mcount
            else:
                if w%mcount==0:
                    newlayer+=[0]*mcount
                newlayer.append(weights[layerIndex][w])
        newweights.append(newlayer)
    
    #Second to last layer
    newweights.append(weights[-1]) #The last layer has not been added to weights yet

    return newweights

newWeights = arrangeWeights(squaringweights, nodes)

# newWeights.append(squaringweights[-1])
newWeights.append([(1+math.e)/(2*math.e)])


print("Layer Counts: " + " ".join([str(len(i)) for i in nodes]))
for i in newWeights:
    print(i)
#Nihal Shah, period 6, 2023