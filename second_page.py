state_name = "second_page_state"
# initialize the page specific state
if state_name not in st.session_state:
    st.session_state[state_name] = {}
# assign it to a variable so you don't have to worry about referencing the right state
# further in this code
state = st.session_state[state_name]

# then reference values with dictionary notation
state['value'] = "second_page_state"
