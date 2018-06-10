from django.db import models
from django.utils import timezone

class Especialidade(models.Model):
        nome = models.CharField(max_length=30,primary_key = True)
        salario = models.FloatField(blank=False, null=False)
        descricao = models.TextField(blank=True, null=True)
        
        def __str__(self):
            return self.nome

class Medico(models.Model):
    especialidade = models.ManyToManyField('Especialidade')
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    data_de_nascimento = models.DateField(blank=False, null=False)
    cidade = models.CharField(max_length=30, blank=False, null=False)
    estado = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapa'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceara'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goias'),
        ('MA', 'Maranhao'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Para'),
        ('PB', 'Paraiba'),
        ('PR', 'Parana'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piaui'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondonia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'Sao Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField(max_length=2, choices=estado, blank=False, null=False)

    cep = models.CharField(max_length=8, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    crm = models.CharField(max_length=6, blank=False, null=False, primary_key = True)
    uf = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PR', 'PR'),
        ('PE', 'PE'),
        ('PI', 'PI'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('SC', 'SC'),
        ('SP', 'SP'),
        ('SE', 'SE'),
        ('TO', 'TO'),
    )

    uf = models.CharField(max_length=2, choices=uf, blank=False, null=False)

    sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=sexo, blank=False, null=False)

    def __str__(self):
            return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, blank=False, null=False, primary_key = True)
    data_de_nascimento = models.DateField(blank=False, null=False)
    cidade = models.CharField(max_length=30, blank=False, null=False)
    estado = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapa'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceara'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goias'),
        ('MA', 'Maranhao'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Para'),
        ('PB', 'Paraiba'),
        ('PR', 'Parana'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piaui'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondonia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'Sao Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField(max_length=2, choices=estado, blank=False, null=False)

    cep = models.CharField(max_length=8, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)

    sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=sexo, blank=False, null=False)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey('Paciente')
    medico = models.ManyToManyField('Medico')
    codigo_da_consulta = models.CharField(max_length=300, blank=False, null=False, primary_key = True)
    data_da_consulta = models.DateTimeField(blank=False, null=False)
    plano_de_saude = (
        ('N', 'Nao'),
        ('S', 'Sim'),
    )
    plano_de_saude = models.CharField(max_length=1, choices=plano_de_saude, blank=False, null=False)

    def __str__(self):
        return self.codigo_da_consulta
