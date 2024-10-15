# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan perguruan yang telah beroperasi sejak tahun 2000, dikenal atas keberhasilannya mencetak lulusan berkualitas dengan reputasi yang baik. Namun, meskipun memiliki rekam jejak yang mengesankan, institut ini menghadapi tantangan serius berupa tingkat dropout siswa yang cukup tinggi. Masalah ini berpotensi merusak reputasi dan keberlanjutan institusi. Oleh karena itu, untuk menjaga kualitas pendidikan dan keberhasilan siswa, Jaya Jaya Institut berupaya mendeteksi siswa yang berisiko dropout sejak dini, agar dapat diberikan bimbingan khusus yang dapat membantu mereka menyelesaikan pendidikan dengan baik.

### Permasalahan Bisnis
Berikut adalah permasalahan bisnis yang ingin diselesaikan oleh Jaya Jaya Institut:
1. Tingkat Dropout yang Tinggi: Banyak siswa yang tidak menyelesaikan pendidikannya, yang berdampak negatif terhadap reputasi dan keberlanjutan institusi sehingga perlu diketahui faktor-faktor yang mempengaruhi tingkat dropout.
2. Kurangnya Deteksi Dini terhadap Siswa Berisiko: Saat ini, tidak ada mekanisme efektif untuk mendeteksi secara dini siswa yang berpotensi dropout, sehingga intervensi yang tepat waktu sulit dilakukan.

### Cakupan Proyek
Proyek ini menghasilkan laporan yang mencakup analisis mendalam dari tingkat dropout siswa, faktor-faktor penyebabnya, serta rekomendasi strategi untuk menurunkan potensi dropout siswa di Jaya Jaya Institu. Selain itu proyek ini akan mengembangkan business dashboard yang memungkinkan pemantauan faktor penyebab dropout secara real-time dan solusi machine learning, guna mendukung pengambilan keputusan yang lebih cepat dan berbasis data.

### Persiapan

Sumber data: Data Student Performance Jaya Jaya Institut

Setup environment:
```
conda create --name student-performance-analysis python=3.9
conda activate student-performance-analysis
pip install -r requirements.txt
jupyter-notebook .
```

## Business Dashboard
Berdasarkan [Business Dashboard Student Performance](https://lookerstudio.google.com/reporting/ac1319b0-e91c-4102-bf68-5f094fae9690) dapat diambil beberapa informasi sebagai berikut:
1. Dropout Rate Jaya Jaya Institut adalah 32,12%
2. Rata-rata Admission Grade siswa yang dropout adalah 124,96
3. Rata-rata Previous Qualification Grade siswa yang dropout adalah 131,11
4. Ada 17.9% siswa dengan status enrolled yang masih potensial untuk dibantu hingga menjadi Graduated
5. 32.2% siswa yang dropout memiliki masalah dalam biaya
6. Siswa yang berstatus dropout mayoritas berusia 18-19 tahun saat pendaftaran
7. Tiga Course tertinggi yang diambil siswa dropout adalah Management, Nursing, dan Journalism and Communication


## Menjalankan Sistem Machine Learning
Untuk menjalankan sistem machine learning yang telah dibuat dapat mengikuti langkah-langkah sebagai berikut

```
conda create --name student-performance-deploy python=3.9
conda activate student-performance-deploy
pip install -r requirements.txt
streamlit run app.py
```

atau dapat langsung mengakses prototype nya pada laman berikut [Student Performance Machine Learning](https://student-perform.streamlit.app/)

## Conclusion
Berdasarkan dari analisis yang dilakukan dapat ditarik kesimpulan sebagai berikut:
1. Tingkat Dropout siswa Jaya Jaya Institut tinggi yaitu 32.12%. Beberapa faktor yang paling mempengaruhi dropout tersebut adalah Curricular Unit (credited, enrolled, evaluations, approved, grade, without evaluations) di semester pertama dan kedua, Tuition fees up to date, Admission Grade, Age at Enrollment, Previous qualification grade, dan Course.
2. Dari data student performance dapat dibangun model machine learning menggunakan Algoritma Random Forest dengan akurasi sebesar 74% sehingga dapat digunakan sebagai pendeteksi awal siswa yang berpotensi Dropout.

### Rekomendasi Action Items
Beberapa hal yang dapat dilakukan untuk mengurangin dropout rate adalah sebagai berikut:
- Membantu siswa yang kesulitan dalam pembayaran karena cukup banyak siswa yang dropout mengalami kesulitan dalam pembayaran
- Melakukan evaluasi terhadap course yang diambil oleh siswa yang dropout antara lain Management, Nursing, Journalism and Communication sehingga dapat diketahui apakah ada kendala dalam course tersebut yang menyebabkan siswa dropout 
