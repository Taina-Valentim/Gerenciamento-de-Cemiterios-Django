from django.db import models
from django.db.models.deletion import CASCADE

class Jazigo(models.Model):
    local = models.CharField(max_length=100, verbose_name="Local")
    tamanho = models.IntegerField(verbose_name="Tamanho")
    qtdSepulturas = models.IntegerField(verbose_name="Quantidade de Sepulturas")
    sepOcupadas = models.IntegerField(blank=True, null=True, verbose_name="Sepulturas Ocupadas")
    nomeFamilia = models.CharField(max_length=100, verbose_name="Nome da Família")
    def __str__(self):
        return f'{self.nomeFamilia} - {self.local}'
    class Meta:
        verbose_name_plural = 'Jazigos'

class Obito(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    dataObito = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name="Data do Óbito")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    cartorio = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cartório")
    livro = models.IntegerField(verbose_name="Livro")
    folha = models.IntegerField(verbose_name="Folha")
    termo = models.IntegerField(verbose_name="Termo")
    medico = models.CharField(max_length=100, blank=True, null=True, verbose_name="Médico")
    crm = models.CharField(max_length=100, blank=True, null=True, verbose_name="CRM")
    id_jazigo = models.ForeignKey(Jazigo, on_delete=models.CASCADE, verbose_name='Nome da Família')
    def __str__(self):
        return f'{self.nome} ({self.cpf}) - {self.dataObito}'
    class Meta:
        verbose_name_plural = 'Obitos'

class Sepultamento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    dataSepultamento = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name="Data do Sepultamento")
    funeraria = models.CharField(max_length=100, blank=True, null=True, verbose_name="Funerária")
    responsavel = models.CharField(max_length=100, verbose_name="Responsável")
    local = models.CharField(max_length=100, verbose_name="Local")
    id_obito = models.ForeignKey(Obito, on_delete=models.CASCADE, verbose_name='Falecido')
    id_jazigo = models.ForeignKey(Jazigo, on_delete=models.CASCADE, verbose_name='Jazigo da Família')
    def __str__(self):
        return f'{self.nome} ({self.dataSepultamento} - {self.horarioEnterro})'
    class Meta:
        verbose_name_plural = 'Sepultamentos'

