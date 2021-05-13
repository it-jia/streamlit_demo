import time
import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
    page_title="自定義網頁標題",
    page_icon="😁",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title('My first app')

st.write("## 子標題")

'### 第三層標題'

st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

if st.checkbox('顯示地圖資料'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.7, 120.4],
        columns=['lat', 'lon'])
    st.map(map_data)


option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected:', option

# 左右排列
left_column, right_column = st.beta_columns(2)

pressed = left_column.button('不要按!')
if pressed:
    left_column.write("就叫你不要按了!")

with right_column:
    chosen = st.radio(
        '你住在哪裡？',
        ("地球", "月亮", "火星"))
    st.write(f"我是 {chosen} 人！！")

expander = st.beta_expander("FAQ")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式...")

# # 增加一個空白元件，等等要放文字
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#     latest_iteration.text(f'目前進度 {i+1} %')
#     bar.progress(i + 1)
#     time.sleep(0.1)


with st.form(key='my_form'):
    name = text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'hello {name}')




# st.video('https://www.youtube.com/watch?v=0rp3pP2Xwhs', start_time=100)



# st.title('My title')
# st.header('My header')
# st.subheader('My sub')
# st.text('Fixed width text')
# st.markdown('_Markdown_')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.code('for i in range(8):\n    foo()')

# st.button('Hit me')
# st.checkbox('Check me out')
# st.radio('Radio', [1,2,3])
# st.selectbox('Select', [1,2,3])
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)
# st.select_slider('Slide to select', options=[1,'2'])
# st.text_input('Enter some text')
# st.number_input('Enter a number')
# st.text_area('Area for textual entry')
# st.date_input('Date input')
# st.time_input('Time entry')
# st.file_uploader('File uploader')
# st.color_picker('Pick a color')