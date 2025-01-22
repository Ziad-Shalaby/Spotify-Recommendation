import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Music Data Dashboard", layout="wide")
st.title("Music Data Dashboard")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("./Music Info.csv") 
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()

df = load_data()

# Replace null values with the most frequent value in each column
for column in df.columns:
    if df[column].isnull().any():
        most_frequent = df[column].mode()[0]
        df[column].fillna(most_frequent, inplace=True)

if df.empty:
    st.stop()

st.sidebar.header("Filter Data:")
# Adding 'All' option to the year filter
year_options = ["All"] + sorted(df['year'].dropna().unique())
year_filter = st.sidebar.multiselect(
    "Select Release Year", 
    options=year_options, 
    default="All"
)

# Adding 'All' option to the genre filter
genre_options = ["All"] + sorted(df['genre'].dropna().unique())
genre_filter = st.sidebar.multiselect(
    "Select Genre", 
    options=genre_options, 
    default="All"
)

# Filtering the dataframe based on selections
df_filtered = df.copy()
if "All" not in year_filter:
    df_filtered = df_filtered[df_filtered['year'].isin(year_filter)]
if "All" not in genre_filter:
    df_filtered = df_filtered[df_filtered['genre'].isin(genre_filter)]

# Display insights
total_tracks = df_filtered.shape[0]
avg_duration = df_filtered['duration_ms'].mean() / 1000 if total_tracks > 0 else 0
st.markdown(f"### Total Tracks: {total_tracks}")
st.markdown(f"### Average Track Duration: {avg_duration:.2f} seconds")

# Layout for visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Genre Distribution")
    if not df_filtered.empty:
        fig = px.pie(df_filtered, names='genre', title="Genre Distribution", color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig)

with col2:
    st.subheader("Top Artists by Track Count")
    if not df_filtered.empty:
        artist_counts = df_filtered['artist'].value_counts().head(10).reset_index()
        artist_counts.columns = ['Artist', 'Track Count']
        fig = px.bar(artist_counts, x='Track Count', y='Artist', orientation='h', title="Top Artists", color='Artist', color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig)

st.markdown("## Tracks by Release Year")
if not df_filtered.empty:
    year_counts = df_filtered['year'].value_counts().reset_index()
    year_counts.columns = ['Year', 'Track Count']
    fig = px.line(year_counts.sort_values(by='Year'), x='Year', y='Track Count', title="Tracks by Release Year", markers=True, color_discrete_sequence=['blue'])
    st.plotly_chart(fig)

st.markdown("## Additional Insights")
if not df_filtered.empty:
    fig = px.histogram(df_filtered, x='danceability', nbins=20, title="Danceability Distribution", color_discrete_sequence=['purple'])
    st.plotly_chart(fig)

    fig = px.scatter(df_filtered, x='energy', y='valence', title="Energy vs Valence", color='genre', hover_data=['name', 'artist'], color_discrete_sequence=px.colors.qualitative.Dark24)
    st.plotly_chart(fig)

    fig = px.histogram(df_filtered, x='tempo', nbins=20, title="Tempo Distribution", color_discrete_sequence=['green'])
    st.plotly_chart(fig)