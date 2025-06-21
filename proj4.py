import streamlit as st
st.header("Management System")
st.subheader("Hotel Project")
menu={
    'pizza':150,
    'passta':80,
    'burgger':60,
    'coldring':70,
    'cake':200,
    'maggi':120,
    'momos':50,
    'panner curry':220,
    'luchha pharatha':25,
    'chikken curry':270,
    'chawal':40
}

light_orange = "#FFDAB9"  

st.markdown(
      f"""
    <style>
    .stApp {{
        background-color: {light_orange};
    }}
    [data-testid="stSidebar"] {{
        background-color: #90EE90 !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.write("wlcome to the hostel project")
st.sidebar.selectbox("menu for snaks:",["pizza : Rs150"," passta : Rs80"," burgger : Rs60","coldring : Rs70","cake : Rs200","maggi : Rs120","momos : Rs50"])
st.sidebar.selectbox("menu for dinner and lunch:",["panner curry : Rs220","luchha pharatha : 1pice : Rs25","chikken curry : Rs270","chawal : fullplate : Rs40"])
sum=0
item=st.text_input("Enter the item you want:")
if item in menu:
    sum=sum+menu[item]
    st.write(f"your item {item} has been added to your order")
else:
    st.write(f"order item {item} not avaliable yet")
another_item=st.text_input("do you want anything else? (Yes/No)")
if another_item=='Yes':
    item_2=st.text_input("Enter the item you want to order:",)
    if item_2 in menu:
          sum=sum+menu[item_2]
          st.write(f"your item {item_2} has been added to your order")
    else:
       st.write(f"order item {item_2} not avaliable yet")
st.write(f"Total bill is{sum}")