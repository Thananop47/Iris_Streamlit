import streamlit as st
st.title('MY first Streamlit app')
st.write('Hello, Streamlit')
tab1, tab2 = st.tabs(['Name','Calculator'])
with tab1:
    name = st.text_input('Enter your name: ')
    if name:
        st.success(f'Welcome, {name}!')

with tab2:
    st.title('Calculator app')
    st.write('Hello, Streamlit!')
    col1, col2, col3 = st.columns(3)

    with col1:
        num1 = st.text_input('num1')

    with col2: 
        operator = st.selectbox('Operator', ('+','-','x','/'),index=None,placeholder="Select operator",accept_new_options=True)

    with col3:
        num2 = st.text_input('num2')

    if st.button('Calculate'):
        try:
            n1 = float(num1)
            n2 = float(num2)

            if operator == '+':
                result = n1 + n2
            elif operator == '-':
                result = n1 - n2
            elif operator == 'x':
                result = n1 * n2
            elif operator == '/':
                if n2 == 0:
                    st.error('Can not devide by 0')
                    result = None
                else:
                    result = n1 / n2
            else:
                st.warning('please select operator')
                result = None

            if result is not None:
                st.success(f'result = {result}')

        except ValueError:
            st.error('กรุณาใส่ตัวเลขให้ถูกต้อง')



