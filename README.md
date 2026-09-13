# Word Guessing Game

Ứng dụng đoán từ được xây dựng bằng Python, gồm giao diện đồ họa (GUI) và giao diện dòng lệnh (CLI). Người chơi chọn độ khó, đoán từng chữ cái và cố gắng tìm ra từ bí mật trước khi hết lượt.

## Tính năng

- Ba mức độ: Easy, Medium và Hard.
- Giao diện GUI bằng Tkinter.
- Có thể đoán bằng cách click các nút chữ hoặc dùng bàn phím thật.
- Hiển thị gợi ý, số mạng, điểm số và các chữ cái đã đoán.
- Trái tim thể hiện số mạng còn lại.
- Lưu lịch sử các ván chơi vào `game_history.txt`.
- Có phiên bản chạy trên terminal bằng CLI.

## Yêu cầu

- Python 3.8 trở lên.
- Tkinter, thường được cài sẵn cùng Python trên Windows.
- Không cần cài thêm thư viện bên ngoài.

## Cấu trúc dự án

```text
ICT401_Assessment3/
├── cli_app.py                 # Phiên bản chạy trên terminal
├── engine.py                  # Logic chính của trò chơi
├── gui_app.py                 # Phiên bản giao diện đồ họa
├── game_history.txt           # Lịch sử các ván chơi
├── words/
│   ├── easy.txt               # Danh sách từ dễ
│   ├── medium.txt             # Danh sách từ trung bình
│   └── hard.txt               # Danh sách từ khó
└── README.md
```

## Cách chạy giao diện đồ họa

Mở terminal tại thư mục dự án và chạy:

```bash
python gui_app.py
```

Sau đó chọn độ khó. Khi game bắt đầu, bạn có thể click các nút chữ trên màn hình hoặc nhấn chữ cái trên bàn phím thật.

## Cách chạy phiên bản CLI

```bash
python cli_app.py
```

Trong CLI, nhập số tương ứng với độ khó và nhập từng chữ cái để đoán. Nhập `quit` trong khi chơi để thoát ván hiện tại.

## Định dạng file từ vựng

Mỗi dòng trong các file thuộc thư mục `words/` phải có định dạng:

```text
WORD|Hint for the word
```

Ví dụ:

```text
APPLE|A red or green fruit
```

Dấu `|` được dùng để phân cách từ và gợi ý. Từ và gợi ý không được để trống.

## Luật chơi

- Mỗi ván có 6 mạng.
- Đoán đúng sẽ mở các vị trí của chữ cái trong từ.
- Đoán sai sẽ mất 1 mạng.
- Mỗi chữ cái đúng được tính điểm dựa trên số lần xuất hiện trong từ.
- Người chơi thắng khi đoán được toàn bộ chữ cái của từ.
- Người chơi thua khi số mạng còn lại bằng 0.

## Lịch sử chơi

Sau khi ván chơi kết thúc, kết quả được thêm vào `game_history.txt` theo định dạng:

```text
timestamp|difficulty|word|result|score|number_of_guesses
```

## Tác giả

Truong Giang Nguyen  
Student ID: 202572186
