import streamlit as st

st.title("🎈 Welcome to Streamlit")
st.write(
    "Streamlit allows you to build interactive Apps using Python. :snake:"
)

with st.expander("Interative Tabular Data"):
    import streamlit as st
    import pandas as pd
    import numpy as np
    
    df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

    st.dataframe(df.style.highlight_max(axis=0))

with st.expander("Visualizations"):
    import streamlit as st
    import pandas as pd
    import numpy as np

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

    st.line_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
    )
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(df)
    
with st.expander("More Visualization"):
    import streamlit as st
    import numpy as np
    import plotly.figure_factory as ff

# Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

# Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
    st.plotly_chart(fig, use_container_width=True)
