# Tugas Kecil 3 IF2211 Strategi Algoritma
## Semester 2 (Genap) Tahun 2022/2023
## Implementasi Algoritma UCS dan A* untuk Menentukan Lintasan Terpendek

## Table of Contents
1. [Table of Contents](#table-of-contents)
2. [Deskripsi Program](#deskripsi-program)
3. [Requirements](#requirements)
4. [Cara Clone Program](#cara-clone-program)
5. [Format Input File Text](#format-input-file-text)
6. [Cara Run Program](#cara-run-program)
7. [Authors](#authors)

## Deskripsi Program


## Requirements
- [Python3](https://www.python.org/downloads/) 
- matplotlib
- networkx
- Library time, platform, random, math (standard library, sehingga seharusnya sudah disertakan saat meng-install python)

## Cara Clone Program
Agar program dapat dijalankan pada mesin Anda, clone repository program dengan cara

```sh
git clone https://github.com/rayhanp1402/Tucil3_13521112.git
```

## Format Input File Text
1. Baris pertama: Jumlah dari Node yang akan dimasukkan
2. Baris kedua: Nama dan koordinat kartesius atau geographical (latitude & longitude) dari Node yang dimasukkan baris per baris
3. Baris setelah baris Node terakhir: Adjacency matrix
4. Constraint: Elemen adjacency matrix berupa bilangan real >= 0

Contoh dapat ditemukan pada file text yang ada di dalam folder test
<br>
<br>
Catatan:  
- Apabila format tidak sesuai, mungkin dapat membuat program error atau tidak berjalan sesuai yang diinginkan
- Start Node dan Goal/End Node di-input pengguna pada runtime

## Cara Run Program
Jalankan perintah berikut pada folder root repository
```sh
python src/main.py
```
## Authors
| Nama                              | NIM      |
| ----------------------------------| -------- |
| Rayhan Hanif Maulana Pradana      | 13521112 |
| Irgiansyah Mondo                  | 13521167 |