import pickle
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

__mental_health_classifier = None
__embedding = None
def load_artifacts():
    print('Loading Artifacts Started')
    global __mental_health_classifier
    global __embedding

    with open('application/artifacts/model_mha.pkl', 'rb') as f:
        __mental_health_classifier = pickle.load(f)

    __embedding = tf.keras.models.load_model('application/artifacts/embedding_model.h5',custom_objects={'KerasLayer': hub.KerasLayer})

    print('Loading Artifacts complete')

def text_preprocessor(text):
    text_input = [text]
    user_embeddings = __embedding.predict(text_input)

    print('Embedding Creation Complete')

    return user_embeddings

def prediction(text):
    text_input = text_preprocessor(text)
    result = int(__mental_health_classifier.predict(text_input))

    label = {0: 'Normal', 1: 'Depression', 2: 'Suicidal', 3: 'Anxiety', 4: 'Bipolar', 5: 'Stress', 6: 'Personality Disorder'}

    if result in list(label.keys()):
        return label[result]



if __name__ == '__main__':
    load_artifacts()
    result = prediction("I always feel sad. I am never happy")
    print(result)
    
