import streamlit as st

st.set_page_config(page_title="Subscribe")

st.title("🚀 Go Pro")
st.write("Unlock full reports, PDF exports, and advanced analysis tools.")

# Replace the URL below with your actual LIVE Stripe Payment Link
stripe_url = "https://buy.stripe.com/your_live_link_here"

st.link_button("Subscribe for £39/month", url=stripe_url)

st.write("---")
st.markdown("### Why Subscribe?")
st.markdown("* ✅ Unlimited deal analysis")
st.markdown("* ✅ Downloadable/Editable PDF reports")
st.markdown("* ✅ Priority support")