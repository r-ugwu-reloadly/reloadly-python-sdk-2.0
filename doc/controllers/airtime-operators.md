# Airtime-Operators

```python
airtime_operators_controller = client.airtime_operators
```

## Class Name

`AirtimeOperatorsController`

## Methods

* [Reloadly-Airtime-Operators](../../doc/controllers/airtime-operators.md#reloadly-airtime-operators)
* [Reloadly-Airtime-Operator-Autodetect](../../doc/controllers/airtime-operators.md#reloadly-airtime-operator-autodetect)
* [Reloadly-Airtime-Operator-by-Id](../../doc/controllers/airtime-operators.md#reloadly-airtime-operator-by-id)
* [Reloadly-Airtime-Operator-by-Iso](../../doc/controllers/airtime-operators.md#reloadly-airtime-operator-by-iso)


# Reloadly-Airtime-Operators

```python
def reloadly_airtime_operators(self,
                              accept,
                              authorization,
                              include_bundles=None,
                              include_data=None,
                              suggested_amounts_map=None,
                              size=None,
                              page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `include_bundles` | `string` | Query, Optional | Indicates if any airtime and data bundles being offered by the operator should be included in the API response. Default value is true. |
| `include_data` | `string` | Query, Optional | Indicates if any airtime or data plans being offered by the operator should be included in the API response. Default value is true. |
| `suggested_amounts_map` | `string` | Query, Optional | Indicates if this field should be returned as a response. Default value is false. |
| `size` | `string` | Query, Optional | This indicates the number of operators to be retrieved on a page. Default value is 200. |
| `page` | `string` | Query, Optional | This indicates the page of the operator list being retrieved. Default value is 1. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
include_bundles = 'true'
include_data = 'true'
suggested_amounts_map = 'false'
size = '10'
page = '2'

result = airtime_operators_controller.reloadly_airtime_operators(accept, authorization, include_bundles, include_data, suggested_amounts_map, size, page)
```

## Example Response

```
{
  "content": [
    {
      "id": 88,
      "operatorId": 88,
      "name": "Movistar Colombia",
      "bundle": false,
      "data": false,
      "pin": false,
      "supportsLocalAmounts": false,
      "denominationType": "RANGE",
      "senderCurrencyCode": "USD",
      "senderCurrencySymbol": "$",
      "destinationCurrencyCode": "COP",
      "destinationCurrencySymbol": "$",
      "commission": 4.42,
      "internationalDiscount": 4.42,
      "localDiscount": 0,
      "mostPopularAmount": null,
      "minAmount": 5,
      "maxAmount": 5,
      "localMinAmount": null,
      "localMaxAmount": null,
      "country": {
        "isoName": "CO",
        "name": "Colombia"
      },
      "fx": {
        "rate": 2192.1867,
        "currencyCode": "COP"
      },
      "logoUrls": [
        "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-1.png",
        "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-2.png",
        "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-3.png"
      ],
      "fixedAmounts": [],
      "fixedAmountsDescriptions": [],
      "localFixedAmounts": [],
      "localFixedAmountsDescriptions": [],
      "suggestedAmounts": [
        7,
        10,
        15
      ],
      "suggestedAmountsMap": {
        "7": 19482.51,
        "10": 27832.16,
        "15": 41748.23
      },
      "promotions": []
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


# Reloadly-Airtime-Operator-Autodetect

```python
def reloadly_airtime_operator_autodetect(self,
                                        accept,
                                        authorization,
                                        phone,
                                        countryisocode,
                                        countrycode,
                                        suggested_amounts=None,
                                        suggested_amounts_map=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `phone` | `string` | Template, Required | The mobile number whose details are to be retrieved. |
| `countryisocode` | `string` | Template, Required | The ISO code of the country where the mobile number is registered. |
| `countrycode` | `string` | Template, Required | - |
| `suggested_amounts` | `bool` | Query, Optional | Indicates if this field should be returned as a response. Default value is false. |
| `suggested_amounts_map` | `bool` | Query, Optional | Indicates if this field should be returned as a response. Default value is false. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
phone = '8147658721'
countryisocode = 'US'
countrycode = 'countrycode6'
suggested_amounts = False
suggested_amounts_map = True

result = airtime_operators_controller.reloadly_airtime_operator_autodetect(accept, authorization, phone, countryisocode, countrycode, suggested_amounts, suggested_amounts_map)
```

## Example Response

```
{
  "id": 88,
  "operatorId": 88,
  "name": "Movistar Colombia",
  "bundle": false,
  "data": false,
  "pin": false,
  "supportsLocalAmounts": false,
  "denominationType": "RANGE",
  "senderCurrencyCode": "USD",
  "senderCurrencySymbol": "$",
  "destinationCurrencyCode": "COP",
  "destinationCurrencySymbol": "$",
  "commission": 4.42,
  "internationalDiscount": 4.42,
  "localDiscount": 0,
  "mostPopularAmount": null,
  "minAmount": 5,
  "maxAmount": 5,
  "localMinAmount": null,
  "localMaxAmount": null,
  "country": {
    "isoName": "CO",
    "name": "Colombia"
  },
  "fx": {
    "rate": 2192.1867,
    "currencyCode": "COP"
  },
  "logoUrls": [
    "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-1.png",
    "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-2.png",
    "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-3.png"
  ],
  "fixedAmounts": [],
  "fixedAmountsDescriptions": [],
  "localFixedAmounts": [],
  "localFixedAmountsDescriptions": [],
  "suggestedAmounts": [
    7,
    10,
    15
  ],
  "suggestedAmountsMap": {
    "7": 19482.51,
    "10": 27832.16,
    "15": 41748.23
  },
  "promotions": []
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Country code must be 2 characters ISO-Alpha-2 country code. See https://www.iban.com/country-codes | `APIException` |


# Reloadly-Airtime-Operator-by-Id

```python
def reloadly_airtime_operator_by_id(self,
                                   accept,
                                   authorization,
                                   operatorid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `operatorid` | `string` | Template, Required | The operator's identification number. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
operatorid = '88'

result = airtime_operators_controller.reloadly_airtime_operator_by_id(accept, authorization, operatorid)
```

## Example Response

```
{
  "id": 88,
  "operatorId": 88,
  "name": "Movistar Colombia",
  "bundle": false,
  "data": false,
  "pin": false,
  "supportsLocalAmounts": false,
  "denominationType": "RANGE",
  "senderCurrencyCode": "USD",
  "senderCurrencySymbol": "$",
  "destinationCurrencyCode": "COP",
  "destinationCurrencySymbol": "$",
  "commission": 4.42,
  "internationalDiscount": 4.42,
  "localDiscount": 0,
  "mostPopularAmount": null,
  "minAmount": 5,
  "maxAmount": 5,
  "localMinAmount": null,
  "localMaxAmount": null,
  "country": {
    "isoName": "CO",
    "name": "Colombia"
  },
  "fx": {
    "rate": 2192.1867,
    "currencyCode": "COP"
  },
  "logoUrls": [
    "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-1.png",
    "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-2.png",
    "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-3.png"
  ],
  "fixedAmounts": [],
  "fixedAmountsDescriptions": [],
  "localFixedAmounts": [],
  "localFixedAmountsDescriptions": [],
  "suggestedAmounts": [
    7,
    10,
    15
  ],
  "suggestedAmountsMap": {
    "7": 19482.51,
    "10": 27832.16,
    "15": 41748.23
  },
  "promotions": []
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Operator not found for given id | `APIException` |


# Reloadly-Airtime-Operator-by-Iso

```python
def reloadly_airtime_operator_by_iso(self,
                                    accept,
                                    authorization,
                                    countrycode,
                                    include_bundles,
                                    suggested_amounts_map=None,
                                    suggested_amounts=None,
                                    include_pin=None,
                                    include_data=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Query, Required | - |
| `countrycode` | `string` | Template, Required | The ISO code of the country where the operator is registered. |
| `include_bundles` | `bool` | Query, Required | Indicates if any airtime and data bundles being offered by the operator should be returned as a response. Default value is true. |
| `suggested_amounts_map` | `bool` | Query, Optional | Indicates if this field should be returned as a response. Default value is false. |
| `suggested_amounts` | `string` | Query, Optional | Indicates if this field should be returned as a response. Default value is false. |
| `include_pin` | `bool` | Query, Optional | Indicates if PIN details if applicable to the operator, should be returned as a response. Default value is true. |
| `include_data` | `bool` | Query, Optional | Indicates if any data plans being offered by the operator should be returned as a response. Default value is true. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
countrycode = 'US'
include_bundles = False
suggested_amounts_map = False
suggested_amounts = 'false'
include_pin = False
include_data = False

result = airtime_operators_controller.reloadly_airtime_operator_by_iso(accept, authorization, countrycode, include_bundles, suggested_amounts_map, suggested_amounts, include_pin, include_data)
```

## Example Response

```
{
  "example": {
    "id": 88,
    "operatorId": 88,
    "name": "Movistar Colombia",
    "bundle": false,
    "data": false,
    "pin": false,
    "supportsLocalAmounts": false,
    "denominationType": "RANGE",
    "senderCurrencyCode": "USD",
    "senderCurrencySymbol": "$",
    "destinationCurrencyCode": "COP",
    "destinationCurrencySymbol": "$",
    "commission": 4.42,
    "internationalDiscount": 4.42,
    "localDiscount": 0,
    "mostPopularAmount": null,
    "minAmount": 5,
    "maxAmount": 5,
    "localMinAmount": null,
    "localMaxAmount": null,
    "country": {
      "isoName": "CO",
      "name": "Colombia"
    },
    "fx": {
      "rate": 2192.1867,
      "currencyCode": "COP"
    },
    "logoUrls": [
      "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-1.png",
      "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-2.png",
      "https://s3.amazonaws.com/rld-operator/3f4a8bcd3268-size-3.png"
    ],
    "fixedAmounts": [],
    "fixedAmountsDescriptions": [],
    "localFixedAmounts": [],
    "localFixedAmountsDescriptions": [],
    "suggestedAmounts": [
      7,
      10,
      15
    ],
    "suggestedAmountsMap": {
      "7": 19482.51,
      "10": 27832.16,
      "15": 41748.23
    },
    "promotions": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Country not found and/or not currently supported | `APIException` |

