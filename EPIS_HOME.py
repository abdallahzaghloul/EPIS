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
 
df = pd.read_excel("Book1.xlsx")
df.columns  = [i.replace(' ','_') for i in df.columns]
df.columns  = [i.upper() for i in df.columns]
for i in ['DESCRIPTION','LOCATION']:
    df[i]= df[i].str.upper().str.replace(' ', '_')
Fail_Pass = {0:'Pass',1:'Fail'}
df['FAIL/PASS'] = df['FAIL/PASS'].map(Fail_Pass)

Fail=df[df['FAIL/PASS']=='Fail'].value_counts().sum() 
Fail_= round(((df[df['FAIL/PASS']=='Fail'].value_counts().sum() / (df['FAIL/PASS'].value_counts().sum()))*100),2)

Pass=df[df['FAIL/PASS']=='Pass'].value_counts().sum() 
Pass_= round(((df[df['FAIL/PASS']=='Pass'].value_counts().sum() / (df['FAIL/PASS'].value_counts().sum()))*100),2)

fig1 = make_subplots(rows=1, cols=2, subplot_titles=("Passed Points Vs. Fail Points","Fail Points Location Distribution","Pass Points Location Distribution"))
 
fig1.append_trace(go.Histogram(x=df[df['FAIL/PASS']=="Fail"]['LOCATION']), row=1, col=1)
fig1.append_trace(go.Histogram(x=df[df['FAIL/PASS']=="Pass"]['LOCATION']), row=1, col=2)

fig2 = px.histogram(df, x='FAIL/PASS')
fig2.add_annotation(x='Fail', text=f"{Fail}({Fail_}%)", showarrow=True, arrowhead=3)
fig2.add_annotation(x='Pass', text=f"{Pass}({Pass_}%)", showarrow=True, arrowhead=1)
st.plotly_chart(fig1, use_container_width=True)

st.write("This graph is hsowing Bla Bla Bla Bla Bla ")

st.plotly_chart(fig2, use_container_width=True)

st.write("This graph is hsowing Bla Bla Bla Bla Bla ")
