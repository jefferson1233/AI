import traceback
from sklearn.preprocessing import LabelEncoder

'''-----------------------------------------------------------'''
'''                   Diego Cruz  @di3cruz                    '''
'''-----------------------------------------------------------'''


'''--------------------- Encoder & decoded label --------'''
# Return the variable to target numerically
# 1) Fit: object_encoder: fn_label_encoder(df,"name_column")
# 2) transform labels: y_encoded = object_encoder.transform(df["name_column"])
# 3) Decoded target:  y_decoded = object_encoder.inverse_transform([number code])


def fn_label_encoder(df, name_column):
    le = LabelEncoder()
    try:
        le.fit(df[name_column])
        return le
    except Exception as e:
        print("Error in function fn_label_encoder")
        print("type error: " + str(e))
        print(traceback.format_exc())
        exit()