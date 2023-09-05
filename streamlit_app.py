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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

# create function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

import requests
from urllib.error import URLError
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_fuction = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_fuction)
except URLError as e:
  streamlit.error()



streamlit.header("Fruit load list contains:")
import snowflake.connector
#create function 
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row)

streamlit.stop()

fruit_choice_two = streamlit.text_input('Enter another fruit','jackfruit')
streamlit.write('The user entered ', fruit_choice_two)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
