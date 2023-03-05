import base64

charicon_path = 'icons/characters/'
elementicon_path = 'icons/elements/'
weaponicon_path = 'icons/weapons/'
regionicon_path = 'icons/regions/'

# given csv dataframe, return a dictionary of char icons 
def load_icon(data):
    icon_dict = {}
    for char_name in data['name']:
        try:
            icon_path = f'{charicon_path}{char_name}.png'
            icon_dict[char_name] = image_to_base64(icon_path)
        except:
            FileNotFoundError('char png not found')
    return icon_dict

def load_placeholder():
    icon_path = f'{charicon_path}cholder.png'
    return image_to_base64(icon_path) 

def load_icon(_field, entity_name):
    if _field == 'element':
        _path = elementicon_path
    elif _field == 'weapon':
        _path = weaponicon_path
    elif _field == 'region':
        _path = regionicon_path
    return image_to_base64(f'{_path}{entity_name}.png')

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string