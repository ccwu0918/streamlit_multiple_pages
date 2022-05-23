import streamlit as st

# state = st.session_state

state_name = "first_page_state"
# initialize the page specific state
if state_name not in st.session_state:
    st.session_state[state_name] = {}
# assign it to a variable so you don't have to worry about referencing the right state
# further in this code
state = st.session_state[state_name]

# then reference values with dictionary notation
state['value'] = "first_page_state"

def run(self):
    try:
        if self._target:
            self._target(*self._args, **self._kwargs)
    finally:
    # Avoid a refcycle if the thread is running a function with
    # an argument that has a member that points to the thread.
        del self._target, self._args, self._kwargs
