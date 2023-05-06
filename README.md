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

Clone source
```
git clone https://github.com/nyagami/anime-face-detector-training.git
```

Cài đặt môi trường
```
cd anime-face-detector-training
pip install -r requirements.txt
```

# Tạo dữ liệu
## Lưu ý: toàn bộ ảnh đều phải convert sang gray scale (đen trắng)
## Positvie
1. Tạo thư mục `pos`
2. Mở photoshop online
3. Kéo thả hoặc mở ảnh chứa mặt nhân vật anime
4. Tên layer của ảnh phải là `Background`. Hãy sửa lại nếu nó là tên khác
5. Sử dụng công cụ `shape`, dạng `hình chữ nhật` (hoặc hình vuông)
6. Vẽ hình chữ nhật lên vị trí các khuôn mặt
![image](https://user-images.githubusercontent.com/86464880/236602498-0aeffd5f-f575-4b87-ad8c-6b936f97f693.png)
7. Lưu lại định dạng PSD và chuyển vào thư mục `pos` vừa tạo, tương tự cho các ảnh khác

## Negative
`. Tạo thư mục `neg`
2. Thêm những ảnh không có mặt nhân vật anime vào
