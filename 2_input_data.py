import streamlit as st

st.set_page_config(page_title="Property Input")

st.title("📊 Property Deal Analysis")
st.write("Input your figures below to calculate potential returns.")

with st.form("deal_form"):
    purchase_price = st.number_input("Purchase Price (£)", min_value=0)
    refurb_cost = st.number_input("Estimated Refurbishment Cost (£)", min_value=0)
    arv = st.number_input("After Repair Value (ARV) (£)", min_value=0)
    
    submit_button = st.form_submit_button(label="Analyze Deal")

if submit_button:
    profit = arv - (purchase_price + refurb_cost)
    st.success(f"Estimated Profit: £{profit:,.2f}")
    st.write("---")
    st.info("Want a downloadable report? Visit the Subscribe page.")

