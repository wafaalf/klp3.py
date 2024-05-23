import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# navigasi sidebar
with st.sidebar.radio :
    selected = option_menu ('Home',
    ['Introduction',
    'Information',
    'Penetapan Kadar Cl %(b/v)'],
    default_index=0)

# halaman introduction
if (selected == 'Introduction') :
    st.title('Perkenalan Kelompok')
    
    st.header('Halo Perkenalkan kami dari kelompok 3')
    
    st.write('Anggota :')
    st.write('Arya Pratama Widya Putra (2360077)')
    st.write('Asriyanti Lestari (2360078)')
    st.write('Azka Afriyuni Suwito (2360084)')
    st.write('Shintya Ingrid Mellyana Manik (2360262)')
    st.write('Wafa Alifiah (2360287)')

if (selected == 'Information') :
    st.title('Informasi tentang perhitungan Kadar Cl %(b/v) secara argentometri dengan metode mohr')
    
    st.write('''Penentuan kadar klorin dapat ditentukan dengan titrasi argentometri, yaitu titrasi dengan menggunakan perak nitrat sebagai titran dimana akan terbentuk garam perak yang sukar larut. Alasan dipilih metode argentometri karena senyawa yang akan dianalisis merupakan golongan halogenida sehingga memerlukan adanya endapan sebagai hasil akhir dari titrasi.''')
    
    st.header('Pengertian Titrasi Argentometri')
    st.write('''Salah satu metode argentometri adalah metode Mohr, yaitu metode yang dipilih berdasarkan indikator yang digunakan dalam titrasi. Titrasi argentometri merupakan titrasi pengendapan yang melibatkan pembentukan endapan dari garam yang tidak mudah larut antara titran dan analit. Hasil yang diperlukan dari titrasi jenis argentometri adalah pencapaian keseimbangan pembentukan yang cepat setiap kali titran ditambahkan pada analit, tidak adanya interferensi yang menggangu titrasi dan titik akhir titrasi mudah diamati.''')
    
    st.header('Prinsip Argentometri dengan Metode Mohr')
    st.write('''Prinsip Argentometri Mohr adalah reaksi pengendapan dimana senyawa klorida dengan tambahan larutan baku sekunder perak nitrat (AgNO3) dan penambahan larutan indikator kalium kromat (K2CrO4) pada permulaan titrasi akan terjadi endapan perak klorida setelah titik ekuivalen, maka dengan penambahan sedikit perak nitrat akan bereaksi dengan kromat dan membentuk endapan perak kromat yang berwarna merah kecokelatan. Penambahan Indikator kalium kromat (K2CrO4) bertujuan untuk mengetahui warna dari titik akhir titrasi.''')

    st.write('Reaksi yang terjadi :')
    st.write('Ag + Cl → AgCl (endapan putih)')
    st.write('2Ag + K2CrO4 → Ag2CrO4 (endapan merah bata)')

    st.write('Rumus kadar Cl %(b/v) :')
    gambar2 = Image.open('rumus.png')
    
    st.image(gambar2)

if (selected == 'Penetapan Kadar Cl %(b/v)') :
    st.title('Perhitungan Kadar Cl %(b/v) menggunakan cara Mohr')
    
    Volume_AgNO3 = st.number_input('Masukkan nilai volume AgNO3 (mL)',key='Volume_AgNO3')
    Normalitas_AgNO3 = st.number_input('Masukkan nilai normalitas AgNO3 (mgrek/mL)',format='%.4f',key='Normalitas_AgNO3')
    BE_Cl = st.number_input('Masukkan nilai BE Cl (mg/mgrek)',format='%.1f',key='BE_Cl')
    Volume_sampel = st.number_input('Masukkan nilai volume sampel (mL)',format='%.0f',key='Volume_sampel')
    
    hitung = st.button('Hitung Kadar Cl')
        
    if hitung : 
        Kadar_Cl = (Volume_AgNO3 * Normalitas_AgNO3 * BE_Cl * 10**-3 * 100) / Volume_sampel
        st.success(f'Persentase kadarnya adalah{Kadar_Cl:.2f}%(b/v)')