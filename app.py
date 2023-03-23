import streamlit as st
import tensorflow as tf 
import numpy as np 
import streamlit.components.v1 as components
import glob,random
import pandas as pd
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding',False)

@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('./flower_sequential_model_trained.hdf5')
    return model

def predict_class(image,model):
    image=tf.cast(image,tf.float32)
    image=tf.image.resize(image,[180,180])
    image=np.expand_dims(image,axis=0)
    prediction = model.predict(image)
    return prediction

def load_random_image(label):
    directory="./flowers/"+label+"/"
    images=glob.glob(directory+"*.jpg")
    random_image=random.choice(images)
    return st.image(random_image)

def knowledge(label):
    df=pd.read_excel('flower-how-to-plant.xlsx',index_col=0)
    return st.markdown(df.loc[label]['description'])


def image_output(test_image):
    st.image(test_image,caption="input Image",width=400)
    pred=predict_class(np.asarray(test_image),model)
    class_names=['daisy','dandelion','rose','sunflower','tulip']
    result=class_names[np.argmax(pred)]
    output='The image is a '+result
    st.success(output)
    col1,col2,col3,col4=st.columns(4)
    with col4:
        google=st.button("check google")
    with col3:
        wiki=st.button('check wiki')
    with col1:
        more_image=st.button("Show me more image")
    with col2:
        know=st.button('how to plant')

    if google:
        components.iframe(f'https://www.google.com/search?igu=1&ei=&q={"how to plant "+result}',height=1000)
    if wiki:
        components.iframe(f'https://en.wikipedia.org/wiki/{result}',height=1000)
    if more_image:
        load_random_image(result)
    if know:
        knowledge(result)




model=load_model()
st.title('Flower Classifier')

file=st.file_uploader("upload an image of flower",type=['jpg','png','jpeg'])

if file is None:
    st.text('Waiting for upload....')
    test_image=st.camera_input("Take a picture")
    if test_image:
        test_image=Image.open(test_image)


else:
    slot=st.empty()
    slot.text('running inference')
    test_image=Image.open(file)

if test_image:
    st.write(test_image)
    image_output(test_image)


with st.sidebar:
    url_github="https://github.com/qian1170/test"
    st.markdown(f'''<a href={url_github}><button style="background-color:Gray;">Source Code</button></a>''',unsafe_allow_html=True)


    url_report="https://docs.google.com/document/d/1mKAfrd51Qv7BOzDAbNq1_LrJlrSQxs42XaSXJgHUpWE/edit"
    st.markdown(f'''<a href={url_report}><button style="background-color:Gray;">Report</button></a>''',unsafe_allow_html=True)


    url_chat="https://qian1170-chatbox-app-xnmjct.streamlit.app/"
    st.markdown(f'''<a href={url_chat}><button style="background-color:Pink;">Talk with An AI expert</button></a>''',unsafe_allow_html=True)

    st.success('Team members: WUQIAN MA,  ZINAN WANG')
    st.success('International Master Project')
    
