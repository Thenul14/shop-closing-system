import streamlit as st
import time
from calculator import Calculator

if st.session_state.number_of_tills == 1:
    calculator = Calculator(
        st.session_state.till1,
        st.session_state.cardmachine1,
        st.session_state.till1.get_cardmachineDetails()
    )
else:
    calculator = Calculator(
        st.session_state.till1,
        st.session_state.cardmachine1,
        st.session_state.till1.get_cardmachineDetails(),
        st.session_state.till2,
        st.session_state.cardmachine2,
        st.session_state.till2.get_cardmachineDetails()
    )

missing_details = calculator.find_missing_transaction_amount()
warning_section = st.empty()

if missing_details["flag"] == True:
    with warning_section.container():
        st.warning("Tills and Card Machines are not Balanced. Please check the following.")
        for key, value in list(missing_details.items())[1:]:
            st.write(f"**{key}:** {value}")

    if st.button("Mistakes Corrected"):
        warning_section.empty()    
        with st.spinner("Calculating Summary..."):
            time.sleep(1)
            
            st.subheader("Here's the summary for A, B, C, D, E!!!")
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
