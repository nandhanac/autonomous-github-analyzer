import streamlit as st
import joblib

from app.github.github_api import get_repository_info


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="GitHub Repository Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================================
# Custom CSS
# ==========================================

st.markdown(
    """
    <style>

    /* ==============================
       GLOBAL
    ============================== */

    .stApp {
        background:
            radial-gradient(
                circle at top,
                #161b22 0%,
                #0d1117 45%,
                #010409 100%
            );
        color: #e6edf3;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    div[data-testid="stVerticalBlock"] {
        gap: 0.6rem;
    }


    /* ==============================
       HEADER
    ============================== */

    .main-title {
        text-align: center;
        font-size: 32px;
        font-weight: 700;
        color: #f0f6fc;
        margin-top: 5px;
        margin-bottom: 3px;
        letter-spacing: -0.5px;
    }

    .subtitle {
        text-align: center;
        font-size: 14px;
        color: #8b949e;
        margin-bottom: 24px;
    }


    /* ==============================
       INPUT
    ============================== */

    div[data-testid="stTextInput"] label {
        color: #c9d1d9 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stTextInput"] input {
        background: #0d1117 !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        font-size: 14px !important;
        padding: 10px 12px !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 0 1px #58a6ff !important;
    }


    /* ==============================
       BUTTONS
    ============================== */

    .stButton > button {
        border-radius: 7px;
        border: 1px solid #30363d;
        background: #21262d;
        color: #e6edf3;
        font-size: 13px;
        font-weight: 600;
        min-height: 38px;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: #30363d;
        border-color: #8b949e;
        color: white;
    }


    /* ==============================
       SECTION TITLES
    ============================== */

    .section-title {
        font-size: 18px;
        font-weight: 650;
        color: #f0f6fc;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid #21262d;
        padding-bottom: 7px;
    }


    /* ==============================
       INFORMATION CARDS
    ============================== */

    .card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px 17px;
        min-height: 78px;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.18);
        transition: 0.2s ease;
    }

    .card:hover {
        border-color: #484f58;
        transform: translateY(-1px);
    }

    .card-title {
        font-size: 11px;
        color: #8b949e;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .card-value {
        font-size: 18px;
        font-weight: 650;
        color: #f0f6fc;
        word-break: break-word;
    }


    /* ==============================
       DESCRIPTION
    ============================== */

    .description {
        color: #c9d1d9;
        font-size: 13px;
        line-height: 1.55;
        min-height: auto;
    }


    /* ==============================
       TOPICS
    ============================== */

    .topics-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 14px 17px;
        color: #c9d1d9;
        font-size: 13px;
        line-height: 1.7;
    }


    /* ==============================
       STREAMLIT ALERTS
    ============================== */

    div[data-testid="stAlert"] {
        border-radius: 8px;
        font-size: 13px;
    }


    /* ==============================
       CHART CONTAINER
    ============================== */

    .chart-container {
        background: #0d1117;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 12px 15px 5px 15px;
        margin-top: 5px;
    }


    /* ==============================
       FOOTER
    ============================== */

    .footer {
        text-align: center;
        color: #484f58;
        font-size: 11px;
        margin-top: 35px;
        padding: 15px;
        border-top: 1px solid #21262d;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# Load ML Model
# ==========================================

model = joblib.load(
    "models/repository_classifier.pkl"
)

vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)


# ==========================================
# Clear URL Function
# ==========================================

def clear_url():
    st.session_state.github_url = ""


# ==========================================
# Header
# ==========================================

st.markdown(
    '<div class="main-title">🤖 GitHub Repository Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze GitHub repositories using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# URL Input
# ==========================================

github_url = st.text_input(
    "🌐 GitHub Repository URL",
    placeholder="https://github.com/username/repository",
    key="github_url"
)


# ==========================================
# Buttons
# ==========================================

col1, col2 = st.columns([2, 1])

with col1:

    analyze_button = st.button(
        "🔍 Analyze Repository",
        use_container_width=True
    )

with col2:

    clear_button = st.button(
        "🗑️ Clear",
        use_container_width=True,
        on_click=clear_url
    )


# ==========================================
# Clear
# ==========================================

if clear_button:

    st.rerun()


# ==========================================
# Analyze Repository
# ==========================================

if analyze_button:

    if not github_url:

        st.warning(
            "Please enter a GitHub repository URL."
        )

    else:

        try:

            with st.spinner(
                "🔄 Fetching repository information..."
            ):

                data = get_repository_info(
                    github_url
                )


            # ==================================
            # Repository Information
            # ==================================

            st.markdown(
                '<div class="section-title">'
                '📁 Repository Information'
                '</div>',
                unsafe_allow_html=True
            )


            col1, col2, col3, col4 = st.columns(4)


            with col1:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">
                            Repository
                        </div>
                        <div class="card-value">
                            {data.get("name", "Unknown")}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with col2:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">
                            Language
                        </div>
                        <div class="card-value">
                            {data.get("language") or "Unknown"}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with col3:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">
                            ⭐ Stars
                        </div>
                        <div class="card-value">
                            {data.get("stargazers_count", 0)}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with col4:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">
                            🍴 Forks
                        </div>
                        <div class="card-value">
                            {data.get("forks_count", 0)}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # ==================================
            # Description
            # ==================================

            st.markdown(
                '<div class="section-title">'
                '📝 Description'
                '</div>',
                unsafe_allow_html=True
            )


            description = (
                data.get("description")
                or "No description available."
            )


            st.markdown(
                f"""
                <div class="card description">
                    {description}
                </div>
                """,
                unsafe_allow_html=True
            )


            # ==================================
            # Extract Features
            # ==================================

            name = data.get(
                "name",
                ""
            )

            language = data.get(
                "language"
            ) or ""

            topics = " ".join(
                data.get(
                    "topics",
                    []
                )
            )


            repository_text = " ".join([
                name,
                description,
                language,
                topics
            ])


            # ==================================
            # TF-IDF
            # ==================================

            text_tfidf = vectorizer.transform(
                [repository_text]
            )


            # ==================================
            # Prediction
            # ==================================

            prediction = model.predict(
                text_tfidf
            )[0]


            # ==================================
            # Prediction Probability
            # ==================================

            probabilities = model.predict_proba(
                text_tfidf
            )[0]

            confidence = (
                max(probabilities) * 100
            )


            # ==================================
            # ML Prediction
            # ==================================

            st.markdown(
                '<div class="section-title">'
                '🤖 Machine Learning Prediction'
                '</div>',
                unsafe_allow_html=True
            )


            col1, col2 = st.columns(2)


            with col1:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">
                            Predicted Category
                        </div>
                        <div class="card-value">
                            {prediction}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with col2:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">
                            Model Probability
                        </div>
                        <div class="card-value">
                            {confidence:.2f}%
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # ==================================
            # Probability Chart
            # ==================================

            st.markdown(
                '<div class="section-title">'
                '📊 Prediction Probabilities'
                '</div>',
                unsafe_allow_html=True
            )


            probability_data = {}

            for category, probability in zip(
                model.classes_,
                probabilities
            ):

                probability_data[
                    category
                ] = probability


            st.markdown(
                '<div class="chart-container">',
                unsafe_allow_html=True
            )

            st.bar_chart(
                probability_data,
                height=260
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


            # ==================================
            # Topics
            # ==================================

            st.markdown(
                '<div class="section-title">'
                '🔧 Detected Technologies / Topics'
                '</div>',
                unsafe_allow_html=True
            )


            topic_list = data.get(
                "topics",
                []
            )


            if topic_list:

                topics_html = " • ".join(
                    topic_list
                )

                st.markdown(
                    f"""
                    <div class="topics-card">
                        {topics_html}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.info(
                    "No GitHub topics available."
                )


        except Exception as e:

            st.error(
                f"❌ Error analyzing repository: {e}"
            )


# ==========================================
# Footer
# ==========================================

st.markdown(
    """
    <div class="footer">
        GitHub Repository Analyzer •
        Machine Learning Version 1
    </div>
    """,
    unsafe_allow_html=True
)