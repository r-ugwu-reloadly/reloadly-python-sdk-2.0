# Gift Cards-Discounts

```python
gift_cards_discounts_controller = client.gift_cards_discounts
```

## Class Name

`GiftCardsDiscountsController`

## Methods

* [Reloadly-Gift-Cards-Discounts](../../doc/controllers/gift-cards-discounts.md#reloadly-gift-cards-discounts)
* [Reloadly-Gift-Cards-Discount-by-Product-Id](../../doc/controllers/gift-cards-discounts.md#reloadly-gift-cards-discount-by-product-id)


# Reloadly-Gift-Cards-Discounts

```python
def reloadly_gift_cards_discounts(self,
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
| `size` | `string` | Template, Optional | Indicates the number of gift card products offering discounts to be retrieved on a page. |
| `page` | `string` | Template, Optional | Indicates the page of the list of gift card products offering discounts. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.giftcards-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
size = '50'
page = '2'

result = gift_cards_discounts_controller.reloadly_gift_cards_discounts(accept, authorization, size, page)
```

## Example Response

```
[
  {
    "product": {
      "productId": 28,
      "productName": "Apple Music 12 month Canada",
      "countryCode": "CA",
      "global": false
    },
    "discountPercentage": 2
  },
  {},
  {}
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Not Found | `APIException` |


# Reloadly-Gift-Cards-Discount-by-Product-Id

```python
def reloadly_gift_cards_discount_by_product_id(self,
                                              accept,
                                              authorization,
                                              productid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `productid` | `string` | Template, Required | The product's identification number. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.giftcards-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
productid = '5'

result = gift_cards_discounts_controller.reloadly_gift_cards_discount_by_product_id(accept, authorization, productid)
```

## Example Response

```
{
  "product": {
    "productId": 28,
    "productName": "Apple Music 12 month Canada",
    "countryCode": "CA",
    "global": false
  },
  "discountPercentage": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Not found | `APIException` |

