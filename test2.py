import streamlit as st
from io import BytesIO
import zipfile

# Music files
music_files = {
    "akhar": "akhar.mp3",
    "the ringtone": "the ringtone.mp3",
    "lehnga": "lehnga.mp3",
    "fly karke": "fly karke.mp3",
    "kaali activa": "kaali activa.mp3",
    "case": "case.mp3",
    "goat": "goat.mp3",
    "tere bin": "tere bin.mp3",
    "gustakhiya": "gustakhiya.mp3",
    "chala": "chala.mp3",
    "challa": "challa.mp3",
    "same time same jagah": "same time same jagah.mp3",
}

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []
if "checkout" not in st.session_state:
    st.session_state.checkout = []
if "users" not in st.session_state:
    # Default admin account
    st.session_state.users = {"kridham08": "ridham_08"}

# Sidebar for navigation
if st.session_state.logged_in:
    page = st.sidebar.radio("Navigation", ["Home", "Wishlist & Checkout"])
else:
    page = st.sidebar.radio("Navigation", ["Login", "Sign Up"])

# Sign-Up Page
if page == "Sign Up":
    st.title("Sign Up")
    new_username = st.text_input("Choose a username:")
    new_password = st.text_input("Choose a password:", type="password")
    confirm_password = st.text_input("Confirm password:", type="password")

    if st.button("Sign Up"):
        if new_username in st.session_state.users:
            st.error("Username already exists. Please choose a different one.")
        elif new_password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        elif not new_username or not new_password:
            st.error("Please fill in all fields.")
        else:
            st.session_state.users[new_username] = new_password
            st.success("Sign-up successful! You can now log in.")

# Login Page
elif page == "Login" and not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password")

    if st.button("Sign In"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            # Redirect to Home after successful login
        else:
            st.error("Invalid username or password. Please try again.")

# Home Page
elif page == "Home" and st.session_state.logged_in:
    st.title("Home")
    st.write("Welcome! You are logged in.")
    song = st.text_input("Enter the song name:")

    if st.button("Play Song"):
        found = False
        for song_name, file_path in music_files.items():
            if song.lower() == song_name.lower():
                st.header(song_name)
                st.audio(file_path, format="audio/mp3")
                found = True
                break

        if not found:
            st.error("Song not found. Please check the spelling.")

    if st.button("Add to Wishlist"):
        if song.lower() in [name.lower() for name in music_files.keys()] and song not in st.session_state.wishlist:
            st.session_state.wishlist.append(song)
            st.success(f"'{song}' added to your wishlist!")
        elif song in st.session_state.wishlist:
            st.warning(f"'{song}' is already in your wishlist.")
        else:
            st.error("Please enter a valid song name.")

# Wishlist & Checkout Page
elif page == "Wishlist & Checkout" and st.session_state.logged_in:
    st.title("Wishlist & Checkout")

    # View Wishlist
    if st.session_state.wishlist:
        st.write("Your Wishlist:")
        for i, wish in enumerate(st.session_state.wishlist, 1):
            st.write(f"{i}. {wish}")
    else:
        st.warning("Your wishlist is empty.")

    # Multi select for checkout
    checkout_songs = st.multiselect(
        "Select songs from your wishlist to checkout:",
        options=st.session_state.wishlist,
    )

    if checkout_songs:
        st.session_state.checkout = checkout_songs
        st.success("Checkout list updated!")
    else:
        st.session_state.checkout = []
        st.warning("Checkout list cleared!")

    # Play or download checked-out songs
    if st.session_state.checkout:
        st.write("Your Checkout:")
        for song in st.session_state.checkout:
            file_path = music_files.get(song.lower())
            if file_path:
                st.audio(file_path, format="audio/mp3")
                with open(file_path, "rb") as file:
                    st.download_button(
                        label=f"Download '{song}'",
                        data=file,
                        file_name=f"{song}.mp3",
                        mime="audio/mp3",
                    )

        # Download all songs as a ZIP
        if len(st.session_state.checkout) > 1:
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for song in st.session_state.checkout:
                    file_path = music_files.get(song.lower())
                    if file_path:
                        zip_file.write(file_path, arcname=f"{song}.mp3")

            zip_buffer.seek(0)
            st.download_button(
                label="Download All Checked-Out Songs as ZIP",
                data=zip_buffer,
                file_name="checked_out_songs.zip",
                mime="application/zip",
            )
else:
    st.error("Please log in to access this page.")
