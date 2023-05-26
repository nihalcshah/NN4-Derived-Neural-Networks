# Derived Neural Networks
## Generations and development of ensemble Neural Networks as a puzzle for the Artificial Intelligence 2 course (319967) at TJHSST

**Imagine a situation where you were given two separate neural networks and the desired output.**
 The purpose of this code is to assemble conglomerate inputs from fully connected NNs and output the aggregate results.


This Repository builds upon the techniques of 
  - NN BP-1 and 2: Neural Networks with Derived Back Propagation 
  - NN1: Feed Forward Neural Networks

<img src="https://www.researchgate.net/publication/273153116/figure/fig2/AS:267488797655114@1440785707994/Multi-layered-perceptron-feed-forward-neural-network-used-to-predict-the-binding_Q640.jpg"> </img>
***Figure 1. Ensemble Networks Example***

```{python}
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
```

