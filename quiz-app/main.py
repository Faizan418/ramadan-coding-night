import streamlit as st
import random
import time

#............................... Custom CSS for Stylish UI
st.markdown("""
    <style>
        body {
            # background: linear-gradient(to right, #000, #fff);
            
            color: white;
        }
        .stApp {
            background: linear-gradient(to right, #fff, #000);
        }
        .question-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
            text-align: center;
        }
        .stButton>button {
            background: #ff8c00;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
            width: 100%;
        }
        .stRadio label {
            font-size: 18px;
        }
        .correct {
            color: #fff;
            font-size: 20px;
            font-weight: bold;
        }
        .incorrect {
            color: #FF0000;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🐍 Python Quiz Challenge By Muhammad Faizan... 🚀")

#............................... Quiz questions
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".java", ".txt", ".cpp"],
        "answer": ".py",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def",
    },
    {
        "question": "Which data type is used to store a sequence of characters in Python?",
        "options": ["int", "str", "list", "bool"],
        "answer": "str",
    },
    {
        "question": "How do you start a comment in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#",
    },
    {
        "question": "Which function is used to get input from the user in Python?",
        "options": ["print()", "input()", "get()", "read()"],
        "answer": "input()",
    },
    {
        "question": "What will be the output of `print(3 * 'hello')`?",
        "options": ["hellohellohello", "hello  hello  hello", "error", "hello*3"],
        "answer": "hellohellohello",
    },
    {
        "question": "Which of the following is a valid variable name in Python?",
        "options": ["2var", "my_var", "my-var", "my var"],
        "answer": "my_var",
    },
    {
        "question": "Which symbol is used for exponentiation in Python?",
        "options": ["^", "**", "//", "*"],
        "answer": "**",
    },
    {
        "question": "What will be the output of `print(type(10))`?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "Error"],
        "answer": "<class 'int'>",
    },
    {
        "question": "Which keyword is used to create a loop in Python?",
        "options": ["loop", "repeat", "for", "do"],
        "answer": "for",
    },
]

#.............................. Initialize session state for quiz
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.score = 0
    st.session_state.question_count = 1

question = st.session_state.current_question

#.............................. Progress Bar
st.progress(st.session_state.question_count / len(questions))

#.............................. Stylish Card for Question
st.markdown(f'<div class="question-card"><h3>{question["question"]}</h3></div>', unsafe_allow_html=True)

#.............................. Options
selected_option = st.radio("Choose your answer:", question["options"], key="answer")

#.............................. Submit Button
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.markdown('<p class="correct">✅ Correct!</p>', unsafe_allow_html=True)
        st.session_state.score += 1
    else:
        st.markdown(f'<p class="incorrect">❌ Incorrect! Correct answer is: {question["answer"]}</p>', unsafe_allow_html=True)

    time.sleep(2)

    if st.session_state.question_count < len(questions):
        st.session_state.current_question = random.choice(questions)
        st.session_state.question_count += 1
        st.rerun()
    else:
        st.write(f"🎉 **Quiz Completed!** Your Score: {st.session_state.score}/{len(questions)}")
