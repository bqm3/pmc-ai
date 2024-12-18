import json

schema_info = {
    "ent_checklistreplace": {
        "description": "Thông tin về checklist thay thế",
        "columns": [
            {"name": "ID_ChecklistReplace", "type": "INTEGER", "description": "Mã định danh của checklist thay thế"},
            {"name": "ID_Checklist", "type": "INTEGER", "description": "Mã định danh của checklist"},
            {"name": "MotaLoi", "type": "TEXT", "description": "Mô tả lỗi"},
            {"name": "Songay", "type": "INTEGER", "description": "Số ngày"},
            {"name": "Solan", "type": "INTEGER", "description": "Số lần"},
            {"name": "Ngaybatdau", "type": "DATE", "description": "Ngày bắt đầu"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"}
        ]
    },
    "ent_chinhanh": {
        "description": "Thông tin về chi nhánh",
        "columns": [
            {"name": "ID_Chinhanh", "type": "INTEGER", "description": "Mã định danh của chi nhánh"},
            {"name": "Tenchinhanh", "type": "VARCHAR", "description": "Tên chi nhánh"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
     "ent_linhvuc": {
        "description": "Thông tin về lĩnh vực dự án",
        "columns": [
            {"name": "ID_Linhvuc", "type": "INTEGER", "description": "Mã định danh của lĩnh vực"},
            {"name": "LinhVuc", "type": "VARCHAR", "description": "Tên lĩnh vực"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    }, 
    "ent_nhom": {
        "description": "Thông tin về nhóm dự án ",
        "columns": [
            {"name": "ID_Nhom", "type": "INTEGER", "description": "Mã định danh của nhóm dự án"},
            {"name": "Tennhom", "type": "VARCHAR", "description": "Tên nhóm dự án"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    }, 
     "ent_phanloaida": {
        "description": "Thông tin về phân loại dự án",
        "columns": [
            {"name": "ID_Phanloai", "type": "INTEGER", "description": "Mã định danh của phân loại"},
            {"name": "Phanloai", "type": "VARCHAR", "description": "Tên phân loại"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    }, 
     "ent_tang": {
        "description": "Thông tin về tầng dự án",
        "columns": [
            {"name": "ID_Tang", "type": "INTEGER", "description": "Mã định danh của phân loại"},
            {"name": "ID_Duan", "type": "INTEGER", "description": "Mã định danh của dự án"},
            {"name": "Tentang", "type": "VARCHAR", "description": "Tên phân loại"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    }, 
    "ent_loaihinhbds": {
        "description": "Thông tin về loại hình bất động sản dự án",
        "columns": [
            {"name": "ID_Loaihinh", "type": "INTEGER", "description": "Mã định danh của loại hình bất động sản"},
            {"name": "Loaihinh", "type": "VARCHAR", "description": "Tên loại hình bất động sản"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_toanha": {
        "description": "Thông tin về tòa nhà",
        "columns": [
            {"name": "ID_Toanha", "type": "INTEGER", "description": "Mã định danh của tòa nhà"},
            {"name": "ID_Duan", "type": "INTEGER", "description": "Mã định danh của dự án"},
            {"name": "Toanha", "type": "VARCHAR", "description": "Tên tòa nhà"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_calv": {
        "description": "Thông tin về ca làm việc",
        "columns": [
            {"name": "ID_Calv", "type": "INTEGER", "description": "Mã định danh của ca làm việc"},
            {"name": "ID_Duan", "type": "INTEGER", "description": "Mã định danh của dự án"},
            {"name": "ID_KhoiCV", "type": "INTEGER", "description": "Mã định danh của khối công việc"},
            {"name": "ID_User", "type": "INTEGER", "description": "Mã định danh của người tạo"},
            {"name": "Tenca", "type": "VARCHAR", "description": "Tên ca làm việc"},
            {"name": "Giobatdau", "type": "TIME", "description": "Giờ bắt đầu vào ca"},
            {"name": "Gioketthuc", "type": "TIME", "description": "Giờ kết thúc ca"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_chucvu": {
        "description": "Thông tin về chức vụ",
        "columns": [
            {"name": "ID_Chucvu", "type": "INTEGER", "description": "Mã định danh chức vụ"},
            {"name": "Chucvu", "type": "VARCHAR", "description": "Tên chức vụ"},
            {"name": "Role", "type": "INTEGER", "description": "Quyền hạn"},
            {"name": "Ghichu", "type": "VARCHAR", "description": "Ghi chú"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_thietlapca": {
        "description": "Thông tin về thiết lập ca dự án",
        "columns": [
            {"name": "ID_ThietLapCa", "type": "INTEGER", "description": "Mã định danh thiết lập ca"},
            {"name": "ID_Calv", "type": "INTEGER", "description": "Mã định danh ca làm việc"},
            {"name": "ID_Hangmucs", "type": "JSON", "description": "Chứa các ID_Hangmuc"},
            {"name": "ID_Duan", "type": "INTEGER", "description": "Mã định danh dự án"},
            {"name": "Sochecklist", "type": "INTEGER", "description": "Tổng số lượng cần checklist"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_duan": {
        "description": "Thông tin dự án",
        "columns": [
            {"name": "ID_Duan", "type": "INTEGER", "description": "Mã định danh dự án"},
            {"name": "ID_Nhom", "type": "INTEGER", "description": "Mã định danh nhóm"},
            {"name": "ID_Chinhanh", "type": "INTEGER", "description": "Mã định danh chi nhánh"},
            {"name": "ID_Linhvuc", "type": "INTEGER", "description": "Mã định danh lĩnh vực"},
            {"name": "Duan", "type": "VARCHAR", "description": "Tên dự án"},
            {"name": "Diachi", "type": "VARCHAR", "description": "Địa chỉ dự án"},
            {"name": "Vido", "type": "TEXT", "description": "Vĩ độ"},
            {"name": "Kinhdo", "type": "TEXT", "description": "Kinh độ"},
            {"name": "Logo", "type": "TEXT", "description": "Logo dự án"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_khoicv": {
        "description": "Thông tin về khối công việc",
        "columns": [
            {"name": "ID_KhoiCV", "type": "INTEGER", "description": "Mã định danh khối công việc"},
            {"name": "KhoiCV", "type": "INTEGER", "description": "Tên khối công việc"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
     "ent_duan_khoicv": {
        "description": "Thông tin về các khối có trong dự án",
        "columns": [
            {"name": "ID_Duan_KhoICV", "type": "INTEGER", "description": "Mã định danh khối dự án"},
            {"name": "ID_KhoiCV", "type": "INTEGER", "description": "Khóa ngoại của bảng ent_khoicv"},
            {"name": "ID_Duan", "type": "INTEGER", "description": "Khóa ngoại của bảng ent_duan"},
            {"name": "Ngaybatdau", "type": "DATE", "description": "Ngày bắt đầu thực hiện checklist"},
           {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_khuvuc": {
        "description": "Thông tin về hạng mục",
        "columns": [
            {"name": "ID_Khuvuc", "type": "INTEGER", "description": "Mã định danh khu vực"},
            {"name": "ID_Toanha", "type": "INTEGER", "description": "Mã định danh tòa nhà"},
            {"name": "ID_Tang", "type": "INTEGER", "description": "Mã định danh tầng"},
            {"name": "ID_KhoiCVs", "type": "JSON", "description": "Chứa nhiều khóa ngoại ID_KhoiCV"},
            {"name": "MaQrCode", "type": "VARCHAR", "description": "Mã QR Code"},
            {"name": "Makhuvuc", "type": "VARCHAR", "description": "Mã khu vực"},
            {"name": "Sothutu", "type": "INTEGER", "description": "Số thứ tự khu vực"},
            {"name": "Tenkhuvuc", "type": "VARCHAR", "description": "Tên khu vực"},
            {"name": "ID_User", "type": "INTEGER", "description": "Người tạo khu vực"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
     "ent_khuvuc_khoicv": {
        "description": "Thông tin về các khối có trong dự án",
        "columns": [
            {"name": "ID_KV_CV", "type": "INTEGER", "description": "Mã định danh khối dự án"},
            {"name": "ID_KhoiCV", "type": "INTEGER", "description": "Khóa ngoại của bảng ent_khoicv"},
            {"name": "ID_Khuvuc", "type": "INTEGER", "description": "Khóa ngoại của bảng ent_duan"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_hangmuc": {
        "description": "Thông tin về hạng mục",
        "columns": [
            {"name": "ID_Hangmuc", "type": "INTEGER", "description": "Mã định danh hạng mục"},
            {"name": "ID_Khuvuc", "type": "INTEGER", "description": "Mã định danh khu vực"},
            {"name": "Hangmuc", "type": "TEXT", "description": "Tên hạng mục"},
            {"name": "Tieuchuankt", "type": "TEXT", "description": "Tiêu chuẩn kiểm tra"},
            {"name": "MaQrCode", "type": "VARCHAR", "description": "Mã QR Code"},
            {"name": "Sothutu", "type": "INTEGER", "description": "Số thứ tự"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "ent_checklist": {
        "description": "Thông tin về checklist",
        "columns": [
            {"name": "ID_Checklist", "type": "INTEGER", "description": "Mã định danh checklist"},
            {"name": "ID_Khuvuc", "type": "INTEGER", "description": "Mã định danh khu vực"},
            {"name": "ID_Hangmuc", "type": "INTEGER", "description": "Mã định danh tòa nhà"},
            {"name": "ID_Tang", "type": "INTEGER", "description": "Mã định danh tầng"},
            {"name": "Checklist", "type": "VARCHAR", "description": "Tên checklist cần kiểm tra"},
            {"name": "Giatridinhdanh", "type": "VARCHAR", "description": "Giá trị định danh là giá trị mặc định đúng"},
            {"name": "Giatrinhan", "type": "VARCHAR", "description": "Giá trị nhận là các giá trị các nhau bằng dấu /"},
            {"name": "Giatriloi", "type": "VARCHAR", "description": "Là giá trị lỗi khi chọn từ giá trị nhận"},
            {"name": "Tieuchuan", "type": "VARCHAR", "description": "Tiêu chuẩn kiểm tra để chọn giá trị"},
            {"name": "isCheck", "type": "INTEGER", "description": "0 là chọn select theo giá trị nhận, 1 là nhập dữ liệu"},
            {"name": "Tinhtrang", "type": "INTEGER", "description": "0 là bình thường, 1 là checklist đó đang lỗi"},
            {"name": "ID_User", "type": "INTEGER", "description": "Người tạo checklist"},
            {"name": "isImportant", "type": "INTEGER", "description": "0 là bình thường, 1 là quan trọng"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "tb_checklistc": {
        "description": "Thông tin về ca thực hiện checklist",
        "columns": [
            {"name": "ID_ChecklistC", "type": "INTEGER", "description": "Mã định danh ca checklist"},
            {"name": "ID_Duan", "type": "INTEGER", "description": "Mã định danh dự án"},
            {"name": "ID_KhoiCV", "type": "INTEGER", "description": "Mã định danh khối công việc"},
            {"name": "ID_ThietLapCa", "type": "INTEGER", "description": "Mã định danh thiết lập ca"},
            {"name": "ID_Calv", "type": "INTEGER", "description": "Mã định danh ca làm việc"},
            {"name": "ID_User", "type": "INTEGER", "description": "Mã định danh người thực hiện ca checklist"},
            {"name": "ID_Hangmucs", "type": "JSON", "description": "Danh sách các ID_Hangmuc cần thực hiện trong ca đó"},
            {"name": "TongC", "type": "INTEGER", "description": "Tổng checklist đã kiểm tra"},
            {"name": "Tong", "type": "INTEGER", "description": "Tổng checklist phải thực hiện"},
            {"name": "Ngay", "type": "DATE", "description": "Ngày thực hiện ca checklist"},
            {"name": "Giobd", "type": "TIME", "description": "Giờ bắt đầu ca checklist"},
            {"name": "Giokt", "type": "TIME", "description": "Giờ đóng ca checklist"},
            {"name": "Tinhtrang", "type": "INTEGER", "description": "Tình trạng đóng ca ( 0 là chưa đóng, 1 là đã đóng)"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "tb_checklistchitiet": {
        "description": "Thông tin về ca thực hiện checklist",
        "columns": [
            {"name": "ID_Checklistchitiet", "type": "INTEGER", "description": "Mã định danh checklist chi tiết"},
            {"name": "ID_ChecklistC", "type": "INTEGER", "description": "Mã định danh ca checklist"},
            {"name": "ID_Checklist", "type": "INTEGER", "description": "Mã định danh ca checklist"},
            {"name": "Ketqua", "type": "VARCHAR", "description": "Kết quả của checklist"},
            {"name": "Anh", "type": "VARCHAR", "description": "Hình ảnh checklist"},
            {"name": "Ngay", "type": "DATE", "description": "Ngày thực hiện checklist"},
            {"name": "Gioht", "type": "TIME", "description": "Giờ hoàn thành checklist đó"},
            {"name": "Kinhdo", "type": "VARCHAR", "description": "Kinh độ"},
            {"name": "Vido", "type": "VARCHAR", "description": "Vĩ độ"},
            {"name": "Docao", "type": "VARCHAR", "description": "Độ cao"},
            {"name": "isScan", "type": "INTEGER", "description": "Kiểm tra có quét qr code hay không (Null là có quét, 1 là không quét )"},
            {"name": "isCheckListLai", "type": "INTEGER", "description": "Có phải checklist lại hay không (0 là không, 1 là checklist lại)"},
            {"name": "Ghichu", "type": "VARCHAR", "description": "Ghi chú cho checklist"},
           {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
     "tb_checklistchitietdone": {
        "description": "Thông tin về ca thực hiện checklist",
        "columns": [
            {"name": "ID_Checklistchitietdone", "type": "INTEGER", "description": "Mã định danh checklist chi tiết"},
            {"name": "ID_ChecklistC", "type": "INTEGER", "description": "Mã định danh ca checklist"},
            {"name": "Description", "type": "VARCHAR", "description": "Danh sách chứa các ID_Checklist( giá trị mặc đinh là giá trị định danh)"},
            {"name": "Gioht", "type": "TIME", "description": "Giờ hoàn thành checklist đó"},
            {"name": "Kinhdo", "type": "VARCHAR", "description": "Kinh độ"},
            {"name": "Vido", "type": "VARCHAR", "description": "Vĩ độ"},
            {"name": "Docao", "type": "VARCHAR", "description": "Độ cao"},
            {"name": "isScan", "type": "INTEGER", "description": "Kiểm tra có quét qr code hay không (Null là có quét, 1 là không quét )"},
            {"name": "isCheckListLai", "type": "INTEGER", "description": "Có phải checklist lại hay không (0 là không, 1 là checklist lại)"},
            {"name": "Ghichu", "type": "VARCHAR", "description": "Ghi chú cho checklist"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    # Thêm các bảng khác tương tự
    "ent_user": {
        "description": "Thông tin người dùng",
        "columns": [
            {"name": "ID_User", "type": "INTEGER", "description": "Mã định danh người dùng"},
            {"name": "UserName", "type": "VARCHAR", "description": "Tên đăng nhập"},
            {"name": "Hoten", "type": "VARCHAR", "description": "Họ tên người dùng"},
            {"name": "Email", "type": "VARCHAR", "description": "Email"},
            {"name": "Ngaysinh", "type": "DATE", "description": "Ngày sinh"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
    "nlr_ai": {
        "description": "Thông tin chi tiết ca checklist (kiểm tra)",
        "columns": [
            {"name": "ID_AI", "type": "INTEGER", "description": "Mã định danh"},
            {"name": "Tenduan", "type": "VARCHAR", "description": "Tên dự án"},
            {"name": "Tenkhoi", "type": "VARCHAR", "description": "Tên khối công việc"},
            {"name": "Tenca", "type": "VARCHAR", "description": "Tên ca làm việc"},
            {"name": "Giamsat", "type": "VARCHAR", "description": "Tên người giám sát"},
            {"name": "Ngay", "type": "DATE", "description": "Ngày thực hiện kiểm tra"},
            {"name": "Tilehoanthanh", "FLOAT": "DATE", "description": "Tỉ lệ hoàn thành của người đấy trong ca đấy"},
            {"name": "TongC", "type": "INTEGER", "description": "Tổng đã kiểm tra"},
            {"name": "Tong", "type": "INTEGER", "description": "Tổng phải kiểm tra"},
            {"name": "Thoigianmoca", "type": "TIME", "description": "Thời gian mở ca làm việc"},
            {"name": "Thoigianchecklistbatdau", "type": "TIME", "description": "Thời gian checklist bắt đầu thực hiện"},
            {"name": "Thoigianchecklistketthuc", "type": "TIME", "description": "Thời gian checklist kết thúc"},
            {"name": "Thoigiantrungbinh", "type": "TIME", "description": "Thời gian trung bình"},
            {"name": "Thoigianchecklistngannhat", "type": "TIME", "description": "Thời gian checklist ngắn nhất"},
            {"name": "Thoigianchecklistlaunhat", "type": "TIME", "description": "Thời gian checklist lâu nhất"},
            {"name": "Soluongghichu", "type": "INTEGER", "description": "Số lượng ghi chú trong một ca"},
            {"name": "Soluonghinhanh", "type": "INTEGER", "description": "Số lượng hình ảnh trong một ca"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
     "ent_tile": {
        "description": "Tỉ lệ checklist các khối của dự án",
        "columns": [
            {"name": "ID_Tile", "type": "INTEGER", "description": "Mã định danh"},
            {"name": "Tenduan", "type": "VARCHAR", "description": "Tên dự án"},
            {"name": "Ngay", "type": "DATE", "description": "Ngày"},
            {"name": "Khoibaove", "type": "FLOAT", "description": "Khối bảo vệ ( khối an ninh)"},
            {"name": "Khoilamsach", "type": "FLOAT", "description": "Khối làm sạch"},
            {"name": "Khoikythuat", "type": "FLOAT", "description": "Khối kỹ thuật"},
            {"name": "Khoidichvu", "type": "FLOAT", "description": "Khối dịch vụ"},
            {"name": "KhoiFB", "type": "FLOAT", "description": "Khối F&B"},
            {"name": "isDelete", "type": "INTEGER", "description": "Trạng thái xóa( 0 là hiển thị, 1 là xóa)"},
            {"name": "createdAt", "type": "TIMESTAMP", "description": "Thời gian tạo"},
            {"name": "updatedAt", "type": "TIMESTAMP", "description": "Thời gian cập nhật"}
        ]
    },
}

# Ghi schema ra file JSON
output_file = "schema_info.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(schema_info, f, indent=4, ensure_ascii=False)

print(f"Schema đã được lưu trong tệp {output_file}")
