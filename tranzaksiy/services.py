from django.db import transaction
from django.core.exceptions import ValidationError
from decimal import Decimal
from .models import FiatWallet, CryptoWallet, BankAccount, CryptoCurrency, Transaction

class WalletService:

    @staticmethod
    def transfer_fiat(from_wallet, to_wallet, amount, bank_account_id, commission_rate=Decimal('0.02')):
        """
        Перевод фиатных средств из одного кошелька в другой с использованием банковских реквизитов.
        """
        if from_wallet == to_wallet:
            raise ValidationError("Нельзя перевести средства на тот же кошелек.")
        if amount <= 0:
            raise ValidationError("Сумма должна быть больше нуля.")

        commission = amount * commission_rate
        total_deducted = amount + commission
        bank_account = BankAccount.objects.get(id=bank_account_id)

        with transaction.atomic():
            if from_wallet.balance < total_deducted:
                raise ValidationError("Недостаточно фиатных средств.")
            from_wallet.balance -= total_deducted
            to_wallet.balance += amount

            from_wallet.save()
            to_wallet.save()

            transaction_record = Transaction(
                from_wallet=from_wallet,
                to_wallet=to_wallet,
                amount=amount,
                currency='fiat',
                commission=commission,
                total_deducted=total_deducted,
                method='bank',
                bank_account=bank_account
            )
            transaction_record.save()

        return transaction_record

    @staticmethod
    def transfer_crypto(from_wallet, to_wallet, amount, currency_code, commission_rate=Decimal('0.02')):
        """
        Перевод криптовалютных средств из одного кошелька в другой.
        """
        if from_wallet == to_wallet:
            raise ValidationError("Нельзя перевести средства на тот же кошелек.")
        if amount <= 0:
            raise ValidationError("Сумма должна быть больше нуля.")
        
        currency = CryptoCurrency.objects.get(code=currency_code)
        if from_wallet.currency != currency or to_wallet.currency != currency:
            raise ValidationError("Несоответствие валюты в кошельках для криптовалютной транзакции.")
        
        commission = amount * commission_rate
        total_deducted = amount + commission

        with transaction.atomic():
            if from_wallet.balance < total_deducted:
                raise ValidationError("Недостаточно средств в криптовалюте.")
            from_wallet.balance -= total_deducted
            to_wallet.balance += amount

            from_wallet.save()
            to_wallet.save()

            transaction_record = Transaction(
                from_wallet=from_wallet,
                to_wallet=to_wallet,
                amount=amount,
                currency=currency_code,
                commission=commission,
                total_deducted=total_deducted,
                method='crypto',
            )
            transaction_record.save()

        return transaction_record




# class Transaction:

#     def tranzaksiy(self, otravitel, poluchatel, commisiy, sum1 , sumpol, fiatkoshel, kriptavalut):
#         tran = otravitel=otravitel 
#         poluchatel=poluchatel
#         if otravitel == sum1


class Transaction:
    
  
    def transactions(self, sender, receiver, commission, amount, receiver_amount, fiat_wallet, crypto_currency):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "commission": commission,
            "amount": amount,
            "receiver_amount": receiver_amount,
            "fiat_wallet": fiat_wallet,
            "crypto_currency": crypto_currency
        }
        return transaction

