import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

# 側邊欄內容
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# 主頁標題
st.title("Interactive Map")

# 分欄
col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:
    # 底圖選項
    basemap = st.selectbox("Select a basemap:", options, index)

# 加載 GeoJSON 數據
TW_fishing = gpd.read_file('https://github.com/KaoYuan1205/homework1127/raw/refs/heads/main/f202311305757.geojson')

with col1:
    # 創建地圖
    m = leafmap.Map(
        center=[23.7652, 120.4980],
        zoom=8,
        locate_control=True,
        latlon_control=True,
        draw_export=True,
        minimap_control=True,
    )
    # 添加底圖
    m.add_basemap(basemap)

    # 添加 GeoJSON 點數據
    m.add_points_from_xy(
        TW_fishing,
        x='座標(WGS84)X',  # 替換為數據中 X 坐標欄位名
        y='座標(WGS84)Y',  # 替換為數據中 Y 坐標欄位名
        layer_name='全台開放釣點'
    )

    # 顯示地圖
    m.to_streamlit(height=700)

# 顯示數據表格
st.dataframe(TW_fishing)

# 顯示原始碼
with st.expander("See source code"):
    with st.echo():
        st.write("Your code is displayed here.")
