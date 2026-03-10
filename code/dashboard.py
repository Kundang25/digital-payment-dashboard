# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # title
# st.title("Digital Payment Adoption Analysis")

# # load dataset
# data = pd.read_csv("../dataset/digital_payment_dataset.csv")

# st.subheader("Dataset Preview")
# st.dataframe(data)

# # sidebar filters
# st.sidebar.header("Filters")

# location_filter = st.sidebar.multiselect(
#     "Select Location",
#     options=data["Location"].unique(),
#     default=data["Location"].unique()
# )

# filtered_data = data[data["Location"].isin(location_filter)]

# # charts
# st.subheader("Digital Payment Distribution")

# fig1 = px.pie(filtered_data,names="Digital_Payment",title="Payment Adoption")
# st.plotly_chart(fig1)

# st.subheader("Urban vs Rural Adoption")

# fig2 = px.histogram(
#     filtered_data,
#     x="Location",
#     color="Digital_Payment",
#     barmode="group"
# )

# st.plotly_chart(fig2)

# st.subheader("Income vs Expenditure")

# fig3 = px.scatter(
#     filtered_data,
#     x="Income",
#     y="Monthly_Expenditure",
#     color="Digital_Payment"
# )

# st.plotly_chart(fig3)

# st.subheader("Discretionary Spending")

# fig4 = px.box(
#     filtered_data,
#     x="Digital_Payment",
#     y="Discretionary_Spending"
# )

# st.plotly_chart(fig4)

# # statistics
# st.subheader("Summary Statistics")

# st.write(filtered_data.describe())














# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split

# st.set_page_config(page_title="Digital Payment Dashboard", layout="wide")

# st.title("💳 Digital Payment Adoption Dashboard")

# # load dataset
# data = pd.read_csv("../dataset/digital_payment_dataset.csv")

# page = st.sidebar.radio(
#     "Navigation",
#     ["Overview","Spending Analysis","Advanced Analytics","Prediction"]
# )

# # ---------------- KPI METRICS ----------------

# total = len(data)
# adopters = len(data[data["Digital_Payment"]=="Yes"])
# rate = adopters/total*100

# col1,col2,col3,col4 = st.columns(4)

# col1.metric("Total Households", total)
# col2.metric("Adoption Rate", f"{rate:.2f}%")
# col3.metric("Average Income", int(data["Income"].mean()))
# col4.metric("Avg Expenditure", int(data["Monthly_Expenditure"].mean()))

# st.divider()

# # ---------------- SIDEBAR FILTERS ----------------

# st.sidebar.header("Filters")

# location_filter = st.sidebar.multiselect(
#     "Location",
#     options=data["Location"].unique(),
#     default=data["Location"].unique()
# )

# income_range = st.sidebar.slider(
#     "Income Range",
#     int(data["Income"].min()),
#     int(data["Income"].max()),
#     (int(data["Income"].min()), int(data["Income"].max()))
# )

# filtered_data = data[
#     (data["Location"].isin(location_filter)) &
#     (data["Income"]>=income_range[0]) &
#     (data["Income"]<=income_range[1])
# ]

# # ---------------- DATASET PREVIEW ----------------

# st.subheader("Dataset Preview")
# st.dataframe(filtered_data,use_container_width=True)

# st.divider()

# # ---------------- ADOPTION DISTRIBUTION ----------------

# col1,col2 = st.columns(2)

# with col1:
#     st.subheader("Adoption Distribution")

#     fig1 = px.pie(
#         filtered_data,
#         names="Digital_Payment",
#         title="Digital Payment Usage"
#     )

#     st.plotly_chart(fig1,use_container_width=True)

# with col2:
#     st.subheader("Urban vs Rural Adoption")

#     fig2 = px.histogram(
#         filtered_data,
#         x="Location",
#         color="Digital_Payment",
#         barmode="group"
#     )

#     st.plotly_chart(fig2,use_container_width=True)

# st.divider()

# # ---------------- SPENDING ANALYSIS ----------------

# col1,col2 = st.columns(2)

# with col1:
#     st.subheader("Income vs Expenditure")

#     fig3 = px.scatter(
#         filtered_data,
#         x="Income",
#         y="Monthly_Expenditure",
#         color="Digital_Payment"
#     )

#     st.plotly_chart(fig3,use_container_width=True)

# with col2:
#     st.subheader("Discretionary Spending")

#     fig4 = px.box(
#         filtered_data,
#         x="Digital_Payment",
#         y="Discretionary_Spending"
#     )

#     st.plotly_chart(fig4,use_container_width=True)

# st.divider()

# # ---------------- SPENDING SEGMENTATION ----------------

# st.subheader("Spending Segmentation")

# filtered_data["Spending_Level"] = pd.qcut(
#     filtered_data["Monthly_Expenditure"],
#     3,
#     labels=["Low","Medium","High"]
# )

# fig5 = px.histogram(
#     filtered_data,
#     x="Spending_Level",
#     color="Digital_Payment"
# )

# st.plotly_chart(fig5,use_container_width=True)

# st.divider()

# # ---------------- CORRELATION HEATMAP ----------------

# st.subheader("Correlation Heatmap")

# corr = filtered_data[["Income","Monthly_Expenditure","Discretionary_Spending"]].corr()

# fig,ax = plt.subplots()

# sns.heatmap(corr,annot=True,cmap="coolwarm",ax=ax)

# st.pyplot(fig)

# st.divider()

# # ---------------- ML PREDICTION TOOL ----------------

# st.subheader("ML Prediction Tool")

# model_data = data.copy()

# model_data["Location"] = model_data["Location"].map({"Urban":1,"Rural":0})
# model_data["Digital_Payment"] = model_data["Digital_Payment"].map({"Yes":1,"No":0})

# X = model_data[["Location","Income","Monthly_Expenditure","Discretionary_Spending"]]
# y = model_data["Digital_Payment"]

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# model = RandomForestClassifier()
# model.fit(X_train,y_train)

# location = st.selectbox("Location",["Urban","Rural"])
# income = st.number_input("Income",10000,100000)
# expenditure = st.number_input("Monthly Expenditure",5000,90000)
# discretionary = st.number_input("Discretionary Spending",1000,30000)

# loc = 1 if location=="Urban" else 0

# if st.button("Predict Adoption"):

#     pred = model.predict([[loc,income,expenditure,discretionary]])

#     if pred[0]==1:
#         st.success("Likely to adopt digital payments")
#     else:
#         st.error("Unlikely to adopt digital payments")

# st.divider()

# # ---------------- KEY INSIGHTS ----------------

# st.subheader("Key Insights")

# st.write("• Urban households tend to adopt digital payments more frequently.")
# st.write("• Higher income households show higher adoption rates.")
# st.write("• Digital payment users have higher discretionary spending.")
# st.write("• Income and expenditure show strong correlation.")








# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split

# st.set_page_config(page_title="Digital Payment Dashboard", layout="wide")

# st.title("💳 Digital Payment Analytics Dashboard")

# # load data
# data = pd.read_csv("../dataset/digital_payment_dataset.csv")

# # ---------------- SIDEBAR ----------------

# st.sidebar.title("Dashboard Menu")

# page = st.sidebar.radio(
#     "Navigation",
#     ["Overview","Spending Analysis","Advanced Analytics","Prediction"]
# )

# # filters
# st.sidebar.subheader("Filters")

# location_filter = st.sidebar.multiselect(
#     "Location",
#     options=data["Location"].unique(),
#     default=data["Location"].unique()
# )

# income_range = st.sidebar.slider(
#     "Income Range",
#     int(data["Income"].min()),
#     int(data["Income"].max()),
#     (int(data["Income"].min()), int(data["Income"].max()))
# )

# filtered = data[
#     (data["Location"].isin(location_filter)) &
#     (data["Income"]>=income_range[0]) &
#     (data["Income"]<=income_range[1])
# ]

# # ---------------- OVERVIEW ----------------

# if page == "Overview":

#     st.header("Overview")

#     total = len(filtered)
#     adopters = len(filtered[filtered["Digital_Payment"]=="Yes"])
#     rate = adopters/total*100

#     col1,col2,col3,col4 = st.columns(4)

#     col1.metric("Total Households", total)
#     col2.metric("Adoption Rate", f"{rate:.2f}%")
#     col3.metric("Avg Income", int(filtered["Income"].mean()))
#     col4.metric("Avg Expenditure", int(filtered["Monthly_Expenditure"].mean()))

#     st.divider()

#     col1,col2 = st.columns(2)

#     with col1:

#         fig = px.pie(
#             filtered,
#             names="Digital_Payment",
#             title="Digital Payment Adoption"
#         )

#         st.plotly_chart(fig,use_container_width=True)

#     with col2:

#         fig = px.histogram(
#             filtered,
#             x="Location",
#             color="Digital_Payment",
#             barmode="group",
#             title="Urban vs Rural Adoption"
#         )

#         st.plotly_chart(fig,use_container_width=True)

#     st.subheader("Dataset Preview")

#     st.dataframe(filtered,use_container_width=True)

#     st.download_button(
#         "Download Dataset",
#         filtered.to_csv(index=False),
#         file_name="digital_payment_data.csv"
#     )

# # ---------------- SPENDING ANALYSIS ----------------

# if page == "Spending Analysis":

#     st.header("Spending Behaviour")

#     tab1,tab2,tab3 = st.tabs(["Income vs Expenditure","Discretionary Spending","Segmentation"])

#     with tab1:

#         fig = px.scatter(
#             filtered,
#             x="Income",
#             y="Monthly_Expenditure",
#             color="Digital_Payment"
#         )

#         st.plotly_chart(fig,use_container_width=True)

#     with tab2:

#         fig = px.box(
#             filtered,
#             x="Digital_Payment",
#             y="Discretionary_Spending"
#         )

#         st.plotly_chart(fig,use_container_width=True)

#     with tab3:

#         filtered["Spending_Level"] = pd.qcut(
#             filtered["Monthly_Expenditure"],
#             3,
#             labels=["Low","Medium","High"]
#         )

#         fig = px.histogram(
#             filtered,
#             x="Spending_Level",
#             color="Digital_Payment"
#         )

#         st.plotly_chart(fig,use_container_width=True)

# # ---------------- ADVANCED ANALYTICS ----------------

# if page == "Advanced Analytics":

#     st.header("Advanced Analytics")

#     with st.expander("Correlation Heatmap"):

#         corr = filtered[
#             ["Income","Monthly_Expenditure","Discretionary_Spending"]
#         ].corr()

#         fig,ax = plt.subplots()

#         sns.heatmap(corr,annot=True,cmap="coolwarm",ax=ax)

#         st.pyplot(fig)

#     with st.expander("Summary Statistics"):

#         st.write(filtered.describe())

#     with st.expander("Auto Insights"):

#         st.write("• Urban households show higher digital payment adoption.")

#         st.write("• Higher income households are more likely to adopt digital payments.")

#         st.write("• Digital payment users spend more on discretionary items.")

# # ---------------- ML PREDICTION ----------------

# if page == "Prediction":

#     st.header("Digital Payment Adoption Predictor")

#     model_data = data.copy()

#     model_data["Location"] = model_data["Location"].map({"Urban":1,"Rural":0})
#     model_data["Digital_Payment"] = model_data["Digital_Payment"].map({"Yes":1,"No":0})

#     X = model_data[["Location","Income","Monthly_Expenditure","Discretionary_Spending"]]
#     y = model_data["Digital_Payment"]

#     X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#     model = RandomForestClassifier()

#     model.fit(X_train,y_train)

#     location = st.selectbox("Location",["Urban","Rural"])
#     income = st.number_input("Income",10000,100000)
#     expenditure = st.number_input("Monthly Expenditure",5000,90000)
#     discretionary = st.number_input("Discretionary Spending",1000,30000)

#     loc = 1 if location=="Urban" else 0

#     if st.button("Predict Adoption"):

#         pred = model.predict([[loc,income,expenditure,discretionary]])

#         if pred[0]==1:

#             st.success("Likely to adopt digital payments")

#         else:

#             st.error("Unlikely to adopt digital payments")




import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Digital Payment AI Dashboard", layout="wide")

st.title("💳 Digital Payment AI Analytics Dashboard")

# load data
data = pd.read_csv("../dataset/digital_payment_dataset.csv")

# ---------------- SIDEBAR ----------------

st.sidebar.title("Dashboard Control")

page = st.sidebar.radio(
    "Navigation",
    ["Overview","Spending Analysis","Advanced Analytics","AI Insights","Prediction"]
)

# theme toggle
theme = st.sidebar.toggle("Dark Mode")

if theme:
    st.markdown(
        """
        <style>
        body {background-color:#0E1117;color:white;}
        </style>
        """,
        unsafe_allow_html=True
    )

# filters
st.sidebar.subheader("Filters")

location_filter = st.sidebar.multiselect(
    "Location",
    options=data["Location"].unique(),
    default=data["Location"].unique()
)

income_range = st.sidebar.slider(
    "Income Range",
    int(data["Income"].min()),
    int(data["Income"].max()),
    (int(data["Income"].min()), int(data["Income"].max()))
)

filtered = data[
    (data["Location"].isin(location_filter)) &
    (data["Income"]>=income_range[0]) &
    (data["Income"]<=income_range[1])
]

# ---------------- OVERVIEW ----------------

if page == "Overview":

    st.header("Overview Dashboard")

    total = len(filtered)
    adopters = len(filtered[filtered["Digital_Payment"]=="Yes"])
    rate = adopters/total*100

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Total Households", total)
    col2.metric("Adoption Rate", f"{rate:.2f}%")
    col3.metric("Average Income", int(filtered["Income"].mean()))
    col4.metric("Average Spending", int(filtered["Monthly_Expenditure"].mean()))

    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        fig = px.pie(
            filtered,
            names="Digital_Payment",
            title="Digital Payment Adoption",
            hole=0.4
        )

        fig.update_layout(transition_duration=800)

        st.plotly_chart(fig,use_container_width=True)

    with col2:

        fig = px.histogram(
            filtered,
            x="Location",
            color="Digital_Payment",
            barmode="group",
            title="Urban vs Rural Adoption"
        )

        fig.update_layout(transition_duration=800)

        st.plotly_chart(fig,use_container_width=True)

    st.subheader("Dataset Preview")

    st.dataframe(filtered,use_container_width=True)

# ---------------- SPENDING ANALYSIS ----------------

if page == "Spending Analysis":

    st.header("Consumer Spending Behaviour")

    tab1,tab2 = st.tabs(["Income vs Expenditure","Discretionary Spending"])

    with tab1:

        fig = px.scatter(
            filtered,
            x="Income",
            y="Monthly_Expenditure",
            color="Digital_Payment",
            size="Discretionary_Spending"
        )

        fig.update_layout(transition_duration=800)

        st.plotly_chart(fig,use_container_width=True)

    with tab2:

        fig = px.box(
            filtered,
            x="Digital_Payment",
            y="Discretionary_Spending"
        )

        st.plotly_chart(fig,use_container_width=True)

# ---------------- ADVANCED ANALYTICS ----------------

if page == "Advanced Analytics":

    st.header("Advanced Data Analysis")

    with st.expander("Correlation Heatmap"):

        corr = filtered[
            ["Income","Monthly_Expenditure","Discretionary_Spending"]
        ].corr()

        fig,ax = plt.subplots()

        sns.heatmap(corr,annot=True,cmap="coolwarm",ax=ax)

        st.pyplot(fig)

    with st.expander("Spending Segmentation"):

        filtered["Spending_Level"] = pd.qcut(
            filtered["Monthly_Expenditure"],
            3,
            labels=["Low","Medium","High"]
        )

        fig = px.histogram(
            filtered,
            x="Spending_Level",
            color="Digital_Payment"
        )

        st.plotly_chart(fig,use_container_width=True)

# ---------------- AI INSIGHTS ----------------

if page == "AI Insights":

    st.header("AI Generated Insights")

    adoption_rate = len(data[data["Digital_Payment"]=="Yes"]) / len(data)

    if adoption_rate > 0.5:
        st.success("Digital payments adoption is dominant among households.")
    else:
        st.warning("Digital payments adoption is still developing.")

    if data["Income"].corr(data["Monthly_Expenditure"]) > 0.5:
        st.info("Income strongly influences household spending behaviour.")

    st.subheader("India Digital Payment Growth Simulation")

    years = np.arange(2016,2025)

    growth = np.cumsum(np.random.randint(10,40,len(years)))

    df = pd.DataFrame({
        "Year":years,
        "UPI Transactions (billions)":growth
    })

    fig = px.line(df,x="Year",y="UPI Transactions (billions)",markers=True)

    st.plotly_chart(fig,use_container_width=True)






#State Selector Add karo

st.subheader("India Digital Payment Adoption Map")

state_selected = st.selectbox(
    "Select State",
    [
        "Maharashtra","Delhi","Karnataka","Tamil Nadu",
        "Uttar Pradesh","Gujarat","West Bengal",
        "Rajasthan","Punjab","Haryana"
    ]
)
# import json

# st.subheader("India Digital Payment Adoption Map")

# with open("../india_states.geojson") as f:
#     india_geo = json.load(f)

# state_data = pd.DataFrame({
#     "state": [
#         "Maharashtra","Delhi","Karnataka","Tamil Nadu",
#         "Uttar Pradesh","Gujarat","West Bengal",
#         "Rajasthan","Punjab","Haryana"
#     ],
#     "adoption":[72,85,78,74,60,70,65,58,66,68]
# })

# fig = px.choropleth(
#     state_data,
#     geojson=india_geo,
#     locations="state",
#     featureidkey="properties.NAME_1",
#     color="adoption",
#     color_continuous_scale="Blues"
# )

# fig.update_geos(
#     fitbounds="locations",
#     visible=False
# )

# st.plotly_chart(fig,use_container_width=True)

#Map Code
import json

with open("../india_states.geojson") as f:
    india_geo = json.load(f)

state_data = pd.DataFrame({
    "state":[
        "Maharashtra","Delhi","Karnataka","Tamil Nadu",
        "Uttar Pradesh","Gujarat","West Bengal",
        "Rajasthan","Punjab","Haryana"
    ],
    "adoption":[72,85,78,74,60,70,65,58,66,68]
})

fig = px.choropleth(
    state_data,
    geojson=india_geo,
    locations="state",
    featureidkey="properties.NAME_1",
    color="adoption",
    color_continuous_scale="Blues"
)

fig.update_geos(
    fitbounds="locations",
    visible=False
)

st.plotly_chart(fig,use_container_width=True)


#Dynamic Charts
st.subheader(f"State Analysis: {state_selected}")

state_filtered = filtered.copy()

fig1 = px.histogram(
    state_filtered,
    x="Digital_Payment",
    color="Location",
    title="Digital Payment Distribution"
)

st.plotly_chart(fig1,use_container_width=True)


fig2 = px.scatter(
    state_filtered,
    x="Income",
    y="Monthly_Expenditure",
    color="Digital_Payment",
    title="Income vs Spending"
)

st.plotly_chart(fig2,use_container_width=True)



# ---------------- ML PREDICTION ----------------

if page == "Prediction":

    st.header("AI Prediction Tool")

    model_data = data.copy()

    model_data["Location"] = model_data["Location"].map({"Urban":1,"Rural":0})
    model_data["Digital_Payment"] = model_data["Digital_Payment"].map({"Yes":1,"No":0})

    X = model_data[["Location","Income","Monthly_Expenditure","Discretionary_Spending"]]
    y = model_data["Digital_Payment"]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

    model = RandomForestClassifier()

    model.fit(X_train,y_train)

    location = st.selectbox("Location",["Urban","Rural"])
    income = st.number_input("Income",10000,100000)
    expenditure = st.number_input("Monthly Expenditure",5000,90000)
    discretionary = st.number_input("Discretionary Spending",1000,30000)

    loc = 1 if location=="Urban" else 0

    if st.button("Predict Digital Adoption"):

        pred = model.predict([[loc,income,expenditure,discretionary]])

        if pred[0]==1:

            st.success("Likely to adopt digital payments")

        else:

            st.error("Unlikely to adopt digital payments")