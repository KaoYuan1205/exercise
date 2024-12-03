import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:
    basemap = st.selectbox("Select a basemap:", options, index)

NORTHAED = gpd.read_file('https://github.com/KaoYuan1205/homework1127/raw/refs/heads/main/f202311305757.geojson')

with col1:
    m = leafmap.Map(
        center=[23.7652, 120.4980],
        zoom=8,
        locate_control=True,
        latlon_control=True,
        draw_export=True,
        minimap_control=True,
    )
    m.add_basemap(basemap)

    m.add_points_from_xy(
        TW_fishing,
        x='座標(WGS84)X',
        y='座標(WGS84)Y', 
        layer_name='北部海巡署AED點位'
    )

    # 顯示地圖
    m.to_streamlit(height=700)

# 顯示數據表格
st.dataframe(NORTHAED)

# 顯示原始碼
with st.expander("See source code"):
    with st.echo():
        st.write("Your code is displayed here.")
