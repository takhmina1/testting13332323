from django.urls import path
from .views import FiatTransferView, CryptoTransferView

urlpatterns = [
    path('transfer/fiat/', FiatTransferView.as_view(), name='transfer_fiat'),
    path('transfer/crypto/', CryptoTransferView.as_view(), name='transfer_crypto'),
]
