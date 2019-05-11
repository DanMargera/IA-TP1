# Experimental Setup

## Network Configuration
We use the sentence embeddings from the Universal Sentence Encoder[1] as text features and train a simple multi layer perceptron (DNNClassifier from tensorflow) to classify the data as Negative, Neutral, Positive.

Our network has two hidden layers with [512, 256] nodes, we use Adagrad Optimizer with a learning rate of 0.001.

## Data Sets
Total of 1028 tweets classified manually:
 - Positive: 317
 - Neutral: 584
 - Negative: 127

We balanced the dataset by selecting randomly 127 tweets of each class.

Then we divide this balanced dataset into a train and a test sets:

Train set has 324 tweets, 108 of each class.\
Test set has 57 tweets, 19 of each class(17.59% holdout).

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
