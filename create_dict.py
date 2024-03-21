import pandas as pd

options = ('A','C','E','F','G','H','I','J','K','L','M','N','P','R','T','U','W','X','Y','0','1','2','3','4','5','6','7','8','9')

dataset = pd.read_csv('Book1.txt',delimiter="\t",na_filter=False)

cols = dataset.keys()

new_dict = {}

def main():
    for col in cols:
        new_dict[col] = []
        for val in dataset[col]:
            if val != '':
                new_dict[col].append(val)
                #print(new_dict)
    encode_dict = {}
    decode_dict = {}
    
    opts_iterator = 0

    for col in cols:
        encode_dict[col] = {}
        decode_dict[col] = {}
        for val in dataset[col]:
            try:
                new_key = options[opts_iterator]
                encode_dict[col][new_key] = val
                decode_dict[col][new_key] = val
                opts_iterator += 1
            except:
                continue
        encode_dict[col] = {v:k for k, v in encode_dict[col].items() if v != ''}
        decode_dict[col] = {k:v for k, v in decode_dict[col].items() if v != ''}
        opts_iterator = 0
    
    return encode_dict, decode_dict

if __name__ == '__main__':
    main()