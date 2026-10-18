import streamlit as st

# This program is based on video

# st code

# Sidebar
with st.sidebar:
    st.title("About this app")
    st.text("This program is based on ___ video that goes over the creator's opinion of the 10 most critical python skills to learn")
    pass

st.title("Welcome!")
st.text("Today I will be going over 10 important Python concepts to know. Let's get started!")
st.markdown("*Thank you ____ for educating me on a few and inspringing the creation of this app!*")
st.text("")

st.subheader("1: Printing", divider='gray')
st.markdown("Printing, or knowledge of print() is critical in dugging and creating Python programs! Learning print(Hello, world!) is a rite of passage for any beginner learning to code in Python")
st.text("")
st.markdown("*What does print() do?*")
st.markdown("When executed, print() returns whatever is inside of the parenthesis in the console. This could be the result of a function, a simple string like hi, or a message critical to debuging your program. Let's look at the code!")
st.text("")

helloWorld = '''print("Hello, world!")
'''

dogPrint = '''dog = 1
print(dog)
'''

awesomePrint = '''def awesome(lyric):
    awesomeLyrics = ["Everything is awesome!"]
    awesomeLyrics.append(lyric)
    print(awesomeLyrics[0] + " " + awesomeLyrics[1])
    return

awesome("Everything is cool when you are part of a team!")'''

st.code(helloWorld, language="python")
st.code(dogPrint, language="python")
st.code(awesomePrint, language="python")







