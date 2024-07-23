'''我的首页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('我的好书推荐:《装在口袋里的爸爸》')
    st.write('下面电影哪个是作者想推荐的？')
    cb1 = st.checkbox('A.流浪地球')
    cb2 = st.checkbox('B.爸爸是外星人')
    cb3 = st.checkbox('C.中国机长')
    cb4 = st.checkbox('D.熊出没之狂野大陆')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == True and cb2 == False and cb3 == False and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')
    st.write('---------------------')
    st.write('下面游戏哪个是作者想推荐的？')
    cb1 = st.checkbox('A.王者荣耀')
    cb2 = st.checkbox('B.蛋仔派对')
    cb3 = st.checkbox('C.开心消消乐')
    cb4 = st.checkbox('D.和平精英')
    b2 = st.button('第2题答案')
    if b2:
        if cb1 == False and cb2 == True and cb3 == False and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')
    st.write('---------------------')
    st.write('下面音乐哪个是作者想推荐的？')
    cb1 = st.checkbox('A.踏山河')
    cb2 = st.checkbox('B.莫问归期')
    cb3 = st.checkbox('C.九九八十一')
    cb4 = st.checkbox('D.大香蕉')
    b3 = st.button('第3题答案')
    if b3:
        if cb1 == False and cb2 == False and cb3 == False and cb4 == True:
            st.write('回答正确！')
        else:
            st.write('再想想')
    st.write('---------------------')
    st.write('下面书名哪个是作者想推荐的？')
    cb1 = st.checkbox('A.装在口袋里的爸爸')
    cb2 = st.checkbox('B.三国演义')
    cb3 = st.checkbox('C.爱的教育')
    cb4 = st.checkbox('D.宝葫芦的秘密')
    b4 = st.button('第4题答案')
    if b4:
        if cb1 == True and cb2 == False and cb3 == False and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))

def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')

def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '杨瑾诚':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '李致远':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['杨瑾诚', '李致远'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
