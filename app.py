import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_mortgage(amount, interest_rate, years):
    """
    Calculates monthly payment for a fixed-rate mortgage.
    """
    interest_rate = interest_rate / 100 / 12
    months = years * 12
    monthly_payment = (amount * interest_rate * ((1 + interest_rate) ** months)) / (((1 + interest_rate) ** months) - 1)
    return monthly_payment

def generate_graph(amount, interest_rate, years):
    """
    Generates a graph showing the breakdown between principal and interest payments over the term of the mortgage.
    """
    interest_rate = interest_rate / 100 / 12
    months = years * 12
    balance = amount
    principal_payments = []
    interest_payments = []
    for i in range(months):
        interest_payment = balance * interest_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        principal_payments.append(principal_payment)
        interest_payments.append(interest_payment)
    plt.plot(principal_payments, label='Principal')
    plt.plot(interest_payments, label='Interest')
    plt.xlabel('Month')
    plt.ylabel('Payment')
    plt.title('Breakdown of Monthly Payment')
    plt.legend()
    return plt

st.title('Mortgage Calculator')

# User input
amount = st.slider('Loan Amount', 1000, 1000000, 100000, step=1000)
interest_rate = st.slider('Interest Rate', 0.1, 20.0, 3.0, step=0.1)
years = st.slider('Number of Years', 1, 30, 15)
user_string = st.text_input("Please enter your text: ")
question = "What is the capital of France?"
options = ["London", "Paris", "Berlin", "Madrid"]
radio_results = st.radio(question, options)

# Calculate monthly payment
monthly_payment = calculate_mortgage(amount, interest_rate, years)
st.write(f'Monthly Payment: ${monthly_payment:.2f}')

# Print out what the user wrote in the string:
st.write(f'Hello! You wrote: ' + user_string)
st.write(f'In your multiple choice, you chose \"' + radio_results + '\"')

# Generate monthly breakdown graph
interest_rate = interest_rate / 100 / 12
months = years * 12
balance = amount
principal_payments = []
interest_payments = []
for i in range(months):
    interest_payment = balance * interest_rate
    principal_payment = monthly_payment - interest_payment
    balance -= principal_payment
    principal_payments.append(principal_payment)
    interest_payments.append(interest_payment)
plt.figure()
plt.plot(principal_payments, label='Principal')
plt.plot(interest_payments, label='Interest')
plt.xlabel('Month')
plt.ylabel('Payment')
plt.title('Monthly Breakdown of Payment')
plt.legend()
st.pyplot(plt)

##################################
# Recommendations Grid
##################################

# Data for the grid: list of tuples (image_url, website_url)
images_and_links = [
    ("https://i.etsystatic.com/7970370/r/il/d9788c/2776582855/il_1588xN.2776582855_k32i.jpg",
     "https://www.etsy.com/listing/502957237"),
    ("https://i.etsystatic.com/30464579/r/il/29c153/5639149372/il_1588xN.5639149372_b1w9.jpg",
     "https://www.etsy.com/listing/1029698212"),
    ("https://i.etsystatic.com/17924119/r/il/72fa87/5639509410/il_1588xN.5639509410_t71z.jpg",
     "https://www.etsy.com/listing/1649579005/leather-key-chain-customized-photo"),
    ("https://i.etsystatic.com/37999343/r/il/789b13/6338249436/il_1588xN.6338249436_k67m.jpg",
     "https://www.etsy.com/listing/1447055688/"),
    ("https://i.etsystatic.com/53656034/r/il/c455bd/6424951083/il_1588xN.6424951083_4fub.jpg",
     "https://www.etsy.com/listing/1801107854"),
    ("https://i.etsystatic.com/53656034/r/il/03696b/6374145428/il_1588xN.6374145428_qkr7.jpg",
     "https://www.etsy.com/listing/1814758383"),
    ("https://i.etsystatic.com/37999343/r/il/789b13/6338249436/il_1588xN.6338249436_k67m.jpg",
     "https://www.etsy.com/listing/1447055688"),
    ("https://i.etsystatic.com/18415225/r/il/cbce1f/3111321608/il_1588xN.3111321608_9tyh.jpg",
     "https://www.etsy.com/listing/1013029260"),
    ("https://i.etsystatic.com/8249326/r/il/288949/4523029659/il_1588xN.4523029659_cf0b.jpg",
     "https://www.etsy.com/listing/1231189859"),
    ("https://i.etsystatic.com/11874839/r/il/27db28/6287380030/il_1588xN.6287380030_hkpy.jpg",
     "https://www.etsy.com/listing/625147129"),
]

st.title("2x5 Image Grid")

# Create a 2x5 grid
cols = st.columns(5)
for idx, (image_url, website_url) in enumerate(images_and_links):
    with cols[idx % 5]:  # Cycle through columns
        st.markdown(
            f'<a href="{website_url}" target="_blank">'
            f'<img src="{image_url}" style="width:100%; border-radius:10px;"></a>',
            unsafe_allow_html=True,
        )
    if (idx + 1) % 5 == 0:  # Add a new row every 5 images
        cols = st.columns(5)
