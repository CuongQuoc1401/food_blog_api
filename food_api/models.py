from djongo import models

class LoaiMonAn(models.Model):
    ten_loai = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    mo_ta = models.TextField(blank=True, null=True)
    hinh_anh_dai_dien = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ten_loai

    class Meta:
        db_table = 'loai_mon_an'  # Tên collection trong MongoDB

class VungMien(models.Model):
    ten_vung = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    mo_ta = models.TextField(blank=True, null=True)
    ban_do = models.JSONField(blank=True, null=True) # Ví dụ: {"lat": 37.5665, "lng": 126.9780}
    hinh_anh_dai_dien = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ten_vung

    class Meta:
        db_table = 'vung_mien'  # Tên collection trong MongoDB

class MonAn(models.Model):
    ten_mon_an = models.CharField(max_length=255)
    ten_mon_an_en = models.CharField(max_length=255, blank=True, null=True)
    loai = models.ForeignKey(LoaiMonAn, on_delete=models.SET_NULL, null=True, related_name='mon_ans')
    vung_mien = models.ForeignKey(VungMien, on_delete=models.SET_NULL, null=True, blank=True, related_name='mon_ans')
    mo_ta_ngan = models.TextField(blank=True, null=True)
    nguyen_lieu = models.JSONField()
    cach_lam = models.JSONField()
    hinh_anh = models.CharField(max_length=255, blank=True, null=True)
    tags = models.JSONField(blank=True, null=True) # Ví dụ: ["thit", "cay"]
    luot_xem = models.IntegerField(default=0)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_cap_nhat = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.ten_mon_an

    class Meta:
        db_table = 'mon_an'  # Tên collection trong MongoDB