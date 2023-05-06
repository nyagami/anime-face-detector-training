# anime-face-detector-training

# Yêu cầu môi trường
- python 3
- pip 3
- python virtualenv
- Photoshop hoặc photoshop online

# Cài đặt
Tạo virtualenv
```
virtualenv venv
```

Kích hoạt virtualenv
```
./venv/Scripts/activate
```

Clone source
```
git clone https://github.com/nyagami/anime-face-detector-training.git
```

Cài đặt môi trường
```
cd anime-face-detector-training
```
```
pip install -r requirements.txt
```

# Tạo dữ liệu

## Positvie
1. Tạo thư mục `bounded_psds`
2. Mở photoshop online
3. Kéo thả hoặc mở ảnh chứa mặt nhân vật anime
4. Tên layer của ảnh phải là `Background`. Hãy sửa lại nếu nó là tên khác
5. Sử dụng công cụ `shape`, dạng `hình chữ nhật` (hoặc hình vuông)
6. Vẽ hình chữ nhật lên vị trí các khuôn mặt
![image](https://user-images.githubusercontent.com/86464880/236613315-d33c914c-3427-4d19-bda1-b72ef3ba22ae.png)
7. Lưu lại định dạng PSD và chuyển vào thư mục `bounded_psds` vừa tạo, tương tự cho các ảnh khác
8. Khi đã tạo đủ dữ liệu, tiến hành generate data
```
py get_bounds.py
```
- Ảnh sẽ được tách từ file psd và lưu vào thư mục `pos`
- Dữ liệu về ảnh sẽ được lưu tại `pos.data`

## Negative
1. Tạo thư mục `neg`
2. Thêm những ảnh không có mặt nhân vật anime vào, ảnh lưu dưới dạng gray scale (đen trắng)

## Training
```
py train.py
```
- file `animeface.xml` đã được tạo

# Kiểm thử 
- Tạo thư mục `input`
- Thêm ảnh muốn detect (bao gồm cả có màu)
```
py main.py
```
- Kết quả sẽ được lưu tại thư mục `output`
