import plotly.express as px
import plotly.data as pldata

# Task 3: Interactive Visualizations with Plotly
df = pldata.wind(return_type='pandas')
# print(df.head(10))
# print(df.tail(10))

# 3.2: Clean the data: convert the 'strength' column to a float using str.replace() with regex, followed by type conversion.
df['strength'] = df['strength'].str.replace(r'\D+', '', regex=True).astype(float)
# print(df.head(10))
# print(df.tail(10))

# df.info()

# 3.3: Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
fig = px.scatter(df, x="frequency", y="strength", 
                 color="direction", 
                 size="strength", 
                 opacity=0.75, 
                 hover_data=["direction"], 
                 title="Wind Data, Strength vs. Frequency",
                 labels={
                     "frequency": "Frequency",
                     "strength": "Strength",
                     "direction": "Direction"
                 }
                 )

# 3.4: Save and load the HTML file, as wind.html. Verify that the plot works correctly.
fig.write_html("wind.html", auto_open=True)