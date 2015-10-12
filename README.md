An implementation of the Algorithm::CouponCode for Python.

Usage
=====
```
from coupon_codes import cc_generate, cc_validate

cc_generate()
=> 'XHGH-AMYT-3E9J'

cc_generate(n_parts=4)
=> 'EJM0-5P1U-QBVV-VQGA'

cc_generate(part_len=6)
=> 'A7QR3V-E06M8X-LWQN22'

cc_validate('xhgh-amyt-3e9j')
=> 'XHGH-AMYT-3E9J'

cc_validate('ejmo-spIu-qbvv-vqga', n_parts=4)
=> 'EJM0-5P1U-QBVV-VQGA'

cc_validate('a7qr3v-eo6m8x-lwqn22', part_len=6)
=> 'A7QR3V-E06M8X-LWQN22'

cc_validate('abcd-efgh-ijkl')
=> ''
```
