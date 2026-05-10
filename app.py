import streamlit as st
from groq import Groq
import streamlit.components.v1 as components

# ---------------- API ----------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- PAGE ----------------

st.set_page_config(page_title="AI Voice Chatbot")

# ---------------- STYLE ----------------

st.markdown("""
<style>

.stApp{
    background-color:#F8C8DC;
    color:white;
}
h1{
    color:#22C55E;
    text-align:center;
}

.stButton button{
    background-color:#22C55E;
    color:white;
    border-radius:10px;
    height:50px;
    width:100%;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🤖 AI Voice Chatbot")

# ---------------- INPUT ----------------

user_input = st.text_input("Ask Anything")

# ---------------- BUTTON ----------------

if st.button("Send"):

    if user_input != "":

        # AI RESPONSE
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        answer = completion.choices[0].message.content

        # SHOW ANSWER
        st.success(answer)

        # SPEAK ANSWER
        components.html(
            f"""
            <script>
            const text = `{answer}`;

            const speech = new SpeechSynthesisUtterance(text);

            speech.lang = "en-US";
            speech.volume = 1;
            speech.rate = 1;
            speech.pitch = 1;

            window.speechSynthesis.speak(speech);
            </script>
            """,
            height=0,
        )

    else:
        st.warning("Please enter something")
