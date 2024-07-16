#python -m streamlit run tutorial.py
import streamlit as st


# Title and header and subheading
st.title('Streamlit Software Academy Tutorial')
st.header('Header')
st.subheader('Subheading')

st.markdown('---')

# Markdown
st.markdown('''
# One Hashtag
            
## Two Hashtags
            
### Three Hashtags
''')

st.markdown('---')

st.markdown('''
- Bullet point 1
- Bullet point 2
''')

st.markdown('''
1. Numbered point 1
2. Numbered point 2
''')

st.markdown('---')

st.markdown('''
- **Bold Word**
- _Italic_
- [Youtube Link](https://www.youtube.com/)
- `Code Indent`
''')

st.markdown('---')


# Interactive Widgets

#slider
number = st.slider('Select a Number Slider', 0, 100, 25)
st.text(f'You selected: {number}')

#radio button
food = ''
food = st.radio('Food Radio Button', ('Pizza', 'Burger', 'Fries'))

#select box
food = ''
food = st.selectbox('Food Select Box', ('Pizza', 'Burger', 'Fries'))

# button
if st.button('Confirm Button'):
    if food == 'Burger':
        st.text(f'You got the correct answer')

st.markdown('---')


# Input widget
name = st.text_input('Enter your name:')
if name:
    st.text(f'Hello, {name}!')

number = st.number_input('Enter a number:', min_value=0, max_value=100, value=50)
st.text(f'You entered: {number}')

message = st.text_area('Enter your message:')
if message:
    st.text(f'Your message: {message}')


#Graphs
m = st.slider('Gradient', -10, 10, 1)
c = st.slider('Y-Intercept', -10, 10, 0)

st.write(f'Equation: y = {m}x + {c}')

st.line_chart([{'x': x, 'y': m*x + c} for x in range(-10, 11)])