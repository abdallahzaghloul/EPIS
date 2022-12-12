from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np

im = Image.open("EPIS.png")
image = np.array(im)
st.image(image)


st.markdown(" <center>  <h1> EDC-87 Drops Analysis </h1> </font> </center> </h1> ",
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

fig = make_subplots(rows=1, cols=3, subplot_titles=("Passed Points Vs. Fail Points","Fail Points Location Distribution","Pass Points Location Distribution"))
 
fig.append_trace(go.Histogram(x=df['FAIL/PASS']), row=1, col=1)

fig.append_trace(go.Histogram(x=df[df['FAIL/PASS']=="Fail"]['LOCATION']), row=1, col=2)
fig.append_trace(go.Histogram(x=df[df['FAIL/PASS']=="Pass"]['LOCATION']), row=1, col=3)

fig.update_layout(title_text='EDC-87 Drops Analysis', showlegend=False)
fig.add_annotation(x='Fail', text=f"{Fail}({Fail_}%)", showarrow=True, arrowhead=3)
fig.add_annotation(x='Pass', text=f"{Pass}({Pass_}%)", showarrow=True, arrowhead=1)
st.plotly_chart(fig_1, use_container_width=True)





# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




