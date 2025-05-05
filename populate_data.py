import os
import django
from faker import Faker
from django.utils.text import slugify
from datetime import datetime
import random
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_blog_api.settings')
django.setup()

from food_api.models import LoaiMonAn, VungMien, MonAn

fake = Faker('vi_VN') # Sử dụng locale 'vi_VN' để tạo dữ liệu tiếng Việt (nếu cần)

def populate_database(num_loai=5, num_vung=5, num_mon_an=100):
    """Tạo dữ liệu mẫu cho các models và lưu vào database."""

    loai_mon_ans = []
    for _ in range(num_loai):
        ten_loai = fake.unique.word().capitalize() + " " + fake.unique.word().capitalize()
        slug_loai = slugify(ten_loai)
        mo_ta_loai = fake.paragraph(nb_sentences=3)
        hinh_anh_dai_dien_loai = fake.image_url()
        loai = LoaiMonAn.objects.create(
            ten_loai=ten_loai,
            slug=slug_loai,
            mo_ta=mo_ta_loai,
            hinh_anh_dai_dien=hinh_anh_dai_dien_loai
        )
        loai_mon_ans.append(loai)
        print(f"Đã tạo LoaiMonAn: {ten_loai}")

    vung_miens = []
    for _ in range(num_vung):
        ten_vung = fake.unique.city()
        slug_vung = slugify(ten_vung)
        mo_ta_vung = fake.paragraph(nb_sentences=4)
        ban_do_vung = {"lat": fake.latitude(), "lng": fake.longitude()}
        hinh_anh_dai_dien_vung = fake.image_url()
        vung = VungMien.objects.create(
            ten_vung=ten_vung,
            slug=slug_vung,
            mo_ta=mo_ta_vung,
            ban_do=ban_do_vung,
            hinh_anh_dai_dien=hinh_anh_dai_dien_vung
        )
        vung_miens.append(vung)
        print(f"Đã tạo VungMien: {ten_vung}")

    for _ in range(num_mon_an):
        ten_mon_an = fake.unique.sentence(nb_words=4).capitalize()[:-1]
        ten_mon_an_en = fake.unique.sentence(nb_words=5).capitalize()[:-1]
        loai = random.choice(loai_mon_ans)
        vung = random.choice(vung_miens) if random.random() < 0.8 else None # Không phải món ăn nào cũng có vùng miền
        mo_ta_ngan = fake.paragraph(nb_sentences=2)
        nguyen_lieu = [fake.word().capitalize() for _ in range(random.randint(3, 7))]
        cach_lam = [fake.paragraph(nb_sentences=random.randint(1, 3)) for _ in range(random.randint(2, 5))]
        hinh_anh = fake.image_url()
        tags = [fake.word() for _ in range(random.randint(0, 3))]
        luot_xem = random.randint(0, 1000)
        ngay_tao = fake.past_datetime()
        ngay_cap_nhat = fake.past_datetime()
        slug_mon_an = slugify(ten_mon_an)

        MonAn.objects.create(
            ten_mon_an=ten_mon_an,
            ten_mon_an_en=ten_mon_an_en,
            loai=loai,
            vung_mien=vung,
            mo_ta_ngan=mo_ta_ngan,
            nguyen_lieu=nguyen_lieu,
            cach_lam=cach_lam,
            hinh_anh=hinh_anh,
            tags=tags,
            luot_xem=luot_xem,
            ngay_tao=ngay_tao,
            ngay_cap_nhat=ngay_cap_nhat,
            slug=slug_mon_an
        )
        print(f"Đã tạo MonAn: {ten_mon_an}")

    print("Đã tạo xong dữ liệu mẫu!")

if __name__ == "__main__":
    populate_database() # Gọi hàm để tạo dữ liệu (mặc định 5 loại, 5 vùng, 100 món ăn)
    # Hoặc bạn có thể chỉ định số lượng:
    # populate_database(num_loai=10, num_vung=8, num_mon_an=150)