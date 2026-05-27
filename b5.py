
"""
PHẦN 1 - THIẾT KẾ HỆ THỐNG (ARCHITECTURE & DATA FLOW)
1. INPUT / OUTPUT DESIGN
INPUT (5 trường dữ liệu):
- patient_name (str)
  Input: "Nhập họ và tên bệnh nhân (VD: Nguyen Van A)"
  Type: string

- patient_age (int)
  Input: "Nhập tuổi bệnh nhân (VD: 30)"
  Type: integer

- spo2_level (int)
  Input: "Nhập SpO2 (%) (VD: 98)"
  Type: integer

- heart_rate (int)
  Input: "Nhập nhịp tim (VD: 85)"
  Type: integer

- has_insurance (str -> bool)
  Input: "Bạn có BHYT không? (yes/no)"
  Type: boolean (True/False)

OUTPUT:
- Phiếu khám bệnh điện tử (triage + phí)
- Log hệ thống (type check)

"""

patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))
spo2_level = int(input("Nhập nồng độ oxy SpO2 (%): "))
heart_rate = int(input("Nhập nhịp tim (nhịp/phút): "))
insurance_input = input("Bạn có thẻ BHYT không?: ")


#chuyển đổi dữ liệu từ chuỗi sang kiểu boolean (True/False)
#insurance_input.strip() Xóa khoảng trắng ở đầu và cuối chuỗi .lower() Chuyển toàn bộ về chữ thường... == "yes" Kiểm tra xem chuỗi có đúng là "yes" không

has_insurance = insurance_input.strip().lower() == "yes"
if spo2_level < 90 or heart_rate > 120:
    triage = "🔴 ĐỎ - CẤP CỨU KHẨN"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage = "🟡 VÀNG - THEO DÕI SÁT"
else:
    triage = "🟢 XANH - KHÁM THƯỜNG"
base_fee = 500000
if patient_age < 6 or patient_age >= 80:
    fee = 0
elif has_insurance:
    fee = 250000
else:
    fee = base_fee

print("      PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print(f"Họ tên bệnh nhân : {patient_name}")
print(f"Tuổi             : {patient_age}")
print(f"SpO2             : {spo2_level}%")
print(f"Nhịp tim         : {heart_rate} bpm")
print(f"Phân luồng       : {triage}")
print(f"Viện phí tạm ứng : {fee:,} VNĐ")

print("\n========== SYSTEM LOG ==========")
print("patient_name   ->", type(patient_name))
print("patient_age    ->", type(patient_age))
print("spo2_level     ->", type(spo2_level))
print("heart_rate     ->", type(heart_rate))
print("has_insurance  ->", type(has_insurance))
print("fee            ->", type(fee))
print("triage         ->", type(triage))