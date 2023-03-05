import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from iconloader import load_icon, load_placeholder, load_icon
from dataloader import create_csv

st.set_page_config(layout='wide')
st.title('genshin character visualizer')
datapath = 'characters.csv'

# given a file path to a csv containing character data, return csv data as pandas dataframe
def load_csv():
    """
    param
    """
    return pd.read_csv(datapath)


# given csv data, return a pandas pivot table as pandas dataframe
def generate_pd_table(data):
    fields = data.columns.delete([0, 1])

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
def html_display(table, icon_dict, fields):
    placeholder = load_placeholder()

    _row, _column = fields

    html_table = "<table><tr><th></th>\n"
    for col in table.columns:
        column_icon = load_icon(_column, col)
        html_table += f"<th> <img src='data:image/png;base64,{column_icon}' style='width:70px;height:70px' /> </th>"
    html_table += "</tr>\n"
    for row in table.index:
        # html_table += f"<tr><th>{row}</th>\n"
        row_icon = load_icon(_row, row)
        html_table += f"<th> <img src='data:image/png;base64,{row_icon}' style='width:70px;height:70px' /> </th>"
        for col in table.columns:
            char_name = table.loc[row, col]
            names = char_name.split(', ')
            for name in names:
                try: 
                    char_icon = icon_dict[name]
                    # char_icon = base64.b64encode(char_icon.tobytes()).decode('utf-8')
                    html_table += f"<td><img src='data:image/png;base64,{char_icon}' style='width:50px;height:50px' /></td>\n"
                    print('flag icon succeed', name)
                except:
                    html_table += f"<td><img src='data:image/png;base64,{placeholder}' style='width:50px;height:50px' /></td>"
                    FileNotFoundError('object name is none')
        html_table += "</tr>\n"
    html_table += "</table>\n"

    components.html(html_table, width=2000, height=2000, scrolling=True)


def run_streamlit():
    create_csv()
    data = load_csv()
    table, fields = generate_pd_table(data)
    print('field', fields)
    print(type(fields))
    st.table(table)
    icon_dict = load_icon(data)
    html_display(table, icon_dict, fields)