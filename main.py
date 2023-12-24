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

    while ' ' in boy:  # removing all the empty spaces
        boy.pop(boy.index(' '))
    while ' ' in girl:
        girl.pop(girl.index(' '))

    for i in range(len(boy) - 1, -1, -1):  # removing all the matched characters
        if boy[i] in girl:
            # print(boy[i],'true')
            girl.pop(girl.index(boy[i]))
            boy.pop(i)
            # print(boy,girl)
    trans = boy + girl
    # print(trans,len(trans))#i dont really mean it, it is just fun and games
    num = len(trans)  # list of unmatched characters
    time.sleep(1)  # added time for that extra bit of suspense
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    a = 0  # stores the index of the previously removed character
    for love in range(6, 1, -1):
        s = num % love - 1  # index no of the element to be removed
        st.write(popped[flames[(s + a) % love]])
        flames.pop((s + a) % love)
        a = s  # this is so that after restart the loop and land on a value,and u move to the next 'a'th element
        time.sleep(1.5)  # cooldown time, to build suspence
    st.title(result[flames[0]])
