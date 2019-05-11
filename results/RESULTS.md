# Experimental Setup

## Network Configuration
We use the sentence embeddings from the Universal Sentence Encoder[1] as text features and train a simple multi layer perceptron (DNNClassifier from tensorflow) to classify the data as Negative, Neutral, Positive.

Our network has two hidden layers with [512, 256] nodes, we use Adagrad Optimizer with a learning rate of 0.001.

## Data Sets
Total of 1028 tweets classified manually:
 - Positive: 317
 - Neutral: 584
 - Negative: 127

Then we divide this into balanced datasets to train/test:

Train set has 324 tweets, 108 of each class(selected randomly).\
Test set has 59 tweets(selected randomly from the remaining pool of tweets):
 - Positive: 20
 - Neutral: 20
 - Negative: 19
 
 (The slight unbalance on test set does not make a difference.)

## Results
### Train Set
We trained the model for 50 steps using a batch size of 128, this means roughly 19 epochs of training.\
Accuracy: 0.9135802388191223

### Test Set
Accuracy: 0.8644067645072937

Confusion matrix:\
![cm-abs](Test%20set%20confusion%20matrix(abs).png)

Confusion matrix (normalized):\
![cm](Test%20set%20confusion%20matrix.png)
