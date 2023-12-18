import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Sistem Prediksi Diabetes')

# Input untuk nilai-nilai variabel
# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Masukkan nilai Pregnancies')

with col2:
    Glucose = st.text_input('Masukkan nilai Glucose')

with col1:
    BloodPressure = st.text_input('Masukkan nilai Blood Pressure')

with col2:
    SkinThickness = st.text_input('Masukkan nilai Skin Thickness')

with col1:
    Insulin = st.text_input('Masukkan nilai Insulin')

with col2:
    BMI = st.text_input('Masukkan nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Masukkan nilai Diabetes Pedigree Function')

with col2:
    Age = st.text_input('Masukkan nilai Age')

# Code untuk prediksi
diabetes_diagnosis = ''

# Tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    try:
        # Mengonversi input ke tipe numerik
        input_data = [[Pregnancies, Glucose, BloodPressure,
                       SkinThickness, Insulin, BMI,
                       DiabetesPedigreeFunction, Age]]

        # Prediksi menggunakan model
        diabetes_prediction = diabetes_model.predict(input_data)

        if diabetes_prediction[0] == 0:
            diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'
        else:
            diabetes_diagnosis = 'Pasien Terkena Diabetes'

        if diabetes_prediction[1] == 1:
            diabetes_diagnosis = 'Pasien Terkena Diabetes'
        else:
            diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'

        # Menampilkan hasil prediksi
        st.success(diabetes_diagnosis)

    except ValueError:
        st.error('Pastikan semua input adalah angka.')
