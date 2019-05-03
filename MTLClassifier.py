import tensorflow as tf
import tensorflow_hub as tfhub
import encoder_large as use
import numpy as np

HVEC = [512, 256]
LRATE = 0.001
STEPS = 50
EPOCHS = 5

def create_input_fn(df, target_column_label, epochs=None, shuffle=True):
    # Epochs=None means unlimited epochs
    return tf.estimator.inputs.pandas_input_fn(df, df[target_column_label], num_epochs=epochs, shuffle=shuffle)

class MTLClassifier:
    def build_dnn_classifier(self, hidden_vec, lrate):
        embedded_text_feature_column = tfhub.text_embedding_column(
            key=self.text_column_label, 
            module_spec=self.encoder_module,
            trainable=True)

        return tf.estimator.DNNClassifier(
            model_dir="models/v1",
            hidden_units=hidden_vec,
            feature_columns=[embedded_text_feature_column],
            n_classes=self.n_classes,
            optimizer=tf.train.AdagradOptimizer(learning_rate=lrate))

    def run(self):
        estimator = self.build_dnn_classifier(HVEC, LRATE)

        estimator.train(input_fn=create_input_fn(self.train_df, self.target_column_label), steps=STEPS)
        train_eval_result = estimator.evaluate(input_fn=self.predict_train_input_fn)
        test_eval_result = estimator.evaluate(input_fn=self.predict_test_input_fn)

        print("-----------------------------------")
        print("Training set accuracy: {accuracy}".format(**train_eval_result))
        print("Test set accuracy: {accuracy}".format(**test_eval_result))
        print("-----------------------------------")

    def __init__(self, train_df, test_df, n_classes, target_column_label, text_column_label):
        #self.encoder_module = "https://tfhub.dev/google/nnlm-en-dim128-with-normalization/1"
        self.encoder_module = use.URL
        self.train_df = train_df
        self.test_df = test_df
        self.n_classes = n_classes
        self.target_column_label = target_column_label
        self.text_column_label = text_column_label
        # Prediction on the whole training set.
        self.predict_train_input_fn = tf.estimator.inputs.pandas_input_fn(
            train_df, train_df[target_column_label], num_epochs=1, shuffle=False)
        # Prediction on the test set.
        self.predict_test_input_fn = tf.estimator.inputs.pandas_input_fn(
            test_df, test_df[target_column_label], num_epochs=1, shuffle=False)