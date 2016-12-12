# machine learning and deep learning



## bayesClassification

It just a bayes classifier using python.
It is very convenient to code using Python for science calculation(than c++ =-=)



### test data
I use some data from UCI dataset.


It can be donwloaded from [UCI dataset] (https://archive.ics.uci.edu/ml/datasets/Census+Income).


After download it,put them into a file named dataset so that program can read data from it.


Havefun !


## decision tree 




## iris dataset for classification

just use deep learning for classification three classes of flowers from iris dataset
and you can get a proper result(accuracy:29/30) from testing, Before using code 
well ,some thing you should konw list below.

 - loss function: using cross entropy loss function to calculate the difference probability distribution between the prediction and the real label
 
 - classifier: using softmax function to get the probability of each class 

 - optimizier: using MSGD algorithm with momentum and learning rate decaying

 - training and testing dataset: 150 in all , 120 for training and the left for testing

 - activation function: ReLU function (I have tried to use tanh but the result was not great)

 - hidden units: The constrution of the neural network can be setted what as you like

## mnist dataset
The project mainly is used for handling image dataset,by using CNN neural network .
The nerual network(can also called by deep learning) has many layers that common used in this field.So you can learn many necessary tricks from the project if you want to be a data scientist(=-=)

The project has something you should know first listed below:

 - inference:the function aims to construte a graph layer by layer

 - layer: There are some layers like conv_layer , ReLU_layer , fully_connected_layer, maxpooling and softmax_layer and so on . You can know more from the code.
 
 - load data:Due to using MSGD ,you should get the samples by min_batch ,using next_batch() function to get data to feed the network for convenience 

 - others:others in the project are like iris project. so omit them here

## Others:
If have others things to upload here ,I will add their information immediately
