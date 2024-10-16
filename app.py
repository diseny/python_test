import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 제목과 설명
st.title("Scatter Plot Example using Streamlit")
st.write("This is a simple scatter plot generated using Matplotlib and displayed using Streamlit.")

# 데이터 생성
x = np.random.rand(50)
y = np.random.rand(50)

# Matplotlib을 사용한 산포도 그리기
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title("Simple Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Streamlit에서 Matplotlib 그래프 표시
st.pyplot(fig)
