import os

from util.conversions import BananoConversions, NanoConversions
from util.number import NumberUtil

class Env():
    @staticmethod
    def banano() -> bool:
        return True

    @staticmethod
    def raw_to_amount(raw_amt: int, truncate: bool = True) -> float:
        converted = BananoConversions.raw_to_banano(raw_amt) if Env.banano() else NanoConversions.raw_to_nano(raw_amt)
        return NumberUtil.truncate_digits(converted, max_digits=Env.precision_digits()) if truncate else converted

    @staticmethod
    def amount_to_raw(amount: float) -> int:
        return BananoConversions.banano_to_raw(amount) if Env.banano() else NanoConversions.nano_to_raw(amount)

    @staticmethod
    def currency_name() -> str:
        return 'PARTYcoin' if Env.banano() else 'Nano'

    @staticmethod
    def currency_symbol() -> str:
        return 'PRTC' if Env.banano() else 'NANO'

    @staticmethod
    def precision_digits() -> int:
        return 2 if Env.banano() else 6

    @staticmethod
    def donation_address() -> str:
        return 'prtc_3p97if96icoskyk4zt3dddkczuq5j4s8mr1r51je3dzzzyu59s6fs5z34hfx' if Env.banano() else 'nano_1bboss18y784j9rbwgt95uwqamjpsi9oips5syohsjk37rn5ud7ndbjq61ft'