from django.db import models


# Create your models here.
class Autorizacao(models.Model):
    categoria = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    emissao = models.DateField
    validade = models.IntegerField
    proc_ADM = models.CharField(max_length=50)
    tcaNum = models.CharField(max_length=50)
    compromitente = models.CharField(max_length=100)
    cpfcnpj = models.CharField(max_length=50)
    insc_CAD = models.CharField(max_length=5)
    endereco = models.CharField(max_length=100)
    quadra = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    area_lote = models.IntegerField
    sup_aut = models.IntegerField
    matricula = models.CharField(max_length=5)
    anuencia_CETESB = models.CharField(max_length=20)
    anuencia_CONDEMA = models.CharField(max_length=20)
    compensacao_averbacao = models.IntegerField
    observacao = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    nativos = models.IntegerField
    exoticos = models.IntegerField
    euterpe = models.IntegerField
    transplante = models.CharField(max_length=50)
    vegetacao = models.CharField(max_length=50)
    estagio = models.CharField(max_length=50)
    area_aut = models.IntegerField
    recup_PRAD = models.IntegerField
    app1 = models.CharField(max_length=20)
    app2 = models.CharField(max_length=20)
    reserva = models.CharField(max_length=20)
    restricao = models.CharField(max_length=50)
    area_rest = models.IntegerField
       
    def __str__(self) -> str:
        return self.numero