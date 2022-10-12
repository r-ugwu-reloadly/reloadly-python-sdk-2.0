# Gift Cards-Account Balance

```python
gift_cards_account_balance_controller = client.gift_cards_account_balance
```

## Class Name

`GiftCardsAccountBalanceController`


# Reloadly-Gift-Cards-Account-Balance

```python
def reloadly_gift_cards_account_balance(self,
                                       accept,
                                       authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.giftcards-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'

result = gift_cards_account_balance_controller.reloadly_gift_cards_account_balance(accept, authorization)
```

## Example Response

```
{
  "balance": 6000,
  "currencyCode": "USD",
  "currencyName": "US Dollar",
  "updatedAt": "2022-02-04 17:45:51"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Not Found | `APIException` |

