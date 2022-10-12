# Airtime-Transactions

```python
airtime_transactions_controller = client.airtime_transactions
```

## Class Name

`AirtimeTransactionsController`

## Methods

* [Reloadly-Airtime-Transactions](../../doc/controllers/airtime-transactions.md#reloadly-airtime-transactions)
* [Reloadly-Airtime-Transaction-by-Id](../../doc/controllers/airtime-transactions.md#reloadly-airtime-transaction-by-id)


# Reloadly-Airtime-Transactions

```python
def reloadly_airtime_transactions(self,
                                 accept,
                                 authorization,
                                 size=None,
                                 page=None,
                                 countrycode=None,
                                 operatorid=None,
                                 operator_name=None,
                                 custom_identifier=None,
                                 start_date=None,
                                 end_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `size` | `int` | Query, Optional | This indicates the number of transactions to be retrieved on a page. Default value is 200. |
| `page` | `int` | Query, Optional | This indicates the page of the transactions list being retrieved. Default value is 1. |
| `countrycode` | `int` | Query, Optional | Indicates the ISO code of the country assigned to the top-up's receiver at the time the top-up transaction was made. |
| `operatorid` | `string` | Query, Optional | Indicates the operator identification number assigned to the top-up transaction at the time it was made. |
| `operator_name` | `string` | Query, Optional | Indicates the operator name assigned to the top-up transaction at the time it was made. |
| `custom_identifier` | `string` | Query, Optional | Indicates the unique reference assigned to the top-up transaction at the time it was made. |
| `start_date` | `string` | Query, Optional | Indicates the beginning of the timeframe range for the transactions to be retrieved. |
| `end_date` | `string` | Query, Optional | String  Indicates the end of the timeframe range for the transactions to be retrieved. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
size = 10
page = 1
operatorid = '341'
operator_name = 'MTN Nigeria'
custom_identifier = 'april-top-up'
start_date = '2021-04-30 00:00:00'
end_date = '2021-07-30 00:00:00'

result = airtime_transactions_controller.reloadly_airtime_transactions(accept, authorization, size, page, None, operatorid, operator_name, custom_identifier, start_date, end_date)
```

## Example Response

```
{
  "content": [
    {
      "transactionId": 4602843,
      "status": "SUCCESSFUL",
      "operatorTransactionId": "7297929551:OrderConfirmed",
      "customIdentifier": "This is example identifier 130",
      "recipientPhone": 447951631337,
      "recipientEmail": null,
      "senderPhone": 11231231231,
      "countryCode": "GB",
      "operatorId": 535,
      "operatorName": "EE PIN England",
      "discount": 63.37,
      "discountCurrencyCode": "NGN",
      "requestedAmount": 3168.4,
      "requestedAmountCurrencyCode": "NGN",
      "deliveredAmount": 4.9985,
      "deliveredAmountCurrencyCode": "GBP",
      "transactionDate": "2021-12-06 08:13:39",
      "pinDetail": {
        "serial": 558111,
        "info1": "DIAL *611",
        "info2": "DIAL *611",
        "info3": "DIAL *611",
        "value": null,
        "code": 773709733097662,
        "ivr": "1-888-888-8888",
        "validity": "30 days"
      },
      "balanceInfo": null
    },
    {},
    {}
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Not Found | `APIException` |


# Reloadly-Airtime-Transaction-by-Id

```python
def reloadly_airtime_transaction_by_id(self,
                                      accept,
                                      authorization,
                                      transactionid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `transactionid` | `int` | Template, Required | This indicates the identification number of the transaction to be retrieved. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
transactionid = 101

result = airtime_transactions_controller.reloadly_airtime_transaction_by_id(accept, authorization, transactionid)
```

## Example Response

```
{
  "transactionId": 4602843,
  "status": "SUCCESSFUL",
  "operatorTransactionId": "7297929551:OrderConfirmed",
  "customIdentifier": "This is example identifier 130",
  "recipientPhone": 447951631337,
  "recipientEmail": null,
  "senderPhone": 11231231231,
  "countryCode": "GB",
  "operatorId": 535,
  "operatorName": "EE PIN England",
  "discount": 63.37,
  "discountCurrencyCode": "NGN",
  "requestedAmount": 3168.4,
  "requestedAmountCurrencyCode": "NGN",
  "deliveredAmount": 4.9985,
  "deliveredAmountCurrencyCode": "GBP",
  "transactionDate": "2021-12-06 08:13:39",
  "pinDetail": {
    "serial": 558111,
    "info1": "DIAL *611",
    "info2": "DIAL *611",
    "info3": "DIAL *611",
    "value": null,
    "code": 773709733097662,
    "ivr": "1-888-888-8888",
    "validity": "30 days"
  },
  "balanceInfo": null
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Airtime transaction not found | `APIException` |

