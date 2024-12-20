import streamlit as st
music1 = "akhar.mp3"
music2 = "the ringtone.mp3"
music3="lehnga.mp3"
music4="fly karke.mp3"
music5="kaali activa.mp3"
music6="case.mp3"
music7="goat.mp3"
music8=""
music9=""
music10=""
# Initialize session state for login, song, wishlist, and checkout
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "song_to_play" not in st.session_state:
    st.session_state.song_to_play = None
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []
if "checkout" not in st.session_state:
    st.session_state.checkout = []

# Title
st.title("Login")

# Login logic
if not st.session_state.logged_in:
    # User input for login
    a = st.text_input("Enter your ID:")
    b = st.text_input("Enter your password:", type="password")

    # Login button
    if st.button("Sign in"):
        if a == "kridham08" and b == "ridham_08":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid ID or password. Please try again.")
            st.image("stress.png")
else:
    # Song selection logic
    st.write("Welcome! You are logged in.")
    song = st.text_input("Enter the song name")

    if st.button("Play Song"):
        if song.lower() in music1.lower():
            st.header("akhar")
            st.audio(music1, format="audio/mp3")
        if song.lower() in music2.lower():
            st.header("the ringtone")
            st.audio(music2,format="audio/mp3")
        if song.lower() in music3.lower():
            st.header("lehnga")
            st.audio(music3,format="audio/mp3")
        

    # Wishlist logic
    if st.button("Add to Wishlist"):
        if song and song not in st.session_state.wishlist:
            st.session_state.wishlist.append(song)
            st.success(f"'{song}' added to your wishlist!")
        elif song in st.session_state.wishlist:
            st.warning(f"'{song}' is already in your wishlist.")
        else:
            st.error("Please enter a valid song name.")

    # View Wishlist
    if st.button("View Wishlist"):
        if st.session_state.wishlist:
            st.write("Your Wishlist:")
            for i, wish in enumerate(st.session_state.wishlist, 1):
                st.write(f"{i}. {wish}")
        else:
            st.warning("Your wishlist is empty.")

    # Checkout logic
    checkout_song = st.selectbox(
        "Select a song from your wishlist to checkout:",
        options=[""] + st.session_state.wishlist,
    )
    if st.button("Add to Checkout"):
        if checkout_song and checkout_song not in st.session_state.checkout:
            st.session_state.checkout.append(checkout_song)
            st.success(f"'{checkout_song}' added to checkout!")
        elif checkout_song in st.session_state.checkout:
            st.warning(f"'{checkout_song}' is already in your checkout.")
        else:
            st.error("Please select a valid song to checkout.")

    # Play or download checked-out songs
    if st.session_state.checkout:
        st.write("Your Checkout:")
        for song in st.session_state.checkout:
            st.write(f"- {song}")
            if song.lower() == "akhar":
                song_path = music1
            elif song.lower() == "the ringtone":
                song_path = music2
            else:
                continue

            st.audio(song_path, format="audio/mp3")
            with open(song_path, "rb") as file:
                st.download_button(
                    label=f"Download '{song}'",
                    data=file,
                    file_name=f"{song}.mp3",
                    mime="audio/mp3",
                )
