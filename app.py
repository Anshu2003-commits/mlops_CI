import streamlit as st
#streamlit ui
st.title("power calculator")
st.write("enter a number to calculate its square,cube and fifth power")

#get user input
n = st.number_input("enter an integer",value=1,step=1)

#calculate result
square = n**2
cube = n**3
fifth = n**5
#display result
st.write(f"the square of {n} is {square}")
st.write(f"the cube of {n} is {cube}")
st.write(f"the fifth of {n} is {fifth}")

         