from django.db import models


# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=9)
    Nama = models.TextField()
    Tanggallahir = models.TextField()
    Photo = models.TextField()
    Email = models.TextField()
    Fakultas = models.TextField()
    Prodi = models.TextField()
    Alamatrumah = models.TextField()
    Nilai = models.TextField()


    def str(self):
        return self.NIP

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=9)
    Nama = models.TextField()
    Tanggallahir = models.TextField()
    Tempatlahir = models.TextField()
    Photo = models.TextField()
    Email = models.TextField()
    Fakultas = models.TextField()
    Prodi = models.TextField()

    def str(self):
        return self.NIM

class pak(models.Model):
    Judul = models.CharField(max_length=50)
    Dosen_id = models.ForeignKey(Dosen, on_delete=models.CASCADE, null=True)
    Mahasiswa_id = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, null=True)
    
    def str(self):
        return self.Judul