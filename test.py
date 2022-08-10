import pandas as pd
import streamlit as st
import extra_streamlit_components as stx

import os
import time
import dtale




def save_uploaded_file(directory, filename, file):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename), 'wb') as f:
        f.write(file)
    return st.success(f'File {filename} uploaded successfully in {directory}')

def delete_file(path):
    if isinstance(path, list):
        for p in path:
            os.remove(p)
    else:
        os.remove(path)



# ----------------------------------------------------------------------------------------------------------------------
# 페이지 세팅
st.set_page_config(layout='wide')


# ----------------------------------------------------------------------------------------------------------------------
# 사이드 바 세팅
st.sidebar.title("Anomaly Detection")
st.sidebar.markdown("""Choose your data type.""")
select = st.sidebar.selectbox("if you want manage files, select file manager.", ("Time Series Data", "Sound Data", "Image Data", "File Manager"))




# ----------------------------------------------------------------------------------------------------------------------
# 타임시리즈 데이터 부분.
if select == "Time Series Data":
    with st.sidebar:
        val = stx.stepper_bar(steps=["Ready", "Data Upload", "Data Preprocess", "Set Hyperparameters", "Train Model", "Predict"], is_vertical=True, lock_sequence=True)

    if val == 0:
        st.title("Time series data anomaly detection")
        st.markdown("""
        """)
        import pandas as pd
        from dtale.views import startup

        df = pd.DataFrame([1, 2, 3, 4])
        startup(data_id="1", data=df)

    elif val == 1:
        st.title("Data Upload")
        st.markdown("""
        Upload your data for train here. it must be labelled.
        """)
        uploaded_file_train = st.file_uploader("Choose a file", key="train_file", accept_multiple_files=True)
        if uploaded_file_train is not None:
            for i in uploaded_file_train:
                df_train = pd.read_csv(i)
                st.subheader("Data preview - {}".format(i.name))
                #st.write(df_train.head())
                bytes_data = i.read()
                

        uploaded_file_test = st.file_uploader("Choose a file", key="test_file", accept_multiple_files=True)
        if uploaded_file_test is not None:
            for i in uploaded_file_test:
                #df_test = pd.read_csv(i)
                st.subheader("Data preview - {}".format(i.name))
                #st.write(df_test.head())
                bytes_data = i.read()
                save_uploaded_file(directory='data/timeseries/test', filename=i.name, file=bytes_data)


        

            




    elif val == 2:
        st.title("Data Preprocess")
        st.markdown("""
        Preprocess your data here.
        """)






    elif val == 3:
        st.title("Set Hyperparameters")
        st.markdown("""
        Set your hyperparameters here.
        """)







    elif val == 4:
        st.title("Train Model")
        st.markdown("""
        Train your model here.
        """)






    elif val == 5:
        st.title("Predict")
        st.markdown("""
        Predict your data here.
        """)

# ----------------------------------------------------------------------------------------------------------------------
# 사운드 데이터 부분.
elif select == "Sound Data":
    with st.sidebar:
        val = stx.stepper_bar(steps=["Ready", "Data Upload", "Set Hyperparameters", "Train Model", "Predict"], is_vertical=True, lock_sequence=True)

    if val == 0:
        st.title("Sound data anomaly detection")
        st.markdown("""
        """)




    elif val == 1:
        st.title("Data Upload")
        st.markdown("""
        Upload your data for train here.
        """)
        uploaded_file_train = st.file_uploader("Choose a file", key="train_file", accept_multiple_files=True)
        if uploaded_file_train is not None:
            for i in uploaded_file_train:
                st.subheader("Data preview - {}".format(i.name))
                #st.audio(i, format='audio/wav')
                bytes_data = i.read()
                save_uploaded_file(directory='data/sound/train', filename=i.name, file=bytes_data)

        uploaded_file_test = st.file_uploader("Choose a file", key="test_file", accept_multiple_files=True)
        if uploaded_file_test is not None:
            for i in uploaded_file_test:
                st.subheader("Data preview - {}".format(i.name))
                #st.audio(i, format='audio/wav')
                bytes_data = i.read()
                save_uploaded_file(directory='data/sound/test', filename=i.name, file=bytes_data)

            




    elif val == 2:
        st.title("Data Preprocess")
        st.markdown("""
        Preprocess your data here.
        """)






    elif val == 3:
        st.title("Set Hyperparameters")
        st.markdown("""
        Set your hyperparameters here.
        """)







    elif val == 4:
        st.title("Train Model")
        st.markdown("""
        Train your model here.
        """)






    elif val == 5:
        st.title("Predict")
        st.markdown("""
        Predict your data here.
        """)







# ----------------------------------------------------------------------------------------------------------------------
# 이미지 데이터 부분.
elif select == "Image Data":
    with st.sidebar:
        val = stx.stepper_bar(steps=["Ready", "Data Upload", "Set Hyperparameters", "Train Model", "Predict"], is_vertical=True, lock_sequence=True)

    if val == 0:
        st.title("Image data anomaly detection")
        st.markdown("""
        """)




    elif val == 1:
        st.title("Data Upload")
        st.markdown("""
        Upload your data for train here.
        """)
        uploaded_file_train = st.file_uploader("Choose a file", key="train_file", accept_multiple_files=True)
        if uploaded_file_train is not None:
            for image in uploaded_file_train:
                st.subheader("Data preview - {}".format(image.name))
                #st.image(image, caption=image.name)
                bytes_data = image.read()
                save_uploaded_file(directory='data/image/train', filename=image.name, file=bytes_data)

        uploaded_file_test = st.file_uploader("Choose a file", key="test_file", accept_multiple_files=True)
        if uploaded_file_test is not None:
            for image in uploaded_file_test:
                st.subheader("Data preview - {}".format(image.name))
                #st.image(image, caption=image.name)
                bytes_data = image.read()
                save_uploaded_file(directory='data/image/test', filename=image.name, file=bytes_data)
            




    elif val == 2:
        st.title("Data Preprocess")
        st.markdown("""
        Preprocess your data here.
        """)






    elif val == 3:
        st.title("Set Hyperparameters")
        st.markdown("""
        Set your hyperparameters here.
        """)







    elif val == 4:
        st.title("Train Model")
        st.markdown("""
        Train your model here.
        """)






    elif val == 5:
        st.title("Predict")
        st.markdown("""
        Predict your data here.
        """)

elif select == "File Manager":
    col1, col2 = st.columns(2)
    dir_path = "./data"
    folder_list =[]
    file_list = []

    for (root, directories, files) in os.walk(dir_path):
        for d in directories:
            d_path = os.path.join(root, d)
            folder_list.append(d_path)
            

        for file in files:
            file_path = os.path.join(root, file)
            
    options = col1.multiselect("select folders", folder_list)

    if options.__len__() > 0:
        for i in options:
            dir_path = i
            for (root, directories, files) in os.walk(dir_path):
                for d in directories:
                    d_path = os.path.join(root, d)
                    folder_list.append(d_path)
                    

                for file in files:
                    file_path = os.path.join(root, file)
                    file_list.append(file_path)

        for i in file_list:
            col1.code(i)
    options2 = col2.multiselect("select files", file_list)

    if col2.button("Delete"):
        delete_file(path=options2)
        col2.success("Deleted : {}".format(options2))
        col2.markdown("""
        if you want to delete more files, please select folder again.
        """)
        
        
        




    
    

    
    
