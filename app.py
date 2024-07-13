import streamlit as st
from PIL import Image
from data.data import subject_to_fields, recommendations

# Load and apply external CSS
with open('data/style.css') as f:
    st.markdown(f'<style>{f.read()}</style><div class="title">🌟 PathwayPlanner 🌟</div>', unsafe_allow_html=True)
try:

    image_path = 'data/logo_career_app.png'  # Update this path
    image = Image.open(image_path)

    # Resize the image to logo size (e.g., 150x150 pixels) using the updated resampling method
    logo_size = (150, 150)
    image = image.resize(logo_size, Image.Resampling.LANCZOS)

    # Use columns to center the image in the Streamlit app
    col1, col2, col3 = st.columns([1.1, 2, 1])  # Adjust the ratio as needed for better centering
    with col2:
        st.image(image, caption='Enhance Your Career Planning with Visual Insights 🌟')

    # Initialize session state variables if not already set
    if 'subject' not in st.session_state:
        st.session_state.subject = None
    if 'fields' not in st.session_state:
        st.session_state.fields = []
    if 'page' not in st.session_state:
        st.session_state.page = 1

    # Sidebar: Select Subject
    with st.sidebar:
        st.markdown("### 📘 Pick a Study Area 📘", unsafe_allow_html=True)
        subjects = {
            "Mathematics": "📊",
            "Physics": "🔭",
            "Chemistry": "🧪",
            "Biology": "🧬",
            "Computer Science": "💻",
            "Economics": "💼",
            "History": "📜",
            "Geography": "🌍",
            "Literature": "📚"
        }
        for subj, emoji in subjects.items():
            if st.button(f"{emoji} {subj}", key=subj):
                st.session_state.subject = subj
                st.session_state.page = 2  # Go to Page 2 upon subject selection


    # Display a default page when no page is selected yet
    if st.session_state.page == 1:
        st.markdown(
            "<div class='content'>Welcome to PathwayPlanner 🚀. Please select your subject from the list below to begin exploring your career opportunities.</div>",
            unsafe_allow_html=True)

    # Page 2: Select Fields
    if st.session_state.page == 2:
        subject = st.session_state.subject
        st.markdown(f"<h2 class='subheader'>Fields Related to {subject} 🔍</h2>", unsafe_allow_html=True)

        fields = subject_to_fields.get(subject, [])
        selected_fields = st.multiselect("Choose your fields:", fields)

        if st.button("Submit 🚀", key="submit"):
            st.session_state.fields = selected_fields
            st.markdown(f"<h2 class='subheader'>Career Recommendations for {st.session_state.subject} 🎓</h2>",
                        unsafe_allow_html=True)
            careers = set()

            for field in st.session_state.fields:
                careers.update(recommendations.get(field, []))

            if careers:  # Display careers if any
                st.markdown(
                    "<div class='recommendations'>💼 Based on your selections, here are the ideal career paths for you:</div>",
                    unsafe_allow_html=True)

                for career in careers:
                    st.markdown(f"<li class='recommendations'>{career}</li>", unsafe_allow_html=True)
            else:
                st.markdown(
                    "<div class='recommendations'>🚫 Unfortunately, no career paths match your selected fields. Please adjust your choices and try again.</div>",
                    unsafe_allow_html=True)
except Exception as e:
    st.error(f"🚫 An unexpected error occurred: {str(e)}")



