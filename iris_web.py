import streamlit as st
import pandas as pd
import warnings
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings("ignore")

st.write("""
# Predictor de flores
Esta app predice el tipo **Flor Iris** !
""")

st.sidebar.header('Parametros de entrada')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Selecciona los parametros')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Etiquetas')
st.write(iris.target_names)

st.subheader('Predicción')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Predicción de probabilidad')
st.write(prediction_proba)