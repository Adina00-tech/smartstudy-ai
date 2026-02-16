
import streamlit as st
st.set_page_config(page_title="SmartStudy AI", layout="centered")
import sympy as sp

st.set_page_config(page_title="SmartStudy AI", layout="centered")

st.title("🧠 SmartStudy AI")
st.write("School Multi-Subject Learning Platform")

subject = st.selectbox(
    "Выберите предмет:",
    ["Математика", "Английский", "Физика", "Русский язык"]
)

# ================== МАТЕМАТИКА ==================
if subject == "Математика":
    st.header("Математика")

    mode = st.radio(
        "Выберите режим:",
        ["Решить пример", "Решить уравнение", "Теория"]
    )

    if mode == "Решить пример":
        expr = st.text_input("Введите пример (например: 2+3 или 5*6):")
        if st.button("Решить"):
            try:
                result = eval(expr)
                st.success(f"Ответ: {result}")
            except:
                st.error("Ошибка. Проверь формат.")

    elif mode == "Решить уравнение":
        eq = st.text_input("Введите уравнение (например: 2*x+5=15)")
        if st.button("Решить уравнение"):
            try:
                x = sp.symbols('x')
                left, right = eq.split("=")
                equation = sp.Eq(eval(left), eval(right))
                solution = sp.solve(equation, x)
                st.success(f"Ответ: x = {solution}")
            except:
                st.error("Проверьте формат.")

    elif mode == "Теория":
        topic = st.selectbox(
            "Выберите тему:",
            ["Линейные уравнения", "Квадратные уравнения", "Степени", "Корни", "Проценты"]
        )

        if topic == "Линейные уравнения":
            st.write("""
ax + b = c

Шаги:
1. Перенести b
2. Разделить на a
""")

        if topic == "Квадратные уравнения":
            st.write("""
ax² + bx + c = 0

D = b² - 4ac

x = (-b ± √D) / (2a)
""")

        if topic == "Степени":
            st.write("""
a^m * a^n = a^(m+n)
(a^m)^n = a^(mn)
""")

        if topic == "Корни":
            st.write("""
√a — число, которое в квадрате даёт a.
√(a + b) ≠ √a + √b
""")

        if topic == "Проценты":
            st.write("""
Чтобы найти процент:
20% от 50 = 50 * 0.2
""")

# ================== АНГЛИЙСКИЙ ==================
elif subject == "Английский":
    st.header("English Grammar")

    topic = st.selectbox(
        "Choose topic:",
        ["Present Simple", "Past Simple",
         "Present Perfect", "Conditionals",
         "Passive Voice", "Modal Verbs",
         "Advanced C1-C2"]
    )

    grammar = {
        "Present Simple": """
Used for habits and facts.

Structure:
I play
He plays
""",
        "Past Simple": """
Used for finished past actions.

Structure:
Subject + V2
""",
        "Present Perfect": """
Have/has + V3

Used for experience and unfinished time.
""",
        "Conditionals": """
Zero: facts
First: real future
Second: unreal present
Third: unreal past
""",
        "Passive Voice": """
Be + V3
The book was written.
""",
        "Modal Verbs": """
Can, Could, Must, Should, Might.
""",
        "Advanced C1-C2": """
Inversion:
Never have I seen...

Cleft sentences:
It was John who...
"""
    }

    st.write(grammar[topic])

# ================== ФИЗИКА ==================
elif subject == "Физика":
    st.header("Физика")

    topic = st.selectbox(
        "Выберите тему:",
        ["Законы Ньютона", "Скорость", "Работа", "Энергия", "Закон Ома"]
    )

    physics = {
        "Законы Ньютона": """
1 закон — инерция
2 закон — F = ma
3 закон — действие равно противодействию
""",
        "Скорость": """
v = s / t
""",
        "Работа": """
A = F * s
""",
        "Энергия": """
Потенциальная: E = mgh
Кинетическая: E = mv² / 2
""",
        "Закон Ома": """
I = U / R
"""
    }

    st.write(physics[topic])

# ================== РУССКИЙ ==================
elif subject == "Русский язык":
    st.header("Русский язык")

    topic = st.selectbox(
        "Выберите тему:",
        ["Падежи", "Времена глагола", "Синонимы", "Антонимы", "Омонимы"]
    )

    russian = {
        "Падежи": """
И.п — кто? что?
Р.п — кого? чего?
Д.п — кому? чему?
В.п — кого? что?
Т.п — кем? чем?
П.п — о ком? о чём?
""",
        "Времена глагола": """
Прошедшее
Настоящее
Будущее
""",
        "Синонимы": "Слова близкие по значению.",
        "Антонимы": "Слова противоположные по значению.",
        "Омонимы": "Слова одинаковые по звучанию, но разные по значению."
    }

    st.write(russian[topic])