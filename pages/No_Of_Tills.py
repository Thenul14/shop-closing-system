import streamlit as st
import time

if "number_of_tills" not in st.session_state:
    st.session_state["number_of_tills"] = 1

st.subheader("Select Number of Tills")

number_of_tills = st.radio(
    "How many tills were used today?",
    ["One Till", "Two Tills"]
    )

if st.button("Start Balance"):
    if number_of_tills == "One Till":
        number_of_tills = 1
    elif number_of_tills == "Two Tills":
        number_of_tills = 2
    st.session_state["number_of_tills"] = number_of_tills

    with st.spinner("Balance started!"):

            time.sleep(1)
            st.switch_page("pages/Count_Cash.py")
            


    