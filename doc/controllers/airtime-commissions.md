# Airtime-Commissions

```python
airtime_commissions_controller = client.airtime_commissions
```

## Class Name

`AirtimeCommissionsController`

## Methods

* [Reloadly-Airtime-Commissions](../../doc/controllers/airtime-commissions.md#reloadly-airtime-commissions)
* [Reloadly-Airtime-Commission-by-Id](../../doc/controllers/airtime-commissions.md#reloadly-airtime-commission-by-id)


# Reloadly-Airtime-Commissions

```python
def reloadly_airtime_commissions(self,
                                accept,
                                authorization,
                                size=None,
                                page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `size` | `int` | Query, Optional | This indicates the number of operators offering discounts to be retrieved on a page. Default value is 200. |
| `page` | `int` | Query, Optional | This indicates the page of the discounts list being retrieved. Default value is 1. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
size = 10
page = 1

result = airtime_commissions_controller.reloadly_airtime_commissions(accept, authorization, size, page)
```

## Example Response

```
{
  "content": [
    {
      "operator": {
        "operatorId": 1,
        "name": "Afghan Wireless Afghanistan",
        "countryCode": "AF",
        "status": true,
        "bundle": false
      },
      "percentage": 10,
      "internationalPercentage": 10,
      "localPercentage": 0,
      "updatedAt": "2021-06-26 03:36:16"
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


# Reloadly-Airtime-Commission-by-Id

```python
def reloadly_airtime_commission_by_id(self,
                                     accept,
                                     authorization,
                                     operatorid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `operatorid` | `string` | Template, Required | - |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.topups-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
operatorid = '341'

result = airtime_commissions_controller.reloadly_airtime_commission_by_id(accept, authorization, operatorid)
```

## Example Response

```
{
  "operator": {
    "operatorId": 1,
    "name": "Afghan Wireless Afghanistan",
    "countryCode": "AF",
    "status": true,
    "bundle": false
  },
  "percentage": 10,
  "internationalPercentage": 10,
  "localPercentage": 0,
  "updatedAt": "2021-06-26 03:36:16"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Operator not found for given ID | `APIException` |

