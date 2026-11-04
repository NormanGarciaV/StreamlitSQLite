import streamlit as st
import pandas as pd
from functions import *
from itables.streamlit import interactive_table


init_db()


st.title("Welcome to the Streamlit App")
           

st.markdown("##  User list")
users = get_users()

columns_headers=["ID", "Username", "Email"]

df = pd.DataFrame(users, columns=columns_headers)

interactive_table(
    df, 
    style = "width: 100%", # Sets the table width and height with scroll
    pageLength= 5,
    lengthMenu= [5, 10, 15, 20, -1],
    order = [[1, "desc"]], # Orders the table desc by the 1st column.
    columnDefs = [
        {"targets": [0], "visible": False}
    ]
)


#names = get_users()

col1, col2 = st.columns(2)
with col1:

    st.markdown("### Add user")
    with st.form(key='user_form', clear_on_submit=True):
        user = st.text_input("Username")
        email = st.text_input("Email")
        addUser = st.form_submit_button("Add User")

        if addUser:
            if user.split() and email.split():
                insert_user(user, email)
                st.rerun()


with col2:
    st.markdown("### Delete user")

    # Drop down list using the lambda function, showing the name but returning the id
    selected_user = st.selectbox("Select a user to delete", options=users, format_func=lambda x: x[1], index=None, placeholder="Select a user")
    if selected_user is not None:
        st.write(f"Selected lambda user: {selected_user[0]}")
    if st.button("Delete User", disabled=selected_user is None):
        delete_user(selected_user[0])
        st.session_state["selected_user"] = None
        st.rerun()