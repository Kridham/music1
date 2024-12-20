import streamlit as st
from io import BytesIO
import zipfile

# Music files
music1 = "akhar.mp3"
music2 = "the ringtone.mp3"
music3 = "lehnga.mp3"
music4 = "fly karke.mp3"
music5 = "kaali activa.mp3"
music6 = "case.mp3"
music7 = "goat.mp3"
music8= "tere bin.mp3"
music9= "gustakhiya.mp3"
music10="chala.mp3"
music11="challa.mp3"
music12="same time same jagah.mp3"


# Initialize session state for login, song, wishlist, and checkout
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "song_to_play" not in st.session_state:
    st.session_state.song_to_play = None
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []
if "checkout" not in st.session_state:
    st.session_state.checkout = []

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1557683304-673a23048d34?fit=crop&w=1920&q=80');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #333333;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    label {
        font-size: 18px;
        color: #333333;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Wishlist & Checkout"])

# Login logic
if not st.session_state.logged_in:
    st.title("Login")
    a = st.text_input("Enter your ID:")
    b = st.text_input("Enter your password:", type="password")

    if st.button("Sign in"):
        if a == "kridham08" and b == "ridham_08":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid ID or password. Please try again.")

elif page == "Home":
    st.title("Home")
    st.write("Welcome! You are logged in.")
    song = st.text_input("Enter the song name")

    if st.button("Play Song"):
        if song.lower() in music1.lower():
            st.header("akhar")
            st.audio(music1, format="audio/mp3")
        elif song.lower() in music2.lower():
            st.header("the ringtone")
            st.audio(music2, format="audio/mp3")
        elif song.lower() in music3.lower():
            st.header("lehnga")
            st.audio(music3, format="audio/mp3")
        elif song.lower() in music4.lower():
            st.header("fly karke")
            st.audio(music4, format="audio/mp3")
        elif song.lower() in music5.lower():
            st.header("kaali activa")
            st.audio(music5, format="audio/mp3")
        elif song.lower() in music6.lower():
            st.header("case")
            st.audio(music6, format="audio/mp3")
        elif song.lower() in music7.lower():
            st.header("goat")
            st.audio(music7, format="audio/mp3")
        elif song.lower() in music8.lower():
            st.header("tere bin")
            st.audio(music8, format="audio/mp3")
        elif song.lower() in music9.lower():
            st.header("gustakhiya")
            st.audio(music9, format="audio/mp3")
        elif song.lower() in music10.lower():
            st.header("chala")
            st.audio(music10, format="audio/mp3")
        elif song.lower() in music11.lower():
            st.header("challa")
            st.audio(music11, format="audio/mp3")
        elif song.lower() in music12.lower():
            st.header("same time same jagah")
            st.audio(music12, format="audio/mp3")
        else:
            st.error("Song not found. Please check the spelling.")
    
    
    
       


    if st.button("Add to Wishlist"):
        if song and song not in st.session_state.wishlist:
            st.session_state.wishlist.append(song)
            st.success(f"'{song}' added to your wishlist!")
        elif song in st.session_state.wishlist:
            st.warning(f"'{song}' is already in your wishlist.")
        else:
            st.error("Please enter a valid song name.")

elif page == "Wishlist & Checkout":
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
    if st.button("Add to Checkout"):
        for song in checkout_songs:
            if song not in st.session_state.checkout:
                st.session_state.checkout.append(song)
        if checkout_songs:
            st.success("Selected songs added to checkout!")
        else:
            st.error("Please select at least one song.")

    # Play or download checked-out songs
    if st.session_state.checkout:
        st.write("Your Checkout:")
        for song in st.session_state.checkout:
            st.write(f"- {song}")
            if song.lower() == "akhar":
                song_path = music1
            elif song.lower() == "the ringtone":
                song_path = music2
            elif song.lower() == "lehnga":
                song_path = music3
            elif song.lower() == "fly karke":
                song_path = music4
            elif song.lower() == "kaali activa":
                song_path = music5
            elif song.lower() == "case":
                song_path = music6
            elif song.lower() == "goat":
                song_path = music7
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

        # Show Download All Wishlist Songs
        if len(st.session_state.wishlist) > 1:
            if st.button("Download All Wishlist Songs"):
                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                    for song in st.session_state.wishlist:
                        if song.lower() == "akhar":
                            song_path = music1
                        elif song.lower() == "the ringtone":
                            song_path = music2
                        elif song.lower() == "lehnga":
                            song_path = music3
                        elif song.lower() == "fly karke":
                            song_path = music4
                        elif song.lower() == "kaali activa":
                            song_path = music5
                        elif song.lower() == "case":
                            song_path = music6
                        elif song.lower() == "goat":
                            song_path = music7
                        else:
                            continue

                        zip_file.write(song_path, arcname=f"{song}.mp3")

                zip_buffer.seek(0)
                st.download_button(
                    label="Download All Songs as ZIP",
                    data=zip_buffer,
                    file_name="wishlist_songs.zip",
                    mime="application/zip",
                )
