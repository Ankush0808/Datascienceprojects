import streamlit as st
import pandas as pd
import pickle
import json
import plotly.graph_objects as go
import plotly.express as px
import math

# --- Add background image using custom CSS ---
def add_bg_image(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_path});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """, 
        unsafe_allow_html=True
    )

# Call the function to add the background image
add_bg_image("C:/Users/Lenovo/Risk_image.png")  # Replace with the path to your image

# Cache the state-county mapping loading
@st.cache_data
def load_state_county_map():
    with open(r'C:\Users\Lenovo\state_county_dict.json', 'r') as f:
        return json.load(f)

# Cache the model loading
@st.cache_resource
def load_models(risk_columns):
    models = {}
    for risk_col in risk_columns:
        model_path = f'C:\\Users\\Lenovo\\{risk_col}_model.pkl'  # Absolute path for each model
        with open(model_path, 'rb') as file:
            models[risk_col] = pickle.load(file)
    return models

# Load the state-county mapping (cached)
state_county_map = load_state_county_map()

# --- Load the models (cached) ---
risk_columns = ['Risk_PN_ensemble', 'Risk_NP_ensemble', 'Risk_PF_ensemble', 'Risk_FP_ensemble', 'Risk_FN_ensemble', 'Risk_NF_ensemble']
models = load_models(risk_columns)

# --- Title ---
st.title("Risk Score Prediction for your Business")

# --- Sidebar Inputs ---
st.sidebar.header("Enter few details listed below:")

# Select State
state = st.sidebar.selectbox("Select State", list(state_county_map.keys()))

# Dynamically show counties based on state
county_options = state_county_map[state]
county = st.sidebar.selectbox("Select County", county_options)

# Other Inputs
hour = st.sidebar.slider("What's the timeframe you are looking at?", 0, 23)

business_category = st.sidebar.selectbox(
    "Business Category",
    ['Airports & Air Transport', 'Hospitals & Healthcare Facilities',
       'Power Plants (Electricity Generation & Distribution)',
       'Water Treatment & Utilities']  # You can populate this dynamically too if needed
)

incident_type = st.sidebar.selectbox(
    "Incident Type",
    ['Fire', 'Tornado', 'Severe Storm', 'Hurricane', 'Flood',
       'Severe Ice Storm', 'Snowstorm', 'Mud/Landslide', 'Earthquake',
       'Coastal Storm']  # Customize this list as needed
)

# Select Current State of Business
business_state = st.sidebar.selectbox(
    "What is the current state of your business?",
    ['Partial', 'Full Operational', 'Non Operational']
)

# Create DataFrame for model input
input_data = pd.DataFrame({
    'name': [county],  # Assuming 'name' = county
    'state': [state],
    'Hour': [hour],
    'Business_category': [business_category],
    'incidentType': [incident_type]
})

# --- Prediction ---
if st.sidebar.button("Predict Risk Scores"):
    st.subheader("Predicted Risk Scores")

    predictions = {}
    for risk_col in risk_columns:
        prediction = models[risk_col].predict(input_data)[0]
        predictions[risk_col] = prediction

    # Prepare risk scores based on business state
    if business_state == 'Partial':
        transitions = {
            'Partial to Non Operational': predictions['Risk_PN_ensemble'],
            'Partial to Full Operational': predictions['Risk_PF_ensemble']
        }
        colors = ['lightblue', 'deepskyblue']  # Lighter shades for better contrast
    elif business_state == 'Full Operational':
        transitions = {
            'Full to Non Operational': predictions['Risk_FN_ensemble'],
            'Full to Partial Operational': predictions['Risk_FP_ensemble']
        }
        colors = ['lightgreen', 'limegreen']  # Lighter shades for better contrast
    elif business_state == 'Non Operational':
        transitions = {
            'Non Operational to Full Operational': predictions['Risk_NF_ensemble'],
            'Non Operational to Partial': predictions['Risk_NP_ensemble']
        }
        colors = ['lightyellow', 'gold']  # Lighter shades for better contrast

    # Identify which transition has a higher value
    transition_labels = list(transitions.keys())
    transition_values = list(transitions.values())
    max_value = max(transition_values)
    max_index = transition_values.index(max_value)

    # Set the darker color for the riskier transition
    bar_colors = [colors[0] if i != max_index else colors[1] for i in range(len(transitions))]

    # ----------------- GAUGE PLOT ------------------------
    def create_gauge_with_needle(value, title):
        angle = 180 * (1 - value)
        radians = math.radians(angle)
        radius = 0.4
        x = 0.5 + radius * math.cos(radians)
        y = 0.5 + radius * math.sin(radians)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title},
            gauge={
                'axis': {'range': [0, 1]},
                'bar': {'color': "rgba(0,0,0,0)"},
                'steps': [
                    {'range': [0, 0.2], 'color': "lightgray"},
                    {'range': [0.2, 0.4], 'color': "lightyellow"},
                    {'range': [0.4, 0.6], 'color': "lightgreen"},
                    {'range': [0.6, 0.8], 'color': "lightblue"},
                    {'range': [0.8, 1], 'color': "lightcoral"}
                ]
            },
            domain={'x': [0, 1], 'y': [0, 1]}
        ))

        fig.add_shape(
            type="line",
            x0=0.5, y0=0.5,
            x1=x, y1=y,
            line=dict(color="red", width=4),
            xref="paper", yref="paper"
        )

        fig.add_shape(
            type="circle",
            xref="paper", yref="paper",
            x0=0.48, y0=0.48,
            x1=0.52, y1=0.52,
            fillcolor="red",
            line_color="red"
        )

        fig.update_layout(
            title_text=f"🕹️ Risk Gauge for {title}",
            height=400,
            margin={'t': 50, 'b': 0, 'l': 0, 'r': 0},
            font={'size': 18}
        )
        return fig

    # Show the gauge plot for the highest risk
    st.plotly_chart(create_gauge_with_needle(max_value, transition_labels[max_index]), use_container_width=True)

    # ----------------- DONUT CHART: TOP 15 COUNTIES ------------------------
    county_df = pd.read_csv("C:/Users/Lenovo/Downloads/mlds (1).csv")  # Replace with your dataset if needed
    county_df = county_df[county_df["State Name"] == state]
    county_df = county_df.groupby("County Name")[transition_labels[max_index]].mean().reset_index()
    county_df = county_df.sort_values(by=transition_labels[max_index], ascending=False)
    if len(county_df) > 15:
        county_df = county_df.head(15)

    fig_pie = go.Figure(data=[go.Pie(
        labels=county_df["County Name"],
        values=county_df[transition_labels[max_index]],
        hole=0.5,
        textinfo='label+percent',
        marker=dict(line=dict(color='#000000', width=1)),
        pull=[0.1] * len(county_df)
    )])

    fig_pie.update_layout(
        title=f"🍩 Top 15 Counties in {state} by Avg {transition_labels[max_index]}",
        showlegend=False,
        margin=dict(t=40, b=0, l=0, r=0),
    )

    st.plotly_chart(fig_pie, use_container_width=True)
