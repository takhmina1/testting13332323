from django.contrib import admin
from .models import BankAccount, CryptoCurrency, CryptoWallet, FiatWallet, Wallet, Transaction

# Регистрация модели BankAccount
@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'account_holder_name')
    search_fields = ('user__username', 'account_number', 'account_holder_name')

# Регистрация модели CryptoCurrency
@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'network', 'deposit_status', 'receive_status')
    search_fields = ('name', 'code', 'network')
    list_filter = ('deposit_status', 'receive_status')

# Регистрация модели CryptoWallet
@admin.register(CryptoWallet)
class CryptoWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency', 'balance')
    search_fields = ('user__username', 'currency__code')

# Регистрация модели FiatWallet
@admin.register(FiatWallet)
class FiatWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username',)

# Регистрация модели Wallet
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'currency')
    search_fields = ('user__username', 'currency')

# Регистрация модели Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('from_wallet', 'to_wallet', 'amount', 'currency', 'method', 'timestamp')
    search_fields = ('from_wallet__user__username', 'to_wallet__user__username', 'currency', 'method')
    list_filter = ('method', 'timestamp')

