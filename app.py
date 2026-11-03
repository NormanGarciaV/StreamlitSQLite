import streamlit as st
import pandas as pd
from functions import *


init_db()


st.title("Welcome to the Streamlit App")
st.write("Add user to the database")

with st.form(key='user_form', clear_on_submit=True):
    user = st.text_input("Username")
    email = st.text_input("Email")
    addUser = st.form_submit_button("Add User")

    if addUser:
        if user.split() and email.split():
            insert_user(user, email)
            st.success(f"User {user} added successfully!")

st.markdown("##  User list")
users = get_users()
df = pd.DataFrame(users, columns=["ID", "Username", "Email"])
st.table(df)

st.markdown("## Delete user")
names = get_users()


users_dict = {user_name: user_id for user_id, user_name, user_email in names}
selectedUser = st.selectbox("Select a user to delete", options=users_dict.keys(), key="dict")
st.write(f"Selected dict user: {users_dict[selectedUser]}")

selected_user = st.selectbox("Select a user to delete", options=names, format_func=lambda x: x[1], key="lamba")
st.write(f"Selected lambda user: {selected_user[0]}")