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
