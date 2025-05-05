import os
import django
from django.utils.text import slugify
from datetime import datetime
import random

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_blog_api.settings')
django.setup()

# Thay đổi import để phù hợp với Djongo
from food_api.models import MonAn, LoaiMonAn, VungMien  # Import cả LoaiMonAn và VungMien

# Dữ liệu mẫu tự định nghĩa (Ẩm thực Hàn Quốc)
ten_mon_an = [
    "Kimchi Jjigae", "Bibimbap", "Samgyeopsal", "Tteokbokki", "Jajangmyeon",
    "Bulgogi", "Haemul Pajeon", "Dak Galbi", "Samgyetang", "Hoe",
    "Gimbap", "Ramyeon", "Sundubu Jjigae", "Galbi", "Bossam",
    "Japchae", "Kimbap", "Tteokbokki", "Bibimbap", "Kimchi Fried Rice",
    "Haemul Pajeon", "Samgyeopsal", "Dak Galbi", "Bulgogi", "Jajangmyeon",
    "Sundubu Jjigae", "Galbi", "Bossam", "Japchae", "Samgyetang",
    "Hoe", "Gimbap", "Ramyeon", "Kimchi Jjigae", "Bingsu",
    "Hotteok", "Tteokbokki", "Odeng", "Kimbap", "Bibimbap"
]

ten_mon_an_en = [
    "Kimchi Stew", "Mixed Rice", "Grilled Pork Belly", "Spicy Rice Cakes", "Black Bean Noodles",
    "Marinated Beef BBQ", "Seafood Pancake", "Spicy Chicken Stir-fry", "Ginseng Chicken Soup", "Raw Fish",
    "Seaweed Rice Rolls", "Instant Noodles", "Soft Tofu Stew", "Beef Ribs BBQ", "Boiled Pork Wraps",
    "Stir-fried Glass Noodles", "Seaweed Rice Rolls", "Spicy Rice Cakes", "Mixed Rice", "Kimchi Fried Rice",
    "Seafood Pancake", "Grilled Pork Belly", "Spicy Chicken Stir-fry", "Marinated Beef BBQ", "Black Bean Noodles",
    "Soft Tofu Stew", "Beef Ribs BBQ", "Boiled Pork Wraps", "Stir-fried Glass Noodles", "Ginseng Chicken Soup",
    "Raw Fish", "Seaweed Rice Rolls", "Instant Noodles", "Kimchi Stew", "Shaved Ice Dessert",
    "Sweet Pancakes", "Spicy Rice Cakes", "Fish Cake Skewers", "Seaweed Rice Rolls", "Mixed Rice"
]

nguyen_lieu_mon_an = [
    ["Kimchi 200g", "Thịt heo 150g", "Đậu phụ 1 bìa", "Hành lá 2 nhánh", "Ớt bột 1 muỗng canh"],
    ["Cơm 2 bát", "Rau các loại 300g", "Thịt bò 100g", "Trứng 2 quả", "Gạo lứt 1/2 bát"],
    ["Thịt heo ba chỉ 500g", "Hành tây 1 củ", "Tỏi 3 tép", "Nấm 200g", "Kimchi 200g"],
    ["Bánh gạo 500g", "Chả cá 200g", "Hành tây 1 củ", "Ớt bột 2 muỗng canh", "Bắp cải 200g"],
    ["Mì tươi 200g", "Thịt heo 100g", "Hành tây 1 củ", "Đậu đen 100g", "Trứng 1 quả"],
    ["Thịt bò 500g", "Nước tương 50ml", "Đường 30g", "Tỏi 5 tép", "Hành tây 1 củ"],
    ["Hải sản 300g", "Bột mì 200g", "Hành lá 100g", "Ớt 2 quả", "Trứng 2 quả"],
    ["Gà 1 con", "Bắp cải 300g", "Hành tây 1 củ", "Ớt bột 2 muỗng canh", "Phô mai 100g"],
    ["Gà 1 con", "Gạo nếp 100g", "Nhân sâm 1 củ", "Táo tàu 5 quả", "Tỏi 5 tép"],
    ["Cá tươi 300g", "Rau sống 200g", "Nước chấm 100ml", "Ớt 2 quả", "Tỏi 3 tép"],
    ["Gạo 2 bát", "Rong biển 3 lá", "Rau củ 200g", "Trứng 2 quả", "Thịt 100g"],
    ["Mì gói 1 gói", "Gia vị vừa đủ", "Trứng 1 quả", "Hành lá 2 nhánh", "Ớt bột 1 muỗng canh"],
    ["Đậu phụ non 2 bìa", "Thịt heo 100g", "Kimchi 200g", "Hành tây 1 củ", "Ớt bột 1 muỗng canh"],
    ["Thịt bò 500g", "Nước tương 50ml", "Đường 30g", "Tỏi 5 tép", "Hành tây 1 củ"],
    ["Thịt heo luộc 300g", "Kimchi 200g", "Rau sống 200g", "Tỏi 3 tép", "Ớt 2 quả"],
    ["Miến dong 200g", "Rau củ 300g", "Thịt bò 100g", "Nấm 200g", "Trứng 2 quả"],
    ["Gạo 2 bát", "Rong biển 3 lá", "Rau củ 200g", "Trứng 2 quả", "Thịt 100g"],
    ["Bánh gạo 500g", "Chả cá 200g", "Hành tây 1 củ", "Ớt bột 2 muỗng canh", "Bắp cải 200g"],
    ["Cơm 2 bát", "Rau các loại 300g", "Thịt bò 100g", "Trứng 2 quả", "Gạo lứt 1/2 bát"],
    ["Kimchi 200g", "Cơm 2 bát", "Thịt heo 150g", "Trứng 2 quả", "Rau củ 200g"],
    ["Hải sản 300g", "Bột mì 200g", "Hành lá 100g", "Ớt 2 quả", "Trứng 2 quả"],
    ["Thịt heo ba chỉ 500g", "Hành tây 1 củ", "Tỏi 3 tép", "Nấm 200g", "Kimchi 200g"],
    ["Gà 1 con", "Bắp cải 300g", "Hành tây 1 củ", "Ớt bột 2 muỗng canh", "Phô mai 100g"],
    ["Thịt bò 500g", "Nước tương 50ml", "Đường 30g", "Tỏi 5 tép", "Hành tây 1 củ"],
    ["Mì tươi 200g", "Thịt heo 100g", "Hành tây 1 củ", "Đậu đen 100g", "Trứng 1 quả"],
    ["Đậu phụ non 2 bìa", "Thịt heo 100g", "Kimchi 200g", "Hành tây 1 củ", "Ớt bột 1 muỗng canh"],
    ["Thịt bò 500g", "Nước tương 50ml", "Đường 30g", "Tỏi 5 tép", "Hành tây 1 củ"],
    ["Thịt heo luộc 300g", "Kimchi 200g", "Rau sống 200g", "Tỏi 3 tép", "Ớt 2 quả"],
    ["Miến dong 200g", "Rau củ 300g", "Thịt bò 100g", "Nấm 200g", "Trứng 2 quả"],
    ["Gà 1 con", "Gạo nếp 100g", "Nhân sâm 1 củ", "Táo tàu 5 quả", "Tỏi 5 tép"],
    ["Cá tươi 300g", "Rau sống 200g", "Nước chấm 100ml", "Ớt 2 quả", "Tỏi 3 tép"],
    ["Gạo 2 bát", "Rong biển 3 lá", "Rau củ 200g", "Trứng 2 quả", "Thịt 100g"],
    ["Mì gói 1 gói", "Gia vị vừa đủ", "Trứng 1 quả", "Hành lá 2 nhánh", "Ớt bột 1 muỗng canh"],
    ["Kimchi 200g", "Thịt heo 150g", "Đậu phụ 1 bìa", "Hành lá 2 nhánh", "Ớt bột 1 muỗng canh"],
    ["Đá bào 500g", "Sữa đặc 100ml", "Hoa quả tươi 300g", "Bánh gạo 100g", "Kem 100g"],
    ["Bột mì 200g", "Đường 50g", "Mật ong 50ml", "Quế 1 thanh", "Đậu phộng 50g"],
    ["Bánh gạo 500g", "Chả cá 200g", "Hành tây 1 củ", "Ớt bột 2 muỗng canh", "Bắp cải 200g"],
    ["Chả cá 300g", "Nước dùng 1 lít", "Hành lá 50g", "Ớt bột 1 muỗng canh"],
    ["Gạo 2 bát", "Rong biển 3 lá", "Rau củ 200g", "Trứng 2 quả", "Thịt 100g"],
    ["Cơm 2 bát", "Rau các loại 300g", "Thịt bò 100g", "Trứng 2 quả", "Gạo lứt 1/2 bát"]
]

cach_lam_mon_an = [
    ["1. Cho kimchi, thịt heo và đậu phụ vào nồi", "2. Thêm nước dùng và đun sôi", "3. Nêm gia vị và thưởng thức."],
    ["1. Trộn cơm với rau và thịt", "2. Thêm trứng và tương ớt", "3. Trộn đều và thưởng thức."],
    ["1. Nướng thịt trên bàn nướng", "2. Ăn kèm với rau sống và nước chấm.", "3. Thưởng thức khi thịt chín."],
    ["1. Luộc bánh gạo", "2. Xào với chả cá và hành tây", "3. Thêm ớt bột và thưởng thức."],
    ["1. Luộc mì", "2. Xào thịt và hành tây với đậu đen", "3. Trộn đều và thưởng thức."],
    ["1. Ướp thịt bò", "2. Nướng thịt trên vỉ", "3. Cắt miếng vừa ăn và thưởng thức."],
    ["1. Trộn bột", "2. Chiên bánh với hải sản và hành lá", "3. Ăn kèm nước chấm."],
    ["1. Xào gà với bắp cải và hành tây", "2. Thêm ớt bột và phô mai", "3. Thưởng thức khi chín."],
    ["1. Nấu gà với gạo nếp và nhân sâm", "2. Hầm đến khi mềm", "3. Thưởng thức nóng."],
    ["1. Chuẩn bị cá sống", "2. Ăn kèm rau sống và nước chấm", "3. Thưởng thức tươi ngon."],
    ["1. Trải rong biển lên mành tre", "2. Cho cơm và các nguyên liệu vào", "3. Cuộn tròn và cắt miếng vừa ăn."],
    ["1. Luộc mì", "2. Cho gia vị vào", "3. Thêm trứng và hành lá", "4. Thưởng thức nóng."],
    ["1. Cho đậu phụ, thịt heo và kimchi vào nồi", "2. Thêm nước dùng và đun sôi", "3. Nêm gia vị và thưởng thức."],
    ["1. Ướp thịt bò", "2. Nướng trên vỉ", "3. Cắt miếng vừa ăn và thưởng thức."],
    ["1. Luộc thịt heo", "2. Ăn kèm kimchi, rau sống và tỏi", "3. Cuốn và thưởng thức."],
    ["1. Luộc miến", "2. Xào với rau củ và thịt bò", "3. Trộn đều và thưởng thức."],
    ["1. Trải rong biển lên mành tre", "2. Cho cơm và các nguyên liệu vào", "3. Cuộn tròn và cắt miếng vừa ăn."],
    ["1. Luộc bánh gạo", "2. Xào với chả cá và hành tây", "3. Thêm ớt bột và thưởng thức."],
    ["1. Trộn cơm với rau và thịt", "2. Thêm trứng và tương ớt", "3. Trộn đều và thưởng thức."],
    ["1. Xào cơm với kimchi và thịt heo", "2. Thêm trứng và rau củ", "3. Trộn đều và thưởng thức."],
    ["1. Trộn bột", "2. Chiên bánh với hải sản và hành lá", "3. Ăn kèm nước chấm."],
    ["1. Nướng thịt trên bàn nướng", "2. Ăn kèm với rau sống và nước chấm.", "3. Thưởng thức khi thịt chín."],
    ["1. Xào gà với bắp cải và hành tây", "2. Thêm ớt bột và phô mai", "3. Thưởng thức khi chín."],
    ["1. Ướp thịt bò", "2. Nướng thịt trên vỉ", "3. Cắt miếng vừa ăn và thưởng thức."],
    ["1. Luộc mì", "2. Xào thịt và hành tây với đậu đen", "3. Trộn đều và thưởng thức."],
    ["1. Cho đậu phụ, thịt heo và kimchi vào nồi", "2. Thêm nước dùng và đun sôi", "3. Nêm gia vị và thưởng thức."],
    ["1. Ướp thịt bò", "2. Nướng trên vỉ", "3. Cắt miếng vừa ăn và thưởng thức."],
    ["1. Luộc thịt heo", "2. Ăn kèm kimchi, rau sống và tỏi", "3. Cuốn và thưởng thức."],
    ["1. Luộc miến", "2. Xào với rau củ và thịt bò", "3. Trộn đều và thưởng thức."],
    ["1. Nấu gà với gạo nếp và nhân sâm", "2. Hầm đến khi mềm", "3. Thưởng thức nóng."],
    ["1. Chuẩn bị cá sống", "2. Ăn kèm rau sống và nước chấm", "3. Thưởng thức tươi ngon."],
    ["1. Trải rong biển lên mành tre", "2. Cho cơm và các nguyên liệu vào", "3. Cuộn tròn và cắt miếng vừa ăn."],
    ["1. Luộc mì", "2. Cho gia vị vào", "3. Thêm trứng và hành lá", "4. Thưởng thức nóng."],
    ["1. Cho kimchi, thịt heo và đậu phụ vào nồi", "2. Thêm nước dùng và đun sôi", "3. Nêm gia vị và thưởng thức."],
    ["1. Chuẩn bị đá bào", "2. Cho sữa đặc và hoa quả lên trên", "3. Thêm bánh gạo và kem", "4. Thưởng thức lạnh."],
    ["1. Trộn bột", "2. Chiên bánh", "3. Rắc đường và mật ong", "4. Thêm quế và đậu phộng", "5. Thưởng thức nóng."],
    ["1. Luộc bánh gạo", "2. Xào với chả cá và hành tây", "3. Thêm ớt bột", "4. Thưởng thức cay nồng."],
    ["1. Xiên chả cá vào que", "2. Nhúng vào nước dùng", "3. Thưởng thức nóng."],
    ["1. Trải rong biển lên mành tre", "2. Cho cơm và các nguyên liệu vào", "3. Cuộn tròn và cắt miếng vừa ăn."],
    ["1. Trộn cơm với rau và thịt", "2. Thêm trứng và tương ớt", "3. Trộn đều và thưởng thức."]
]
tags_mon_an = [
    ["cay", "hầm"],
    ["trộn", "rau"],
    ["nướng", "thịt"],
    ["bánh gạo", "cay"],
    ["mì", "đậu đen"],
    ["nướng", "bò"],
    ["bánh", "hải sản"],
    ["gà", "cay"],
    ["gà", "súp"],
    ["sống", "hải sản"],
    ["cơm", "rong biển"],
    ["mì", "nóng"],
    ["đậu phụ", "hầm"],
    ["bò", "nướng"],
    ["thịt heo", "cuốn"],
    ["miến", "xào"],
    ["cơm", "rong biển"],
    ["bánh gạo", "cay"],
    ["trộn", "rau"],
    ["cơm", "kimchi"],
    ["bánh", "hải sản"],
    ["nướng", "thịt"],
    ["gà", "cay"],
    ["nướng", "bò"],
    ["mì", "đậu đen"],
    ["đậu phụ", "hầm"],
    ["bò", "nướng"],
    ["thịt heo", "cuốn"],
    ["miến", "xào"],
    ["gà", "súp"],
    ["sống", "hải sản"],
    ["cơm", "rong biển"],
    ["mì", "nóng"],
    ["cay", "hầm"],
    ["đá", "ngọt"],
    ["bánh", "ngọt"],
    ["bánh gạo", "cay"],
    ["chả cá", "nóng"],
    ["cơm", "rong biển"],
    ["trộn", "rau"]
]

mo_ta_loai_mon_an = [
    "Các món ăn khai vị kích thích vị giác, thường có hương vị nhẹ nhàng và tươi mát.",
    "Các món ăn chính cung cấp nguồn dinh dưỡng và năng lượng chính cho bữa ăn.",
    "Các món canh và lẩu không chỉ làm ấm bụng mà còn cung cấp nhiều dưỡng chất từ rau củ và thịt/hải sản.",
    "Các món nướng mang đến hương vị đậm đà, hấp dẫn, thường được ăn kèm với các loại panchan.",
    "Các món ăn đường phố đa dạng, tiện lợi, mang đậm bản sắc văn hóa ẩm thực địa phương."
]

mo_ta_ngan_mon_an = [
    "Món canh kim chi cay nồng, đậm đà, ăn kèm với đậu phụ và thịt heo.",
    "Cơm trộn rau và thịt bò, trứng lòng đào, tương ớt đặc trưng.",
    "Thịt ba chỉ nướng thơm lừng, ăn kèm rau sống và kim chi.",
    "Bánh gạo cay dẻo dai, chả cá, sốt ớt ngọt cay hấp dẫn.",
    "Mì tương đen đậm đà, thịt heo và rau củ.",
    "Thịt bò ướp nướng thơm mềm, đậm đà gia vị.",
    "Bánh xèo hải sản giòn rụm, thơm ngon.",
    "Gà xào cay phô mai hấp dẫn, đậm đà hương vị.",
    "Gà hầm sâm bổ dưỡng, thơm ngon.",
    "Gỏi cá tươi sống, ăn kèm rau sống và nước chấm đặc biệt.",
    "Cơm cuộn rong biển với rau củ, trứng và thịt.",
    "Mì gói cay nồng, ăn kèm trứng và hành lá.",
    "Canh đậu hũ non cay nóng, thơm ngon.",
    "Sườn bò nướng thơm lừng, đậm đà gia vị.",
    "Thịt ba chỉ luộc cuốn rau sống, kim chi.",
    "Miến trộn rau củ và thịt bò, thơm ngon.",
    "Cơm cuộn rong biển với rau củ, trứng và thịt.",
    "Bánh gạo cay dẻo dai, chả cá, sốt ớt ngọt cay hấp dẫn.",
    "Cơm trộn rau và thịt bò, trứng lòng đào, tương ớt đặc trưng.",
    "Cơm rang kim chi đậm đà, thơm ngon.",
    "Bánh xèo hải sản giòn rụm, thơm ngon.",
    "Thịt ba chỉ nướng thơm lừng, ăn kèm rau sống và kim chi.",
    "Gà xào cay phô mai hấp dẫn, đậm đà hương vị.",
    "Thịt bò ướp nướng thơm mềm, đậm đà gia vị.",
    "Mì tương đen đậm đà, thịt heo và rau củ.",
    "Canh đậu hũ non cay nóng, thơm ngon.",
    "Sườn bò nướng thơm lừng, đậm đà gia vị.",
    "Thịt ba chỉ luộc cuốn rau sống, kim chi.",
    "Miến trộn rau củ và thịt bò, thơm ngon.",
    "Gà hầm sâm bổ dưỡng, thơm ngon.",
    "Gỏi cá tươi sống, ăn kèm rau sống và nước chấm đặc biệt.",
    "Cơm cuộn rong biển với rau củ, trứng và thịt.",
    "Mì gói cay nồng, ăn kèm trứng và hành lá.",
    "Món canh kim chi cay nồng, đậm đà, ăn kèm với đậu phụ và thịt heo.",
    "Món tráng miệng đá bào mát lạnh với sữa đặc, hoa quả và kem.",
    "Bánh rán ngọt nhân đường và mật ong, thơm ngon.",
    "Bánh gạo cay dẻo dai, chả cá, sốt ớt ngọt cay hấp dẫn.",
    "Chả cá xiên que nóng hổi, ăn kèm nước dùng đậm đà.",
    "Cơm cuộn rong biển với rau củ, trứng và thịt.",
    "Cơm trộn rau và thịt bò, trứng lòng đào, tương ớt đặc trưng."
]


def populate_database(num_mon_an=40):
    """
    Tạo dữ liệu mẫu cho các models và lưu vào database.
    Args:
        num_mon_an (int, optional): Số lượng món ăn cần tạo. Mặc định là 40.
    """
    try:
        print("Bắt đầu tạo dữ liệu mẫu ẩm thực Hàn Quốc...")

        # Lấy danh sách loại món ăn và vùng miền từ database
        loai_mon_ans = list(LoaiMonAn.objects.all())
        vung_miens = list(VungMien.objects.all())

        if not loai_mon_ans or not vung_miens:
            print("Cần có dữ liệu LoaiMonAn và VungMien trong database trước khi tạo MonAn.")
            print("Hãy chạy populate_database() với số lượng loại và vùng lớn hơn 0 trước.")
            return

        for i in range(num_mon_an):
            mon_an_name = ten_mon_an[i]
            mon_an_name_en = ten_mon_an_en[i]
            # Chọn ngẫu nhiên một loại món ăn và vùng miền từ danh sách đã lấy
            # loai_mon_an_obj = random.choice(loai_mon_ans)
            # vung_mien_obj = random.choice(vung_miens) if random.random() < 0.8 else None #80% món ăn có vùng miền
            loai_mon_an_obj = None
            vung_mien_obj = None
            mo_ta_ngan = mo_ta_ngan_mon_an[i]
            nguyen_lieu = nguyen_lieu_mon_an[i]
            cach_lam = cach_lam_mon_an[i]
            hinh_anh = "https://example.com/korean_food_" + str(i+1) + ".jpg"
            tags = tags_mon_an[i]
            luot_xem = random.randint(0, 1000)
            ngay_tao = datetime(2025, 5, 10, 12, 0, 0)
            ngay_cap_nhat = datetime(2025, 5, 10, 12, 0, 0)
            slug_mon_an = slugify(mon_an_name)

            MonAn.objects.create(
                ten_mon_an=mon_an_name,
                ten_mon_an_en=mon_an_name_en,
                loai=loai_mon_an_obj,
                vung_mien=vung_mien_obj,
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
            print(f"[{i+1}/{num_mon_an}] Đã tạo MonAn: {mon_an_name}")

        print("Đã tạo xong dữ liệu mẫu ẩm thực Hàn Quốc!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        print("Quá trình tạo dữ liệu mẫu bị dừng lại.")

if __name__ == "__main__":
    populate_database()
