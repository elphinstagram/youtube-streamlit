import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# 11-4.expandar
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(F'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!'

# 10-1. 画像表示チェックボックス
# st.write('Display Image')
# if st.checkbox('show image'):
#    img = Image.open('image0.jpeg')
#    st.image(img, caption='sample', use_column_width=True)

# 10-2. Selectbox
# option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1, 11))
#'あなたの好きな数字は、', option, 'です'

# 10-3. テキスト入力
#hobby = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味：', hobby

# 10-4. スライダー
#condition = st.slider('あなたの調子は？', 0, 100, 50)
#'コンディション：', condition

# 11-1.サイドバー
#st.sidebar.write('Interractive Widgets')
#hobby = st.sidebar.text_input('あなたの趣味は？')
#condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

#'あなたの趣味：', hobby
#'コンディション：', condition

# 11-2.2カラム(columns)
# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字列を追加')
# if button:
#     right_column.write('ここは右カラム')

# 11-3.expandar
# expander1 = st.expander('問い合わせ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.expander('問い合わせ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.expander('問い合わせ3')
# expander3.write('問い合わせ3の回答')


# st.write("DataFrame")
# df = pd.DataFrame({
#    '1列目': [1, 2, 3, 4],
#    '2列目': [10, 20, 30, 40]
# })

# df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
# )
# st.dataframe(df.style.highlight_max(axis=0))
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50.50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)


# """
# 章
# 節
# 項

# ```python
#import streamlit as st
#import numpy as np
#import pandas as pd
# ```
# """
