import streamlit as st
import time

st.title('FLAMES')
st.subheader("Unveil the relationship with just the names!!")

st.text_input(label="1", placeholder="Enter the first name: ",  key="1st", label_visibility="collapsed")
st.text_input(label="2", placeholder="Enter the second name: ", key="2nd", label_visibility="collapsed")

button = st.button(label="Click here to reveal",key="But")
if button:
    popped = {'F': 'You are not friends', 'L': 'You guys are not lovers', 'A': 'You guys are not affectionate',
              'M': 'You guys are not Married', 'E': 'You guys are not Enemies', 'S': 'You guys are not siblings'}
    result = {'F': 'You are friends', 'L': 'You guys are lovers', 'A': 'You guys are affectionate',
              'M': 'You guys are Married', 'E': 'You guys are Enemies', 'S': 'You guys are siblings'}

    B = st.session_state["1st"]
    G = st.session_state["2nd"]

    boy = list(B.lower())
    girl = list(G.lower())

    while ' ' in boy:
        boy.pop(boy.index(' '))
    while ' ' in girl:
        girl.pop(girl.index(' '))
    for i in range(len(boy)-1,-1,-1):                               
        if boy[i] in girl:
         girl.pop(girl.index(boy[i]))
         boy.pop(i)
    num = len(boy + girl)
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    a = 0
    time.sleep(2)
    for love in range(6, 1, -1):
        s = num % love - 1
        st.write(popped[flames[(s + a) % love]])
        flames.pop((s + a) % love)
        a = s
        time.sleep(2)
    st.title(result[flames[0]])
