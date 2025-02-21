## 1. Tạo môi trường ảo Python

#### Step 1: Cài đặt `virtualenv` (nếu chưa có)

    pip install virtualenv

#### Step 2: Tạo môi trường ảo

    python -m venv myenv

Thay `myenv` bằng tên thư mục bạn muốn đặt cho môi trường ảo.

#### Step 3: Kích hoạt môi trường ảo

**Trên `Windows`:**

    myenv\Scripts\activate

**Trên `macOS/Linux`:**

    source myenv/bin/activate

#### Step 4: Cài đặt các gói trong môi trường ảo

    pip install ...

`django`
`paho-mqtt`

#### Step 5: Thoát khỏi môi trường ảo

    deactivate

## 2. Nếu lỗi khi active

#### Step 1: Kiểm tra `Execution Policy` hiện tại trong `cmd`

    Get-ExecutionPolicy

Nếu nó trả về `Restricted`, nghĩa là script PowerShell bị chặn.

#### Step 2: Gõ lệnh sau để thay đổi chính sách

    Set-ExecutionPolicy Unrestricted -Scope Process

#### Hoặc nếu bạn muốn áp dụng vĩnh viễn (có thể gây rủi ro bảo mật), dùng:

    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

#### Step 3: Kích hoạt lại môi trường ảo

    myenv\Scripts\Activate

#### Step 4: Sau khi làm xong, nếu muốn khôi phục lại chính sách mặc định, chạy:

    Set-ExecutionPolicy Restricted -Scope CurrentUser

## 3. Cài đặt `Mosquitto`

#### Step 1: Tải file `.exe`

Vào [Mosquitto](https://mosquitto.org/download/)

#### Step 2: Thêm `Mosquitto` vào System PATH

-   Nhấn `Win + R`, gõ `sysdm.cpl`, nhấn `Enter`
-   Chuyển sang tab `Advanced`, bấm vào `Environment Variables`
-   Trong phần `System variables`, tìm và chọn `Path`, rồi bấm `Edit`
-   Bấm `New`, nhập đường dẫn thư mục `Mosquitto`, ví dụ: `C:\Program Files\Mosquitto`

#### Step 3: Chạy `Mosquitto Broker` tại cmd

    mosquitto -v

## 4. Sử dụng `Mosquitto MQTT` trên cùng mạng LAN

#### Step 1: Tìm địa chỉ IP của thiết bị chạy `Mosquitto` trong cmd

    ipconfig

#### Step 2: Chạy `Mosquitto Broker`

    mosquitto -v

#### Step 3: Tạo `pub.py` và đổi `IP Broker`

Ví dụ: ![1](./doc/pub.png)
