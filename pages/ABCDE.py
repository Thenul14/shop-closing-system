import streamlit as st
import time
from calculator import Calculator


st.subheader("Here's the summary for A, B, C, D, E!!!")
A,B,C,D,E = st.session_state.calculator.calcualte_ABCED()
st.write("A is", A)
st.write("B is", B)
st.write("C is", C)
st.write("D is", D)
st.write("E is", E)

if st.button("Finish"):
                        
    with st.spinner("Thank you, Have a nice day..!"):
        time.sleep(1)
        st.switch_page("app2.py")
