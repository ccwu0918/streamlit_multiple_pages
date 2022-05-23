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
    first_page()
elif page == second_page_title:
    second_page()
