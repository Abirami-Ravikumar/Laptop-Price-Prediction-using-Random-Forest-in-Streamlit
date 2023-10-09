# Importing Libraries
from PIL import Image
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# from bs4 import BeautifulSoup
# Call set_page_config() as the first Streamlit command in your script
st.set_page_config(page_title="Laptop Prediction",
                   page_icon=":smiley:", layout="wide")

st.title("Laptop Price Prediction")

# Define the navigation buttons
nav = st.sidebar.radio(
    "Navigation", ["Home", "Flowchart", "EDA", "Prediction"])

# Define the content to display based on the selected button
if nav == "Home":
    st.write("Welcome to the Home page!")
    # st.image("l1.jpg", caption="Home Image", use_column_width=True)
    img = Image.open("images/l1.jpg")
    # Resize the image to a specified width and height
    new_width = 1400
    new_height = 600
    img = img.resize((new_width, new_height))

    # Display the resized image
    st.image(img)
elif nav == "Flowchart":
    st.write("Architecture Diagram!")
    img = Image.open("images/arc.png")
    # Resize the image to a specified width and height
    new_width = 1400
    new_height = 700
    img = img.resize((new_width, new_height))

    # Display the resized image
    st.image(img)
elif nav == "EDA":
    st.write("Welcome to the EDA page!")
    if st.sidebar.button("os"):
        os_image = Image.open("images/os-image.png")
        new_width = 400
        new_height = 400
        img = os_image.resize((new_width, new_height))
        st.image(os_image)
        st.header("How does OS affects the price?")
        st.write(
            "Laptops with MacOS have greater median cost compared to any other laptops.")
        st.write(
            "Laptops with Android Operating systems are less costly compared to other operating systems.")
        st.write(
            "The range of price is greatest for Windows 10 laptop and least for Android laptops.")

    if st.sidebar.button("company"):
        company_image = Image.open("images/company-image.png")
        new_width = 500
        new_height = 500
        img = company_image.resize((new_width, new_height))
        st.image(company_image)
        st.header("How does Company/ brand affects the price?")
        st.write(
            "The company with the highest average price is laptops is RAZER with Rs.1,78,282.")
        st.write(
            "The company with the lowest average price is laptops is VERO with Rs.11,584.4.")
        st.write("The company closest to the middle average price Rs.89,386.1.")

    if st.sidebar.button("cpu"):
        cpu_image = Image.open("images/cpu-image.png")
        new_width = 500
        new_height = 500
        img = cpu_image.resize((new_width, new_height))
        st.image(cpu_image)
        st.header("How does CPUaffects the price?")
        st.write(
            "Laptops with Intel Core i7 have a greater median cost compared to any other laptops.")
        st.write(
            "Laptops with Intel Other (Intel, Atom, Celeron) are less costly compared to other CPUs.")
        st.write("The range of price is greatest for Intel Core i7. It is least for Intel Core i3 and Laptops in the other category.")

    if st.sidebar.button("ram"):
        ram_image = Image.open("images/ram-image.png")
        new_width = 500
        new_height = 500
        img = ram_image.resize((new_width, new_height))
        st.image(ram_image)
        st.header("How does RAM affects the price?")
        st.write("Laptops with a RAM of 32 have the highest median price.")
        st.write("Laptops with a RAM of 2 have the lowest median price.")
        st.write("The range of price is greatest for laptops with a RAM of 32, and the smallest for laptops with a RAM of 64.")

    if st.sidebar.button("gpu"):
        gpu_image = Image.open("images/gpu-image.png")
        new_width = 500
        new_height = 500
        img = gpu_image.resize((new_width, new_height))
        st.image(gpu_image)
        st.header("How does GPU affects the price?")
        st.write(
            "Laptops with Nvidia have a greater median cost compared to any other laptops.")
        st.write("Laptops with ARM to AMD are less costly compared to other GPUs.")
        st.write(
            "the range of price is greatest for Nvidia GPU and least for ARM and AMD GPU.")

elif nav == "Prediction":
    st.write("Welcome to the Prediction page!")

    # --------------------------------------------------------PREDICTION SYSTEM----------------------------------------
    # import model
    #pipe = pickle.load(open('pipe.pkl', 'rb'))
    pipe = pd.compat.pickle_compat.load(open('pipe.pkl','rb')) 
    #df = pickle.load(open('df.pkl', 'rb'))
    df = pd.compat.pickle_compat.load(open('df.pkl','rb')) 

    st.markdown("Just fill out the specifications your need for you laptop and hit the 'Predict Price' button, and voila! You get the estimated price for the laptop.")

    # brand
    company = st.selectbox('Brand', df['Company'].unique())

    # type of laptop
    type = st.selectbox('Type', df['Type Name'].unique())

    # Ram
    ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

    # weight
    weight = st.selectbox(
        'Weight (in KG)', [1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00])

    # Touchscreen
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

    # IPS
    ips = st.selectbox('IPS', ['No', 'Yes'])

    # screen size
    screen_size = st.selectbox('Screen Size (in Inches)', [13, 14, 15.6, 17.3])

    # resolution
    resolution = st.selectbox('Screen Resolution',
                              ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                               '2560x1440', '2304x1440'])

    # cpu
    cpu = st.selectbox('CPU', df['CPU Brand'].unique())

    hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

    ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

    gpu = st.selectbox('GPU Brand', df['GPU Brand'].unique())

    os = st.selectbox('OS', df['OS'].unique())

    if st.button('Predict Price'):
        # query
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
        query = np.array([company, type, ram, weight,
                         touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

        query = query.reshape(1, 12)
        st.title("The predicted price of this configuration is " +
                 str(int(np.exp(pipe.predict(query)[0]))))
