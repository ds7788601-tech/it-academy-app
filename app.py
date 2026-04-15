import streamlit as st
from openai import OpenAI
import os

# ===== CONFIG =====
st.set_page_config(page_title="IT Academy Pro", page_icon="💻", layout="wide")

# ===== API KEY =====
client = OpenAI(api_key="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")
# ===== LANGUAGE =====
lang = st.sidebar.selectbox("🌍 Language / Язык", ["RU", "EN"])

# ===== TEXTS =====
texts = {
    "RU": {
        "menu": ["🏠 Главная", "📚 Курсы", "🤖 AI Ассистент", "📞 Контакты"],
        "title": "💻 IT Academy Pro",
        "subtitle": "Стань разработчиком будущего",
        "chat_title": "🤖 Умный AI-консультант",
        "input": "Задай вопрос...",
    },
    "EN": {
        "menu": ["🏠 Home", "📚 Courses", "🤖 AI Assistant", "📞 Contact"],
        "title": "💻 IT Academy Pro",
        "subtitle": "Become a developer of the future",
        "chat_title": "🤖 Smart AI Assistant",
        "input": "Ask anything...",
    }
}

t = texts[lang]

# ===== HEADER =====
st.title(t["title"])
st.caption(t["subtitle"])

# ===== MENU =====
menu = st.sidebar.radio("Menu", t["menu"])

# ===== HOME =====
if menu == t["menu"][0]:
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475")

    if lang == "RU":
        st.markdown("""
        ## 🚀 Добро пожаловать в IT Academy Pro

        ### 🏫 О нас
        IT Academy Pro — современная онлайн-школа программирования.

        ### 💡 Почему выбирают нас:
        - 👨‍🏫 Наставники из IT
        - 📚 Актуальные технологии (Python, Web, AI)
        - 💼 Помощь с работой
        - 🧠 Практика 80%

        ### 🎯 Наша цель:
        Сделать тебя востребованным разработчиком 🚀
        """)
    else:
        st.markdown("""
        ## 🚀 Welcome to IT Academy Pro

        ### 🏫 About us
        IT Academy Pro is a modern coding school.

        ### 💡 Why choose us:
        - 👨‍🏫 Industry mentors
        - 📚 Modern technologies
        - 💼 Job assistance
        - 🧠 80% practice

        ### 🎯 Our goal:
        Make you job-ready 🚀
        """)

# ===== COURSES =====
elif menu == t["menu"][1]:
    st.header("📚 Courses" if lang=="EN" else "📚 Курсы")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1515879218367-8466d910aaa4")
        st.write("🐍 Python Developer")

        st.image("https://images.unsplash.com/photo-1586717791821-3f44a563fa4c")
        st.write("🎨 UI/UX Design")

    with col2:
        st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085")
        st.write("🌐 Web Development")

        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b")
        st.write("🔐 Cybersecurity")

# ===== AI PAGE =====
elif menu == t["menu"][2]:
    st.header(t["chat_title"])

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input(t["input"])

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        try:
            with st.spinner("🤖 Thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "Ты эксперт IT академии. Помогай выбрать курс и отвечай просто."
                            if lang == "RU"
                            else "You are an IT academy assistant. Help users choose courses."
                        },
                        *st.session_state.messages
                    ]
                )

            reply = response.choices[0].message.content

        except Exception as e:
            reply = f"Ошибка: {e}"

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)

# ===== CONTACT =====
elif menu == t["menu"][3]:
    st.header("📞 Contact")

    name = st.text_input("Name")
    phone = st.text_input("Phone")

    if st.button("Send"):
        st.success("✅ Sent!")