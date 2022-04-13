'''
James Halladay
Copyright (c) 2021

Multi-Layer Grid (MLG) Neural Network
    An improvement on the Feed-Forward Neural Network Multi-Layer Perceptron (MLP) model.
    The MLP model is a simple feed-forward neural network that is trained to classify
        the input data into a set of categories. 
    The MLG model is an MLP where the individual perceptrons would be overlayed onto a grid
        in n space such that each neuron sits at the intersection of integer valued grid lines
    Each grid line represents a shared parameter between each perceptron sharing a coordinate on 
        that axis.
    Each parameter can represent either a single parameter of the MLP. This we define as an Additive 
        shared parameter.
    Each parameter can multipy against another parameter of the MLP. This we define as a Multiplicative
        shared parameter.
    Additive parameters give each perceptron connected to it a shared parameter.
    Multiplicative parameters give each perceptron connected to a parameter proportional to a shared parameter.

The shape of a MLP should be defined by the number of perceptrons in each layer. 
Let (N, M) be the shape of the MLP. Let n be the number of shared parameters in the model
    and let m be the number of shared parameters between layers and n-m be the number of
    shared parameters in each layer. If there are atleast n-m

Each perceptron has an integer valued coordinate in n space where the first n-m coordinates are the 
    shared parameters in its layer, and the last m coordinates are the shared parameters with each layer.

    Example: Let p1 and p2 be perceptrons in a 3 dimensional grid where 1 parameter is shared with every layer
        and 2 parameters are shared in their respective layers such that p1=(x,y,z) and p2=(x',y,z'). Then p1 
        and p2 share the same parameter represented by the second coordinate, but have different parameters for 
        their first and third coordinates.

'''