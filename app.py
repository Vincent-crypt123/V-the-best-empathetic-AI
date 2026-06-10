import streamlit as st

st.set_page_config(
    page_title="V",
    page_icon="⚫",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&display=swap');

.stApp {
    background-color: #f4f4f4;
}

.block-container {
    padding-top: 1rem;
}

.settings-btn {
    position: fixed;
    top: 20px;
    right: 30px;
    font-size: 28px;
}

.center-container {
    height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* Шар */

.orb {
    width: 260px;
    height: 260px;
    border-radius: 50%;

    background:
    radial-gradient(
        circle at 40% 30%,
        rgba(255,255,255,0.8),
        rgba(80,80,80,0.3),
        rgba(0,0,0,1)
    );

    box-shadow:
        0 0 40px rgba(0,0,0,0.15);

    animation: pulse 4s infinite;
}

/* Пульсация */

@keyframes pulse {

0% {
transform: scale(1);
}

50% {
transform: scale(1.04);
}

100% {
transform: scale(1);
}

}

.orb-text {

    font-family: 'Caveat', cursive;
    font-size: 42px;

    margin-top: 25px;

    color: #111;
}

</style>
""", unsafe_allow_html=True)

# Настройки

with st.sidebar:

    st.title("⚙ Голосовой движок")

    hf_space = st.text_input(
        "Hugging Face Space",
        value="hexgrad/Kokoro-82M"
    )

    st.button("Сохранить")

# Центральная часть

st.markdown(
"""
<div class="center-container">

    <div class="orb"></div>

    <div class="orb-text">
        кликни чтобы поговорить
    </div>

</div>
""",
unsafe_allow_html=True
)
