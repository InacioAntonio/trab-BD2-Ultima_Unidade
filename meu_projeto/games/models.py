from djongo import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.email

class Jogo(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuarios_favoritos = models.ManyToManyField(Usuario, related_name='jogos_favoritos')
    data_lancamento = models.DateField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        db_table = 'jogos'

    def __str__(self):
        return self.titulo