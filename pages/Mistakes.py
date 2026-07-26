import streamlit as st
import time
from calculator import Calculator

if "calculator" not in st.session_state:
    st.session_state.calculator = None


if st.session_state.number_of_tills == 1:
    calculator = Calculator(
        st.session_state.till1,
        st.session_state.cardmachine1,
        st.session_state.till1.get_cardmachineDetails()
    )
    st.session_state.calculator = calculator
else:
    calculator = Calculator(
        st.session_state.till1,
        st.session_state.cardmachine1,
        st.session_state.till1.get_cardmachineDetails(),
        st.session_state.till2,
        st.session_state.cardmachine2,
        st.session_state.till2.get_cardmachineDetails()
    )
    st.session_state.calculator = calculator

missing_details = calculator.find_missing_transaction_amount()


if missing_details["flag"] == True:
    
    st.warning("Tills and Card Machines are not Balanced. Please check the following.")
    for key, value in list(missing_details.items())[1:]:
        st.write(f"**{key}:** {value}")

    if st.button("Mistakes Corrected"):
          
        with st.spinner("Calculating Summary..."):
            time.sleep(1)
            st.switch_page("pages/ABCDE.py")
else:
    st.success("Tills and Card Machines are Balance. You can go to the next step. Click the button below.")
    if st.button("Go to next step"):
              
            with st.spinner("Calculating Summary..."):
                time.sleep(1)
                st.switch_page("pages/ABCDE.py")
            
            