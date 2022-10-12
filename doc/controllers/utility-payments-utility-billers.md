# Utility Payments-Utility Billers

```python
utility_payments_utility_billers_controller = client.utility_payments_utility_billers
```

## Class Name

`UtilityPaymentsUtilityBillersController`


# Reloadly-Utility-Payments-Billers

```python
def reloadly_utility_payments_billers(self,
                                     accept,
                                     authorization,
                                     id=None,
                                     name=None,
                                     mtype=None,
                                     service_type=None,
                                     country_iso_code=None,
                                     page=None,
                                     size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `id` | `int` | Query, Optional | This is the unique identification number of each biller. It uniquely identifies the biller servicing the utility. |
| `name` | `string` | Query, Optional | This indicates the biller's name. In situations where the biller's name is exceptionally long, partial names are used. |
| `mtype` | `string` | Query, Optional | This indicates the type of utility payment handled by the biller. Values included are ELECTRICITY_BILL_PAYMENT, WATER_BILL_PAYMENT, TV_BILL_PAYMENT and INTERNET_BILL_PAYMENT. |
| `service_type` | `string` | Query, Optional | This indicates the payment service type being rendered by the utility biller service. Examples are PREPAID and POSTPAID. |
| `country_iso_code` | `string` | Query, Optional | This indicates the ISO code of the country where the utility biller is operating in. |
| `page` | `int` | Query, Optional | This indicates the page of the billers list being retrieved. Default value is 1. |
| `size` | `int` | Query, Optional | This indicates the number of billers to be retrieved on a page. Default value is 200. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.utilities-v1+json'
authorization = 'Bearer <YOUR TOKEN HERE>'
id = 12
name = 'Eko Electricity'
mtype = 'ELECTRICITY_BILL_PAYMENT'
service_type = 'PREPAID'
country_iso_code = 'KE'
page = 1
size = 10

result = utility_payments_utility_billers_controller.reloadly_utility_payments_billers(accept, authorization, id, name, mtype, service_type, country_iso_code, page, size)
```

## Example Response

```
{
  "content": [
    {
      "id": 1,
      "name": "Ikeja Electricity Postpaid",
      "countryIsoCode": "NG",
      "type": "ELECTRICITY_BILL_PAYMENT",
      "serviceType": "POSTPAID",
      "localAmountSupported": true,
      "localTransactionCurrencyCode": "NGN",
      "minLocalTransactionAmount": 1000,
      "maxLocalTransactionAmount": 300000,
      "localTransactionFee": 227.83997,
      "localTransactionFeeCurrencyCode": "NGN",
      "localDiscountPercentage": 0,
      "internatonalAmountSupported": true,
      "internationalTransactionCurrencyCode": "INR",
      "minInternationalTransactionAmount": 194.73483,
      "maxInternationalTransactionAmount": 45567.996,
      "internationalTransactionFee": 227.83997,
      "internationalTransactionFeeCurrencyCode": "INR",
      "internationalDiscountPercentage": 0,
      "fx": [
        {
          "rate": 5.20265
        },
        {
          "curencyCode": "INR"
        }
      ]
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

