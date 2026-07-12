import streamlit as st
import time
from calculator import Calculator




st.subheader("Here's the summary for A, B, C, D, E!!!")
calculator = Calculator(st.session_state.till1, st.session_state.cardmachine1, st.session_state.till2, st.session_state.cardmachine2)
A,B,C,D,E = calculator.calcualte_ABCED()
st.write("A is", A)
st.write("B is", B)
st.write("C is", C)
st.write("D is", D)
st.write("E is", E)

if st.button("Finish"):
    
    with st.spinner("Thank you, Have a nice day..!"):
        time.sleep(1)
        st.switch_page("app2.py")