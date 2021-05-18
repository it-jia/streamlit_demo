import time
import streamlit as st
import numpy as np
import pandas as pd


# 網頁配置設定(要寫在所有 Streamlit 命令之前，而且只能設定一次)
st.set_page_config(
    page_title="自定義網頁標題",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# 加入標題
st.title('我的第一個應用程式')


# 使用 Magic commands 指令，顯示 Markdown
st.write("嘗試創建**表格**：")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
# 單行只有變數，不需要使用 st.write()，它會自動套用
df


# 繪製折線圖
# 使用 Numpy 生成一個隨機樣本，然後將其繪製成圖表。
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# 使用複選框顯示/隱藏數據
if st.checkbox('顯示地圖圖表'):
    # 繪製地圖
    # 使用 Numpy 生成一個隨機樣本，繪製到地圖上。
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
        columns=['lat', 'lon'])
    st.map(map_data)

# 使用選擇框進行選擇(選擇框移至側邊欄中)
option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
'你的答案：', option

'---'

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

# 隱藏大量內容來節省空間。
expander = st.beta_expander("點擊來展開...")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")


# 加入進度條
# 增加一個空白元件，等等要放文字
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#     latest_iteration.text(f'目前進度 {i+1} %')
#     bar.progress(i + 1)
#     time.sleep(0.1)


@st.cache(suppress_st_warning=True)
def expensive_computation(a):
    st.write(f"沒有快取：expensive_computation({a})")
    time.sleep(2)
    return a * 2

a = st.slider("選擇一個數字", 0, 10)
result = expensive_computation(a)
st.write("結果：", result)


# 更多元件請參考官方說明：https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
# st.title('My title')
# st.header('My header')
# st.subheader('My sub')
# st.text('Fixed width text')
# st.markdown('_Markdown_')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.code('for i in range(8):\n    foo()')
# st.video('https://www.youtube.com/watch?v=0rp3pP2Xwhs', start_time=100)

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
