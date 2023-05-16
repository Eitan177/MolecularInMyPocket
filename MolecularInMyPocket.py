import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os
st.set_page_config(layout="wide")


img1=Image.open("ampsd1.png")
img2=Image.open("ampsd2.png")

st.title('MOLECULAR IN MY POCKET SOLID TUMORS')

st.title('Prepared by the Association for Molecular Pathology  Training and Education Committee')

dd = pd.read_csv('EditedSolidTumors.csv')

solid, tab1, tab2, tab3,tab4, tab5, tab6  = st.tabs(["solid","MPN", "Colorectal", "Melanoma","CNS","Lung",'Thyroid'])


mpn=pd.read_csv('MPN.csv')
colorectal=pd.read_csv('Colorectal.csv')
melanoma=pd.read_csv('Melanoma.csv')
cns=pd.read_csv('CNS.csv')
lung=pd.read_csv('Lung.csv')
thyroid=pd.read_csv('Thyroid.csv')
with solid:

    
    st.title('Solid Tumors')
    solidsearch=st.text_input('Solid Tumor Search','')
    if solidsearch != '':
        substring=solidsearch
        dd= dd[dd.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.dataframe(dd)
with tab1:
    st.title('MPN')
    mpnsearch=st.text_input('MPN Search','')
    if mpnsearch != '':
        substring=mpnsearch
        mpn= mpn[mpn.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.dataframe(mpn)
with tab2:
    st.title('Colorectal')
    colorectalsearch=st.text_input('Colorectal Search','')
    if colorectalsearch != '':
        substring=colorectalsearch
        colorectal= colorectal[colorectal.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.dataframe(colorectal,height=900)
with tab3:
    st.title('Melanoma')
    melanomasearch=st.text_input('Melanoma Search','')
    if melanomasearch != '':
        substring=melanomasearch
        melanoma= melanoma[melanoma.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.dataframe(melanoma,height=900)
with tab4:
    st.title('CNS')
    cnssearch=st.text_input('CNS Search','')
    if cnssearch != '':
        substring=cnssearch
        cns= cns[cns.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.dataframe(cns,height=900)
with tab5:
    st.title('Lung')
    lungsearch=st.text_input('Lung Search','')
    if lungsearch != '':
        substring=lungsearch
        lung= lung[lung.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.dataframe(lung,height=900)
with tab6:
    st.title('Thyroid')
    thyroidsearch=st.text_input('Thyroid Search','')
    if thyroidsearch != '':
        substring=thyroidsearch
        thyroid= thyroid[thyroid.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    st.dataframe(thyroid,height=900)

st.image(img1,use_column_width=True)
st.image(img2,use_column_width=True)
st.download_button('solid tumor data',dd.to_csv(index=False).encode('utf-8'),'SolidTumors.csv')
