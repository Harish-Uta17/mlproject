import streamlit as st

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


APP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    color-scheme: dark;
    --bg-0: #050816;
    --bg-1: #0b1220;
    --bg-2: #111827;
    --surface: rgba(15, 23, 42, 0.96);
    --surface-strong: rgba(17, 24, 39, 0.96);
    --surface-soft: rgba(30, 41, 59, 0.92);
    --text-0: #f8fafc;
    --text-1: #e2e8f0;
    --text-2: #cbd5e1;
    --text-3: #94a3b8;
    --border: rgba(148, 163, 184, 0.18);
    --border-strong: rgba(56, 189, 248, 0.42);
    --shadow: 0 24px 60px rgba(2, 6, 23, 0.30);
    --shadow-hover: 0 28px 70px rgba(2, 6, 23, 0.40);
    --accent: #38bdf8;
    --accent-2: #6366f1;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

body {
    background: linear-gradient(180deg, var(--bg-0) 0%, var(--bg-1) 24%, var(--bg-2) 100%);
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(59, 130, 246, 0.24), transparent 22%),
        radial-gradient(circle at top right, rgba(16, 185, 129, 0.16), transparent 20%),
        linear-gradient(180deg, var(--bg-0) 0%, var(--bg-1) 24%, var(--bg-2) 100%);
    color: var(--text-1);
}

header[data-testid="stHeader"] {
    background: rgba(5, 8, 22, 0.72);
    backdrop-filter: blur(18px);
    border-bottom: 1px solid rgba(148, 163, 184, 0.12);
    height: 3.5rem;
}

header[data-testid="stHeader"] * {
    color: var(--text-1) !important;
}

div[data-testid="stToolbar"] {
    top: 0.5rem;
    right: 0.75rem;
    gap: 0.35rem;
    padding: 0.35rem 0.5rem;
    border-radius: 999px;
    border: 1px solid rgba(148, 163, 184, 0.14);
    background: rgba(15, 23, 42, 0.72);
    backdrop-filter: blur(14px);
    box-shadow: 0 12px 28px rgba(2, 6, 23, 0.24);
}

div[data-testid="stToolbar"] button,
div[data-testid="stToolbar"] a,
div[data-testid="stToolbar"] svg {
    color: var(--text-1) !important;
    fill: var(--text-1) !important;
    opacity: 1 !important;
}

div[data-testid="stToolbar"] button,
button[kind="header"],
button[data-testid="baseButton-header"],
.stDeployButton button {
    min-height: 2rem !important;
    min-width: 2rem !important;
    padding: 0.45rem 0.7rem !important;
    border-radius: 999px !important;
    border: 1px solid rgba(148, 163, 184, 0.16) !important;
    background: rgba(15, 23, 42, 0.82) !important;
    color: var(--text-1) !important;
    cursor: pointer !important;
    transition: transform 0.18s ease, border-color 0.18s ease, background-color 0.18s ease, box-shadow 0.18s ease, opacity 0.18s ease;
    box-shadow: 0 10px 24px rgba(2, 6, 23, 0.18);
}

div[data-testid="stToolbar"] button:hover,
button[kind="header"]:hover,
button[data-testid="baseButton-header"]:hover,
.stDeployButton button:hover {
    background: rgba(30, 41, 59, 0.96) !important;
    border-color: rgba(56, 189, 248, 0.48) !important;
    transform: translateY(-1px);
    box-shadow: 0 14px 30px rgba(2, 6, 23, 0.28);
}

div[data-testid="stToolbar"] button:focus-visible,
button[kind="header"]:focus-visible,
button[data-testid="baseButton-header"]:focus-visible,
.stDeployButton button:focus-visible,
.stButton > button:focus-visible,
.stSelectbox [data-baseweb="select"] > div:focus-within,
.stNumberInput input:focus-visible {
    outline: 3px solid rgba(56, 189, 248, 0.55) !important;
    outline-offset: 2px !important;
    box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.15) !important;
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

.hero-shell,
.panel,
div[data-testid="stForm"],
.result-card,
.metric-card,
.sidebar-brand,
.stAlert {
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
}

.hero-shell {
    padding: 2rem 2.2rem;
    border-radius: 30px;
    background: linear-gradient(135deg, rgba(8, 15, 31, 0.96), rgba(17, 24, 39, 0.92));
    color: var(--text-1);
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
    pointer-events: none;
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
    color: var(--text-0);
}

.hero-copy {
    max-width: 760px;
    color: var(--text-2);
    font-size: 1.02rem;
    line-height: 1.8;
}

.metric-card {
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.88), rgba(17, 24, 39, 0.88));
    backdrop-filter: blur(10px);
    border-radius: 22px;
    padding: 1.05rem 1.15rem;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}

.metric-card:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow-hover);
    border-color: rgba(56, 189, 248, 0.32);
}

.metric-label {
    font-size: 0.76rem;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    color: var(--text-3);
    font-weight: 700;
}

.metric-value {
    font-size: 1.45rem;
    font-weight: 800;
    color: var(--text-0);
    margin-top: 0.25rem;
}

.panel {
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(17, 24, 39, 0.94));
    border-radius: 28px;
    padding: 1.6rem;
}

div[data-testid="stForm"] {
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(17, 24, 39, 0.94));
    border-radius: 28px;
    padding: 1.4rem;
}

.panel h3 {
    color: var(--text-0);
    font-weight: 800;
    letter-spacing: -0.03em;
}

.section-copy {
    color: var(--text-2);
    margin-top: 0.25rem;
}

.stSelectbox label, .stNumberInput label {
    font-weight: 700 !important;
    color: var(--text-1) !important;
    font-size: 0.92rem !important;
    letter-spacing: 0.01em;
}

.stSelectbox div[data-baseweb="select"] > div,
.stNumberInput input,
.stNumberInput [data-baseweb="input"] {
    background-color: #0f172a !important;
    border: 1px solid rgba(148, 163, 184, 0.24) !important;
    border-radius: 14px !important;
    min-height: 3.1rem !important;
    box-shadow: none !important;
    color: var(--text-1) !important;
}

.stSelectbox [data-baseweb="select"] * {
    color: var(--text-1) !important;
    opacity: 1 !important;
}

.stSelectbox [data-baseweb="select"] svg {
    fill: var(--text-2) !important;
}

.stSelectbox [data-baseweb="popover"] {
    border-radius: 14px !important;
    overflow: hidden !important;
}

.stSelectbox [data-baseweb="menu"] {
    background: #0f172a !important;
}

.stSelectbox [role="option"] {
    color: var(--text-1) !important;
    background: #0f172a !important;
}

.stSelectbox [role="option"][aria-selected="true"],
.stSelectbox [role="option"]:hover {
    background: rgba(59, 130, 246, 0.18) !important;
    color: var(--text-1) !important;
}

.stSelectbox [data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
.stSelectbox [data-baseweb="select"] input,
.stNumberInput input {
    color: var(--text-1) !important;
    -webkit-text-fill-color: var(--text-1) !important;
}

.stNumberInput [data-baseweb="input"] {
    background: #0f172a !important;
}

.stNumberInput button {
    background: #1e293b !important;
    color: var(--text-0) !important;
    border: none !important;
    border-radius: 12px !important;
    cursor: pointer !important;
}

.stNumberInput button:hover {
    background: #334155 !important;
}

.stNumberInput button svg {
    fill: var(--text-0) !important;
}

.stSelectbox div[data-baseweb="select"] > div:hover,
.stNumberInput input:hover {
    border-color: var(--border-strong) !important;
}

.stButton {
    width: 100%;
}

.stButton > button {
    width: 100%;
    padding: 0.92rem 1.2rem;
    border-radius: 14px;
    background: linear-gradient(135deg, var(--accent), var(--accent-2));
    color: var(--text-0) !important;
    font-weight: 800;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    box-shadow: 0 18px 35px rgba(59, 130, 246, 0.24);
    cursor: pointer !important;
    appearance: none;
    -webkit-appearance: none;
    -webkit-tap-highlight-color: transparent;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, filter 0.18s ease, background-position 0.18s ease;
    background-size: 120% 120%;
    background-position: center;
}

.stButton > button:hover {
    transform: translateY(-1px);
    border-color: rgba(255, 255, 255, 0.18) !important;
    box-shadow: 0 24px 50px rgba(99, 102, 241, 0.30);
    filter: brightness(1.03);
}

.stButton > button:active {
    transform: translateY(0);
    filter: brightness(0.98);
}

.stButton > button:focus:not(:focus-visible) {
    outline: none !important;
    box-shadow: 0 18px 35px rgba(59, 130, 246, 0.24);
}

.result-card {
    border-radius: 24px;
    padding: 1.25rem 1.35rem;
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.10), rgba(59, 130, 246, 0.10));
    color: var(--text-1);
}

.result-value {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: var(--text-0);
}

.sidebar-brand {
    padding: 1.1rem 1rem 1.5rem;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.18), rgba(124, 58, 237, 0.14));
    margin-bottom: 1rem;
}

.sidebar-brand h4 {
    margin: 0;
    font-size: 1.05rem;
    font-weight: 800;
    color: var(--text-1);
}

.sidebar-brand p {
    margin: 0.35rem 0 0;
    color: var(--text-3);
    font-size: 0.88rem;
}

.stSidebar {
    background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
}

.stSidebar label, .stSidebar p, .stSidebar span {
    color: var(--text-1) !important;
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
    color: var(--text-3);
    font-size: 0.9rem;
    padding: 1.25rem 0 0.75rem;
}

.stAlert {
    background: rgba(15, 23, 42, 0.96) !important;
    color: var(--text-1) !important;
    border-radius: 16px !important;
}

.stAlert p, .stAlert div, .stAlert span {
    color: var(--text-1) !important;
}

@media (max-width: 900px) {
    section.main > div.block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-shell,
    .panel,
    div[data-testid="stForm"] {
        padding: 1.2rem;
        border-radius: 22px;
    }

    .metric-value {
        font-size: 1.2rem;
    }
}

@media (max-width: 576px) {
    section.main > div.block-container {
        padding-top: 0.75rem;
        padding-bottom: 1.25rem;
    }

    .hero-title {
        font-size: clamp(1.75rem, 9vw, 2.4rem);
    }

    .hero-copy {
        font-size: 0.98rem;
        line-height: 1.7;
    }

    .stButton > button {
        width: 100%;
    }

    div[data-testid="stToolbar"] {
        top: 0.35rem;
        right: 0.45rem;
        padding: 0.25rem 0.4rem;
    }
}
</style>
"""


st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


def inject_styles() -> None:
    st.markdown(APP_CSS,
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
    submitted = st.form_submit_button("Predict Score", use_container_width=True, type="primary")

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
