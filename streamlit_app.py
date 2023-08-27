import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('Omega 3 & Blueberry Oatmeal😊😊😊😊😊😊😊😊☆*: .｡. o(≧▽≦)o .｡.:*☆🤣😂')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-boiled Free-range Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)
