import streamlit as st

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp, .main, .block-container {
            color: #e2e8f0;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(59, 130, 246, 0.24), transparent 22%),
                radial-gradient(circle at top right, rgba(16, 185, 129, 0.18), transparent 20%),
                linear-gradient(180deg, #050816 0%, #0b1220 24%, #111827 100%);
        }

        section.main > div.block-container {
            padding-top: 1.15rem;
            padding-bottom: 1.75rem;
            max-width: 1320px;
        }

        .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6, .stMarkdown span {
            color: inherit !important;
            opacity: 1 !important;
        }

        .hero-shell {
            padding: 2rem 2.2rem;
            border-radius: 30px;
            background: linear-gradient(135deg, rgba(8, 15, 31, 0.96), rgba(17, 24, 39, 0.92));
            border: 1px solid rgba(148, 163, 184, 0.16);
            box-shadow: 0 30px 80px rgba(2, 6, 23, 0.45);
            color: #e2e8f0;
            position: relative;
            overflow: hidden;
        }

        .hero-shell::after {
            content: '';
            position: absolute;
            inset: auto -6% -55% auto;
            width: 320px;
            height: 320px;
            border-radius: 999px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.24) 0%, rgba(59, 130, 246, 0) 68%);
        }

        .hero-kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.45rem 0.9rem;
            border-radius: 999px;
            background: rgba(14, 165, 233, 0.14);
            border: 1px solid rgba(56, 189, 248, 0.18);
            font-size: 0.84rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #7dd3fc;
        }

        .hero-title {
            margin-top: 1rem;
            font-size: clamp(2rem, 4vw, 3.4rem);
            line-height: 1.05;
            font-weight: 800;
            letter-spacing: -0.04em;
            color: #f8fafc;
        }

        .hero-copy {
            max-width: 760px;
            color: #cbd5e1;
            font-size: 1.02rem;
            line-height: 1.8;
        }

        .metric-card {
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.88), rgba(17, 24, 39, 0.88));
            border: 1px solid rgba(148, 163, 184, 0.16);
            backdrop-filter: blur(10px);
            border-radius: 22px;
            padding: 1.05rem 1.15rem;
            box-shadow: 0 18px 35px rgba(2, 6, 23, 0.24);
        }

        .metric-label {
            font-size: 0.76rem;
            letter-spacing: 0.11em;
            text-transform: uppercase;
            color: #94a3b8;
            font-weight: 700;
        }

        .metric-value {
            font-size: 1.45rem;
            font-weight: 800;
            color: #f8fafc;
            margin-top: 0.25rem;
        }

        .panel {
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(17, 24, 39, 0.94));
            border: 1px solid rgba(148, 163, 184, 0.16);
            border-radius: 28px;
            padding: 1.6rem;
            box-shadow: 0 24px 60px rgba(2, 6, 23, 0.28);
        }

        div[data-testid="stForm"] {
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(17, 24, 39, 0.94));
            border: 1px solid rgba(148, 163, 184, 0.16);
            border-radius: 28px;
            padding: 1.4rem;
            box-shadow: 0 24px 60px rgba(2, 6, 23, 0.28);
        }

        .panel h3 {
            color: #f8fafc;
            font-weight: 800;
            letter-spacing: -0.03em;
        }

        .section-copy {
            color: #cbd5e1;
            margin-top: 0.25rem;
        }

        .stSelectbox label, .stNumberInput label {
            font-weight: 700 !important;
            color: #e2e8f0 !important;
            font-size: 0.92rem !important;
        }

        .stSelectbox div[data-baseweb="select"] > div,
        .stNumberInput input {
            background-color: #0f172a !important;
            border: 1px solid rgba(148, 163, 184, 0.24) !important;
            border-radius: 14px !important;
            min-height: 3.1rem !important;
            box-shadow: none !important;
        }

        .stSelectbox [data-baseweb="select"] * {
            color: #e2e8f0 !important;
            opacity: 1 !important;
        }

        .stSelectbox [data-baseweb="select"] svg {
            fill: #cbd5e1 !important;
        }

        .stSelectbox [data-baseweb="popover"] {
            border-radius: 14px !important;
            overflow: hidden !important;
        }

        .stSelectbox [data-baseweb="menu"] {
            background: #0f172a !important;
        }

        .stSelectbox [role="option"] {
            color: #e2e8f0 !important;
            background: #0f172a !important;
        }

        .stSelectbox [role="option"][aria-selected="true"],
        .stSelectbox [role="option"]:hover {
            background: rgba(59, 130, 246, 0.18) !important;
            color: #e2e8f0 !important;
        }

        .stSelectbox [data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
        .stSelectbox [data-baseweb="select"] input {
            color: #e2e8f0 !important;
            -webkit-text-fill-color: #e2e8f0 !important;
        }

        .stNumberInput input {
            color: #e2e8f0 !important;
            -webkit-text-fill-color: #e2e8f0 !important;
        }

        .stNumberInput [data-baseweb="input"] {
            background: #0f172a !important;
        }

        .stNumberInput button {
            background: #1e293b !important;
            color: #f8fafc !important;
        }

        .stNumberInput button svg {
            fill: #f8fafc !important;
        }

        .stSelectbox div[data-baseweb="select"] > div:hover,
        .stNumberInput input:hover {
            border-color: #38bdf8 !important;
        }

        .stButton > button {
            width: 100%;
            padding: 0.88rem 1.2rem;
            border-radius: 14px;
            background: linear-gradient(135deg, #38bdf8, #6366f1);
            color: #f8fafc;
            font-weight: 800;
            border: none;
            box-shadow: 0 18px 35px rgba(59, 130, 246, 0.24);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 24px 50px rgba(99, 102, 241, 0.30);
        }

        .result-card {
            border-radius: 24px;
            padding: 1.25rem 1.35rem;
            background: linear-gradient(135deg, rgba(34, 197, 94, 0.10), rgba(59, 130, 246, 0.10));
            border: 1px solid rgba(148, 163, 184, 0.16);
            color: #e2e8f0;
        }

        .result-value {
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            color: #f8fafc;
        }

        .sidebar-brand {
            padding: 1.1rem 1rem 1.5rem;
            border-radius: 22px;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.18), rgba(124, 58, 237, 0.14));
            border: 1px solid rgba(148, 163, 184, 0.16);
            margin-bottom: 1rem;
        }

        .sidebar-brand h4 {
            margin: 0;
            font-size: 1.05rem;
            font-weight: 800;
            color: #e2e8f0;
        }

        .sidebar-brand p {
            margin: 0.35rem 0 0;
            color: #94a3b8;
            font-size: 0.88rem;
        }

        .stSidebar {
            background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
        }

        .stSidebar label, .stSidebar p, .stSidebar span {
            color: #e2e8f0 !important;
        }

        .info-chip {
            display: inline-flex;
            padding: 0.45rem 0.78rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
            background: rgba(14, 165, 233, 0.12);
            color: #bae6fd;
            border: 1px solid rgba(255,255,255,0.1);
        }

        .footer-note {
            text-align: center;
            color: #94a3b8;
            font-size: 0.9rem;
            padding: 1.25rem 0 0.75rem;
        }

        .stAlert {
            background: rgba(15, 23, 42, 0.96) !important;
            color: #e2e8f0 !important;
            border: 1px solid rgba(148, 163, 184, 0.16) !important;
            border-radius: 16px !important;
        }

        .stAlert p, .stAlert div, .stAlert span {
            color: #e2e8f0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_styles()

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <h4>🎓 Student Predictor</h4>
            <p>Streamlit deployment demo</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Quick Guide")
    st.markdown(
        """
        <div class="info-chip">1. Choose student profile</div><br><br>
        <div class="info-chip">2. Enter reading and writing scores</div><br><br>
        <div class="info-chip">3. Click Predict Score</div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("This app uses the trained model and preprocessing artifacts in the project folder.")

st.markdown(
    """
    <div class="hero-shell">
        <div class="hero-kicker">● AI powered academic analytics</div>
        <h1 class="hero-title">Student Exam Performance Predictor</h1>
        <p class="hero-copy">
            Enter a few profile details and the trained ML pipeline will estimate the student’s score.
            The layout is designed to feel like a modern analytics product, not a plain form.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
left, middle, right = st.columns([1, 1, 1])
with left:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Model</div>
            <div class="metric-value">CatBoost / Scikit-learn</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with middle:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Deployment</div>
            <div class="metric-value">Streamlit Ready</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">UI Style</div>
            <div class="metric-value">Premium Dashboard</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.markdown("<h3 style='margin: 0 0 0.3rem 0; color: #f8fafc; font-weight: 800;'>Predict Student Performance</h3>", unsafe_allow_html=True)
st.markdown("<div class='section-copy'>Use the input fields below to generate a score prediction.</div>", unsafe_allow_html=True)

with st.form(key="predict_form"):
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["male", "female"])
        race_ethnicity = st.selectbox("Race / Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        parental = st.selectbox(
            "Parental Level of Education",
            ["associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"],
        )
    with col2:
        lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])
        prep = st.selectbox("Test Preparation", ["none", "completed"])
        reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=70)

    writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=70)
    submitted = st.form_submit_button("Predict Score")

if submitted:
    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental,
        lunch=lunch,
        test_preparation_course=prep,
        reading_score=int(reading_score),
        writing_score=int(writing_score),
    )

    pipeline = PredictPipeline()
    try:
        prediction = pipeline.predict(data.get_data_as_dataframe())
        prediction_value = round(float(prediction[0]), 3) if hasattr(prediction, "__len__") else round(float(prediction), 3)

        st.markdown(
            f"""
            <div class="result-card">
                <div class="metric-label">Predicted score</div>
                <div class="result-value">{prediction_value}</div>
                <div class="section-copy">Based on the selected student profile and trained pipeline.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.markdown('<div class="footer-note">Built for a polished deployment experience.</div>', unsafe_allow_html=True)
