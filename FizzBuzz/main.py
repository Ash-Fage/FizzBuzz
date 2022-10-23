# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st

def inputs():
    st.sidebar.header('FizzBuzz Inputs')
    start = int(round(st.sidebar.number_input('Start')))
    stop = int(round(st.sidebar.number_input('Stop')))
    run = st.sidebar.button('Run')
    return start, stop, run


def count(start, stop):
    st.header(f'FizzBuzz ({start}-{stop})')
    if start < stop:
        for x in range(start, (stop + 1)):
            fizzBuzz(x)
    elif stop > start:
        for x in range(start, (stop + 1), -1):
            fizzBuzz(x)
    else:
        fizzBuzz(start)


def fizzBuzz(num):
    if num == 0:
        st.markdown(f'{num}')
    elif num % 3 == 0 and num % 5 == 0:
        st.markdown('FizzBuzz')
    elif num % 3 == 0:
        st.markdown('Fizz')
    elif num % 5 == 0:
        st.markdown('Buzz')
    else:
        st.markdown(f'{num}')


def main():
    start, stop, button = inputs()
    if button:
        count(start, stop)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/'''