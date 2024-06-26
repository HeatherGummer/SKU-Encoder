import streamlit as st
import create_dict 
import os
import requests as rq
import shutil

# == Generate Dictionaries == #

# read the dict from the text file via the module
dicts = create_dict.main()

# generate the encoding and decoding dicts
dict_base = dicts[0]
dict_decode = dicts[1]


def addToClipBoard(text): # copy the output to your clipboard
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def barcode(var, prod_name): # generate and export the response
    url = f'https://barcodeapi.org/api/dm/{var}?dpi=300'

    response = rq.get(url, stream=True)

    with open(f'DM-{prod_name}-{var}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    
    del response

def decode(string): # Provide the decoding as a list rather than 
    # as a dict
    dict_keys = dict_decode.keys()
    iter_counter = 0
    decoded = ''

    for key in dict_keys:
        string_2 = string[iter_counter]
        try:
            val = str(dict_decode[key][string_2.upper()]).title()
            decoded += val + ' '
        except:
            continue
        iter_counter += 1

    return decoded

def main():
    # create a list of the labels used in the main dict
    labels = list(dict_base.keys())

    # initialize the output variable
    output = ''

    # initiate the iterator variable
    l_iter = 0

# == Start Streamlit App Coding == #
    
    st.header('Erin\'s SKU Generator')
    st.write(f'This is based on the options I require on the back end.' 
             f' I\'m using a text file to generate the options list.')
    st.write('Labels of the selection boxes below are determined by the colum'
             ' title in the column in the tab delimited text file I\'m using'
             ' to generate the dictionary containing the options.')
    
    st.write('')
    
    tab_1, tab_2 = st.tabs(['Generator', 'Decoder'])

    with tab_1:
    
        col_1, col_2 = st.columns(2) # create two columns

        with col_1:            
            cat_name = st.selectbox(
                # create a slection box
                label=labels[l_iter].title().replace('_', ' ')
                # pull the options from the dictionary
                , options=dict_base[labels[l_iter]]
                , index=None
                , key=labels[l_iter]
                , placeholder='Choose from the below...'
            )

            if cat_name: # if there is a category name
                output += str(dict_base[labels[l_iter]][cat_name])
            else:
                output += 'A'

            l_iter += 1

            att_1 = st.selectbox(
                label=labels[l_iter].title().replace('_', ' ')
                , options=dict_base[labels[l_iter]]
                , index=None
                , key=labels[l_iter]
                , placeholder='Choose from the below...'
            )

            if cat_name and att_1:
                output += str(dict_base[labels[l_iter]][att_1])
            else:
                output += 'A'

            l_iter += 1

            att_2 = st.selectbox(
                label=labels[l_iter].title().replace('_', ' ')
                , options=dict_base[labels[l_iter]]
                , index=None
                , key=labels[l_iter]
                , placeholder='Choose from the below...'
            )

            if cat_name and att_2:
                output += str(dict_base[labels[l_iter]][att_2])
            else:
                output += 'A'

            l_iter += 1

            att_3 = st.selectbox(
                label=labels[l_iter].title().replace('_', ' ')
                , options=dict_base[labels[l_iter]]
                , index=None
                , key=labels[l_iter]
                , placeholder='Choose from the below...'
            )

            if cat_name and att_3:
                output += str(dict_base[labels[l_iter]][att_3])
            else:
                output += 'A'

            l_iter += 1

            att_4 = st.selectbox(
                label=labels[l_iter].title().replace('_', ' ')
                , options=dict_base[labels[l_iter]]
                , index=None
                , key=labels[l_iter]
                , placeholder='Choose from the below...'
            )

            if cat_name and att_4:
                output += str(dict_base[labels[l_iter]][att_4])
            else:
                output += 'A'

            l_iter += 1

            att_5 = st.selectbox(
                label=labels[l_iter].title().replace('_', ' ')
                , options=dict_base[labels[l_iter]]
                , index=None
                , key=labels[l_iter]
                , placeholder='Choose from the below...'
            )

            if cat_name and att_5:
                output += str(dict_base[labels[l_iter]][att_5])
            else:
                output += 'A'

            l_iter += 1

            theme_name = st.selectbox(
                label=labels[l_iter].title().replace('_', ' ')
                , options=dict_base[labels[l_iter]]
                , index=None
                , key=labels[l_iter]
                , placeholder='Choose from the below...'
            )

            if cat_name and theme_name:
                output += str(dict_base[labels[l_iter]][theme_name])
            else:
                output += 'A'

        with col_2:

            if cat_name:
                st.write(output)
                seq = st.text_input(
                    label='Sequence',
                    max_chars=3,
                    placeholder='Enter a 3-digit numeric sequence'
                )

                prod_name = st.text_input(
                    label='Name',
                    key='prod_name',
                    placeholder='Enter a name here...',
                    label_visibility='hidden'
                )       

                if st.button(label='generate') and prod_name:
                    stuff = output + seq
                    barcode(stuff, prod_name)

                if st.button(label='Press to Copy'):
                    stuff = output + seq
                    addToClipBoard(stuff)

            else:
                st.write('Choose a main category!')

    with tab_2:
        st.header('SKU Decoder')
        st.divider()

        string = st.text_input(
            label='decode',
            key='decode',
            placeholder='Enter the SKU to decode...',
            label_visibility='hidden'
        ) 

        if string:
            iter_counter = 0
            output_string = []
            for key in dict_decode.keys():
                try:
                    string_2 = string[iter_counter]
                    output_string.append(f'{key} : {dict_decode[key][string_2.upper()]}')
                except:
                    output_string.append(f'{key} : --KEY UNKNOWN--')
                iter_counter += 1

            output_string

if __name__ == '__main__':
    main()