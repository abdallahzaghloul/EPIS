import numpy as np #1
import pandas as pd #2
import plotly.graph_objects as go  #6
import plotly.express as px  #7
from plotly.subplots import make_subplots  #8
import plotly.figure_factory as ff #21
from PIL import Image
import streamlit as st

pd.set_option('mode.chained_assignment',None)

im = Image.open("EPIS.png")
image = np.array(im)
st.image(image)

st.markdown(" <center>  <h1> KPC (DRLG/WO) Drops Analysis </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
 
###

pd.set_option('mode.chained_assignment',None)
df = pd.read_excel('Book2.xlsx')
df.columns  = [i.replace(' ','_') for i in df.columns]
df.columns  = [i.upper() for i in df.columns]
Camp_List= list(df.columns)
Removed=['PASS','RIG_TYPE']
Camp_List.remove('RIG_TYPE')
Camp_List.remove('RIG_NAME')
#Camp_Count=[df['PASS'].sum()]
Camp_Count=[]
for i in range (1, len(Camp_List)):
  Camp_Count.append(df[Camp_List[i]].sum()) 
  fig = px.bar(x= Camp_List[1:i+1], y= Camp_Count,labels={ 'y':'Total Achievements'})
  fig.update_layout(title_text="Campaigns Progress", showlegend=False)
  st.plotly_chart(fig, use_container_width=True)
  st.write("This graph is hsowing Bla Bla Bla Bla Bla ")

# streamlit run "C:\\Users\\hp\\Desktop\\EPIS\\EDC_87\\EPIS_HOME.py" 


















