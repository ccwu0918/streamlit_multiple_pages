import streamlit as st
import first_page, second_page

state = st.session_state

first_page_title= "first_page"
second_page_title = "second_page"
page_titles = [first_page_title, second_page_title]

def page_change():
    st.experimental_set_query_params(page=state.page_select)


# on first run, set page index to page in query params
# if that doesn't exist, set it to 0 and set the query params to the first page
page_index = 0
if "first_run" not in state:
    state.first_run = True
    if "page" in st.experimental_get_query_params():
        page_index = page_titles.index(st.experimental_get_query_params()["page"][0])
    st.experimental_set_query_params(page=page_titles[page_index])

# Page Selector
# value isn't saved since it's tracked in the query params.
st.sidebar.selectbox("Navigation", page_titles, key="page_select", on_change=page_change, index=page_index)

# get the page from the query params
page = st.experimental_get_query_params()["page"][0]

# load the selected page
if page == first_page_title:
    first_page.run()
elif page == second_page_title:
    second_page.run()

    
if not hasattr(st, 'already_started_server'):
    # Hack the fact that Python modules (like st) only load once to
    # keep track of whether this file already ran.
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    from flask import Flask

    app = Flask(__name__)

    @app.route('/foo')
    def serve_foo():
        return 'This page is served via Flask!'

    app.run(port=8888)


# We'll never reach this part of the code the first time this file executes!

# Your normal Streamlit app goes here:
x = st.slider('Pick a number')
st.write('You picked:', x)
