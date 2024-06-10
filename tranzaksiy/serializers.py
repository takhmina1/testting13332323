# from rest_framework import serializers
# from .models import Bank, CryptoCurrency, Transaction

# # Сериализатор для модели Bank
# class BankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bank
#         fields = '__all__'

# # Сериализатор для модели CryptoCurrency
# class CryptoCurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CryptoCurrency
#         fields = '__all__'

# # Сериализатор для модели Transaction
# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'






from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FiatWallet, CryptoWallet, BankAccount, CryptoCurrency, Transaction
from .services import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'



# Сериализатор для пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# # Сериализатор для банка
# class BankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bank
#         fields = ['id', 'name', 'country']

# Сериализатор для банковского счёта
class BankAccountSerializer(serializers.ModelSerializer):
    # bank = BankSerializer(read_only=True)
    
    class Meta:
        model = BankAccount
        fields = ['id', 'user', 'bank', 'account_number', 'account_holder_name']

# Сериализатор для криптовалюты
class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = ['id', 'name', 'code', 'network', 'deposit_status', 'receive_status', 'min_confirmations', 'max_confirmations', 'explorer_url']

# Сериализатор для фиатного кошелька
class FiatWalletSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = FiatWallet
        fields = ['id', 'user', 'balance']

# Сериализатор для криптовалютного кошелька
class CryptoWalletSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    currency = CryptoCurrencySerializer(read_only=True)
    
    class Meta:
        model = CryptoWallet
        fields = ['id', 'user', 'balance', 'currency']

# Сериализатор для транзакции
class TransactionSerializer(serializers.ModelSerializer):
    from_wallet = serializers.StringRelatedField()
    to_wallet = serializers.StringRelatedField()
    bank_account = BankAccountSerializer(read_only=True)
    
    class Meta:
        model = Transaction
        fields = ['id', 'from_wallet', 'to_wallet', 'amount', 'currency', 'commission', 'total_deducted', 'method', 'timestamp', 'bank_account']

# Сериализатор для перевода фиатных средств
class FiatTransferSerializer(serializers.Serializer):
    to_wallet_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    bank_account_id = serializers.IntegerField()
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Сумма должна быть больше нуля.")
        return value

# Сериализатор для перевода криптовалютных средств
class CryptoTransferSerializer(serializers.Serializer):
    to_wallet_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=8)
    currency_code = serializers.CharField(max_length=10)
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Сумма должна быть больше нуля.")
        return value
