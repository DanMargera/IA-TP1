import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
import tensorflow as tf

def debug(*args, **kwargs):
    # Use this to disable/enable debugging
    if (True):
        print(*args, **kwargs)

def plot_confusion_matrix(df, target_column_label, estimator, predict_input_fn, labels):
    # Create a confusion matrix for df.
    with tf.Graph().as_default():
        predictions = [x["class_ids"][0] for x in estimator.predict(input_fn=predict_input_fn)]
        i = 0
        for p in predictions:
            if (p != df[target_column_label].iloc[i]):
                debug(i,df["text"].iloc[i],'pred:',p,'true:',df[target_column_label].iloc[i])
            i = i+1

        cm = tf.confusion_matrix(df[target_column_label], 
                                 predictions)
        with tf.Session() as session:
            cm_out = session.run(cm)

    debug(cm_out)
    # Normalize the confusion matrix so that each row sums to 1.
    cm_out = cm_out.astype(float) / cm_out.sum(axis=1)[:, np.newaxis]

    hmap = sns.heatmap(cm_out, annot=True, cbar=False, xticklabels=labels, yticklabels=labels)
    hmap.yaxis.set_ticklabels(hmap.yaxis.get_ticklabels(), rotation=0, ha='right')
    plot.xlabel("Predicted")
    plot.ylabel("Class")
    plot.subplots_adjust(left=0.21, bottom=0.15, right=0.87)
    plot.show()