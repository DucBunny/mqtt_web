### Kiểm tra Execution Policy hiện tại

Get-ExecutionPolicy

### Gõ lệnh sau để thay đổi chính sách

Set-ExecutionPolicy Unrestricted -Scope Process

### Hoặc nếu bạn muốn áp dụng vĩnh viễn (có thể gây rủi ro bảo mật), dùng:

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

### Kích hoạt lại môi trường ảo

myenv\Scripts\Activate

### Sau khi làm xong, nếu muốn khôi phục lại chính sách mặc định, chạy:

Set-ExecutionPolicy Restricted -Scope CurrentUser

### Chạy Mosquitto

mosquitto -v
