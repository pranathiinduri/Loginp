mport streamlit as st

# Function for checking login credentials
def check_credentials(username, password):
    # Simple static check for credentials
    return username == "abhay" and password == "abhay"

# Function to display the login page
def login_page():
    st.title("Welcome to the Login Page")
    st.markdown("""
        <style>
        .login-container {
            text-align: center;
            padding: 20px;
            margin-top: 50px;
        }
        </style>
        <div class='login-container'>
            <h3>Please enter your credentials</h3>
        </div>
    """, unsafe_allow_html=True)

    # Create a two-column layout for better aesthetics
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150", width=100)  # Placeholder for a logo/image
    with col2:
        # Input fields for username and password
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

    # Centered login button
    if st.button("Login", help="Click to log in"):
        if check_credentials(username, password):
            st.success("Login successful!")
            st.session_state['logged_in'] = True
            st.balloons()  # Add a celebratory touch for successful login
            st.markdown('[Go to Home Page](https://homepy-bx2rsnhevyrwh5wxkvynmy.streamlit.app/)', unsafe_allow_html=True)
        else:
            st.error("Invalid username or password. Please try again.")

# Main app function
def main_app():
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        login_page()
    else:
        st.title("Welcome!")
        st.markdown("You are successfully logged in. Explore the features or visit the home page below:")
        st.markdown('[Go to Home Page](https://homepy-bx2rsnhevyrwh5wxkvynmy.streamlit.app/)', unsafe_allow_html=True)

# Run the app
if _name_ == "_main_":
    main_app()