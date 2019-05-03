import tensorflow as tf
import tensorflow_hub as tfhub

URL = "https://tfhub.dev/google/universal-sentence-encoder-large/3"

def load_module():
    return tfhub.Module(URL)

def create_embeddings(module, sentences):
    with tf.Session() as session:
        session.run([tf.global_variables_initializer(), tf.tables_initializer()])
        message_embeddings = session.run(module(sentences))
        return message_embeddings