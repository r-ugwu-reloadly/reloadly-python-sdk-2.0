
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from reloadlysdk.reloadlysdk_client import ReloadlysdkClient
from reloadlysdk.configuration import Environment

client = ReloadlysdkClient(
    environment=Environment.PRODUCTION,)
```

## reloadly-sdk Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| authentication | Gets AuthenticationController |
| airtime_account_balance | Gets AirtimeAccountBalanceController |
| airtime_countries | Gets AirtimeCountriesController |
| airtime_operators | Gets AirtimeOperatorsController |
| airtime_fx_rates | Gets AirtimeFXRatesController |
| airtime_commissions | Gets AirtimeCommissionsController |
| airtime_promotions | Gets AirtimePromotionsController |
| airtime_topups | Gets AirtimeTopupsController |
| airtime_transactions | Gets AirtimeTransactionsController |
| gift_cards_account_balance | Gets GiftCardsAccountBalanceController |
| gift_cards_countries | Gets GiftCardsCountriesController |
| gift_cards_products | Gets GiftCardsProductsController |
| gift_cards_redeem_instructions | Gets GiftCardsRedeemInstructionsController |
| gift_cards_discounts | Gets GiftCardsDiscountsController |
| gift_cards_transactions | Gets GiftCardsTransactionsController |
| gift_cards_orders | Gets GiftCardsOrdersController |
| airtime_number_lookup | Gets AirtimeNumberLookupController |
| utility_payments_account_balance | Gets UtilityPaymentsAccountBalanceController |
| utility_payments_utility_billers | Gets UtilityPaymentsUtilityBillersController |
| utility_payments_pay_bill | Gets UtilityPaymentsPayBillController |
| utility_payments_transactions | Gets UtilityPaymentsTransactionsController |

