import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from iconloader import load_profile, load_icon
from dataloader import create_csv

st.set_page_config(
    page_title='genshin character visualizer',
    page_icon='🤗',
    layout='wide', 
    initial_sidebar_state="auto",
    menu_items={
        'About': "I've had this idea for a while.", 
        'Report a bug': "https://github.com/harryzhu626?tab=repositories"
    }
)
datapath = 'characters.csv'

# given a file path to a csv containing character data, return csv data as pandas dataframe
def load_csv():
    """
    param
    """
    return pd.read_csv(datapath)


# given csv data, return a pandas pivot table as pandas dataframe
def generate_pd_table(data):
    fields = data.columns.delete([0, 1, -1])

    col1, col2, buffer = st.columns([1, 1, 2])

    row = col1.selectbox('select row', fields)
    column = col2.selectbox('select column', fields.drop(row))

    table = pd.pivot_table(
        data,
        index=row,
        columns=column,
        values='name',
        fill_value = '',
        aggfunc=lambda x: ', '.join(str(v) for v in x))
    return table, (row, column)
    

# given dataframe table, create a html markup
def create_html(table, icon_dict, fields):
    _row, _column = fields

    html_table = "<table style='background-color: #3bb6ef;'><tr><th></th>\n"
    for col in table.columns: 
        column_icon = load_icon(_column, col)
        #html_table += f"<th> {col} </th>"
        html_table += f"<th> <img src='data:image/png;base64,{column_icon}' style='width:70px;height:70px' /> </th>"
    html_table += "</tr>\n"
    for row in table.index:
        row_icon = load_icon(_row, row)
        #html_table += f"<tr> <th>{row}</th>"
        html_table += f"<tr> <th> <img src='data:image/png;base64,{row_icon}' style='width:70px;height:70px' /> </th>\n"
        for col in table.columns:
            char_name = table.loc[row, col]
            names = char_name.split(', ')
            html_table += "<td>"
            char_icon_html = "<div class='image-container'>"
            for name in names:
                try: 
                    char_icon = icon_dict[name]
                    char_icon_html += f"<img src='data:image/png;base64,{char_icon}'> \n"
                except:
                    FileNotFoundError('character image is not found')
            html_table += char_icon_html + "</div>\n </td>"
        html_table += "</tr>\n"
    html_table += "</table>\n"
    
    html_markup = stylize_html(html_table)
    components.html(html_markup, width=2000, height=2000, scrolling=True)


def stylize_html(html):
    container_style = '  .image-container {clear: both;overflow: hidden; width: 110px; \
                box-sizing: border-box;}\
                  .image-container img {width: 50px; height: 50px;float: left;\
                box-sizing: border-box; margin: 0 5px 5px 0;}\
                  .image-container img:nth-child(2n) {margin-right: 0;}'
    table_style = 'table {border-collapse: collapse; border: 2px solid white;} \
        th, td {border: 1px solid white;padding: 8px;text-align: left;}'
    header = f'<style> {table_style} {container_style}</style>'
    return header + html

def download_option(image_file):
    print('flag download')
    st.download_button(
    label="Download table as png",
    data=image_file,
    file_name='genshin_chart.png',
    mime='image/png',
)

def run_streamlit():
    st.title('genshin character visualizer')

    create_csv()
    data = load_csv()

    table, fields = generate_pd_table(data)
    # st.table(table)
    icon_dict = load_profile(data)
    create_html(table, icon_dict, fields)