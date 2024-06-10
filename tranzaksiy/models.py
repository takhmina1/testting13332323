# from django.db import models
# from django.contrib.auth.models import User

# # Модель для банка
# class Bank(models.Model):
#     name = models.CharField(max_length=100)  # Название банка
#     country = models.CharField(max_length=100)  # Страна, где находится банк

#     def __str__(self):
#         return self.name

# # Модель для криптовалюты
# class CryptoCurrency(models.Model):
#     name = models.CharField(max_length=100)  # Название криптовалюты
#     code = models.CharField(max_length=10)  # Код криптовалюты (например, BTC, ETH)
#     network = models.CharField(max_length=50)  # Сеть криптовалюты (например, ERC20, TRC20)
#     deposit_status = models.BooleanField(default=True)  # Статус приема депозитов
#     receive_status = models.BooleanField(default=True)  # Статус получения средств
#     min_confirmations = models.IntegerField()  # Минимальное количество подтверждений для транзакции
#     max_confirmations = models.IntegerField()  # Максимальное количество подтверждений для транзакции
#     explorer_url = models.URLField()  # URL для отслеживания транзакций в блокчейне

#     def __str__(self):
#         return self.name

# # Модель для кошелька пользователя
# class Wallet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ссылка на пользователя
#     balance_fiat = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Баланс в фиатной валюте
#     balance_crypto = models.DecimalField(max_digits=12, decimal_places=8, default=0.00000000)  # Баланс в криптовалюте
#     currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE, null=True, blank=True)  # Валюта кошелька

#     def __str__(self):
#         return f"{self.user.username}'s Wallet"

# # Модель для транзакций
# class Transaction(models.Model):
#     TRANSACTION_METHODS = [  # Выбор метода транзакции
#         ('bank', 'Bank Transfer'),
#         ('crypto', 'Cryptocurrency'),
#     ]

#     from_wallet = models.ForeignKey(Wallet, related_name='outgoing_transactions', on_delete=models.CASCADE)  # Отправитель
#     to_wallet = models.ForeignKey(Wallet, related_name='incoming_transactions', on_delete=models.CASCADE)  # Получатель
#     amount = models.DecimalField(max_digits=12, decimal_places=2)  # Сумма транзакции
#     currency = models.CharField(max_length=10)  # Валюта транзакции
#     commission = models.DecimalField(max_digits=12, decimal_places=2)  # Комиссия
#     total_deducted = models.DecimalField(max_digits=12, decimal_places=2)  # Общая сумма списания
#     method = models.CharField(max_length=10, choices=TRANSACTION_METHODS)  # Метод транзакции
#     timestamp = models.DateTimeField(auto_now_add=True)  # Временная метка

#     def __str__(self):
#         return f"Transaction from {self.from_wallet} to {self.to_wallet} ({self.amount} {self.currency})"

#     def save(self, *args, **kwargs):
#         # Вычисление общей суммы списания
#         self.total_deducted = self.amount + self.commission
#         super().save(*args, **kwargs)  # Сохранение объекта






from django.db import models
from django.contrib.auth.models import User

# # Модель для банка
# class Bank(models.Model):
#     name = models.CharField(max_length=100)  # Название банка
#     country = models.CharField(max_length=100)  # Страна, где находится банк

#     def __str__(self):
#         return self.name

# Модель для банковских реквизитов
class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    # bank = models.ForeignKey(Bank, on_delete=models.CASCADE)  # Связь с банком
    account_number = models.CharField(max_length=20)  # Номер банковского счета
    account_holder_name = models.CharField(max_length=100)  # Имя владельца счета

    def __str__(self):
        return f"{self.account_holder_name} - {self.account_number}"

# Модель для криптовалюты
class CryptoCurrency(models.Model):
    name = models.CharField(max_length=100)  # Название криптовалюты
    code = models.CharField(max_length=10)  # Код криптовалюты (например, BTC, ETH)
    network = models.CharField(max_length=50)  # Сеть криптовалюты (например, ERC20, TRC20)
    deposit_status = models.BooleanField(default=True)  # Статус приема депозитов
    receive_status = models.BooleanField(default=True)  # Статус получения средств
    min_confirmations = models.IntegerField()  # Минимальное количество подтверждений для транзакции
    max_confirmations = models.IntegerField()  # Максимальное количество подтверждений для транзакции
    explorer_url = models.URLField(null=True, blank=True)  # URL для отслеживания транзакций в блокчейне

    def __str__(self):
        return f"{self.min_confirmations }-{self.max_confirmations}"

# Модель для криптовалютного кошелька
class CryptoWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь один-к-одному с пользователем
    balance = models.DecimalField(max_digits=12, decimal_places=8, default=0.00000000)  # Баланс в криптовалюте
    currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)  # Валюта кошелька

    def __str__(self):
        return f"{self.user.username}'s {self.currency.code} Wallet"

# Модель для фиатного кошелька
class FiatWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь один-к-одному с пользователем
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Баланс в фиатной валюте

    def __str__(self):
        return f"{self.user.username}'s Fiat Wallet"

# # Модель для транзакций
# class Transaction(models.Model):
#     TRANSACTION_METHODS = [  # Выбор метода транзакции
#         ('bank', 'Bank Transfer'),
#         ('crypto', 'Cryptocurrency'),
#     ]

#     from_wallet = models.ForeignKey('Wallet', related_name='outgoing_transactions', on_delete=models.CASCADE)  # Отправитель
#     to_wallet = models.ForeignKey('Wallet', related_name='incoming_transactions', on_delete=models.CASCADE)  # Получатель
#     amount = models.DecimalField(max_digits=12, decimal_places=2)  # Сумма транзакции
#     currency = models.CharField(max_length=10)  # Валюта транзакции
#     commission = models.DecimalField(max_digits=12, decimal_places=2)  # Комиссия
#     total_deducted = models.DecimalField(max_digits=12, decimal_places=2)  # Общая сумма списания
#     method = models.CharField(max_length=10, choices=TRANSACTION_METHODS)  # Метод транзакции
#     timestamp = models.DateTimeField(auto_now_add=True)  # Временная метка
#     bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True, blank=True)  # Банковский счёт (для фиатных транзакций)

#     def __str__(self):
#         return f"Transaction from {self.from_wallet} to {self.to_wallet} ({self.amount} {self.currency})"

#     def save(self, *args, **kwargs):
#         # Вычисление общей суммы списания
#         self.total_deducted = self.amount + self.commission
#         super().save(*args, **kwargs)  # Сохранение объекта



class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Баланс кошелька
    currency = models.CharField(max_length=10)  # Валюта кошелька (например, USD, BTC, ETH)
    kriptavallut = models.ForeignKey(CryptoWallet, on_delete=models.CASCADE)
    fiatnihvallut = models.ForeignKey(FiatWallet, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.user.username}'s Wallet ({self.balance} {self.currency})"




# Определение модели для транзакций
class Transaction(models.Model):
    # Методы транзакций
    TRANSACTION_METHODS = [
        ('bank', 'Bank Transfer'),  # Банковский перевод
        ('crypto', 'Cryptocurrency'),  # Криптовалюта
    ]

    # Отправитель транзакции
    from_wallet = models.ForeignKey(Wallet,related_name='outgoing_transactions', on_delete=models.CASCADE)
    # Получатель транзакции
    to_wallet = models.ForeignKey(Wallet,related_name='incoming_transactions', on_delete=models.CASCADE)
    # Сумма транзакции
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    # Валюта транзакции
    currency = models.CharField(max_length=10)
    # Комиссия
    commission = models.DecimalField(max_digits=12, decimal_places=2)
    # Общая сумма списания
    total_deducted = models.DecimalField(max_digits=12, decimal_places=2)
    # Метод транзакции
    method = models.CharField(max_length=10, choices=TRANSACTION_METHODS)
    # Временная метка
    timestamp = models.DateTimeField(auto_now_add=True)
    # Банковский счёт (для фиатных транзакций)
    bank_account = models.ForeignKey('BankAccount', on_delete=models.CASCADE, null=True, blank=True)

    # Строковое представление объекта
    def __str__(self):
        return f"Transaction from {self.from_wallet} to {self.to_wallet} ({self.amount} {self.currency})"

    # Метод сохранения объекта
    def save(self, *args, **kwargs):
        # Вычисление общей суммы списания
        self.total_deducted = self.amount + self.commission
        super().save(*args, **kwargs)  # Сохранение объекта


