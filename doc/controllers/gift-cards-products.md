# Gift Cards-Products

```python
gift_cards_products_controller = client.gift_cards_products
```

## Class Name

`GiftCardsProductsController`

## Methods

* [Reloadly-Gift-Cards-Products](../../doc/controllers/gift-cards-products.md#reloadly-gift-cards-products)
* [Reloadly-Gift-Cards-Product-by-Id](../../doc/controllers/gift-cards-products.md#reloadly-gift-cards-product-by-id)
* [Reloadly-Gift-Cards-Product-by-Iso](../../doc/controllers/gift-cards-products.md#reloadly-gift-cards-product-by-iso)


# Reloadly-Gift-Cards-Products

```python
def reloadly_gift_cards_products(self,
                                accept,
                                authorization,
                                include_range=None,
                                include_fixed=None,
                                size=None,
                                page=None,
                                product_name=None,
                                country_code=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `include_range` | `bool` | Query, Optional | Indicates the list of gift card products with the denominationType property specified as RANGE are to be retrieved. |
| `include_fixed` | `bool` | Query, Optional | Indicates the list of gift card products with the denominationType property specified as FIXED are to be retrieved. |
| `size` | `int` | Query, Optional | This indicates the number of gift card products to be retrieved on a page. |
| `page` | `string` | Query, Optional | This indicates the page of the product list being retrieved. |
| `product_name` | `string` | Query, Optional | Indicates the name of the gift card product. |
| `country_code` | `string` | Query, Optional | Indicates the ISO code of the country whose gift card products are to be retrieved. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.giftcards-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
include_range = True
include_fixed = True
size = 10
page = '1'
product_name = 'Amazon'
country_code = 'US'

result = gift_cards_products_controller.reloadly_gift_cards_products(accept, authorization, include_range, include_fixed, size, page, product_name, country_code)
```

## Example Response

```
[
  {
    "productId": 1,
    "productName": "1-800-PetSupplies",
    "global": false,
    "senderFee": 205.29,
    "discountPercentage": 7.5,
    "denominationType": "FIXED",
    "recipientCurrencyCode": "USD",
    "minRecipientDenomination": null,
    "maxrecipientDenomination": null,
    "senderCurrencyCode": "NGN",
    "minSenderDenomination": null,
    "maxSenderDenomination": null,
    "fixedRecipientDenominations": [
      25,
      50
    ],
    "fixedSenderDenominations": [
      10264.5,
      20529
    ],
    "fixedRecipientToSenderDenominationsMap": [
      {
        "25.00": 10264.5
      },
      {
        "50.00": 20529
      }
    ],
    "logoUrls": [
      "https://cdn.reloadly.com/giftcards/5daa2b8b-b1ad-4ca6-a34d-a7ce3c14dfaf.jpg"
    ],
    "brand": {
      "brandId": 1,
      "brandName": "1-800-PetSupplies"
    },
    "country": {
      "isoName": "US",
      "name": "United States",
      "flagUrl": "https://s3.amazonaws.com/rld-flags/us.svg"
    },
    "redeemInstruction": {
      "concise": "This card is redeemable for merchandise on www.1-800-petsupplies.com",
      "verbose": "Your acceptance of this eCertificate constitutes your agreement to these terms and conditions. This card is redeemable in U.S. only for merchandise on www.1-800-petsupplies.com . Only two eCertificates are redeemable per order. eCertificates cannot be redeemed for cash, except as required by law. Void if altered or reproduced. This gift card is issued in U.S. funds by Tabcom, LLC. When Redeeming online please be sure to enter the entire gift card number including preceding zeros. The maximum number of eCertificates that can be used for phone is nine. By accepting these Terms and Conditions through your use of this Site, you certify that you reside in the United States and are 18 years of age or older. If you are under the age of 18 but at least 14 years of age you may use this Site only under the supervision of a parent or legal guardian who agrees to be bound by these Terms and Conditions."
    }
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


# Reloadly-Gift-Cards-Product-by-Id

```python
def reloadly_gift_cards_product_by_id(self,
                                     accept,
                                     authorization,
                                     productid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `productid` | `int` | Template, Required | The product's identification number. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.giftcards-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
productid = 10

result = gift_cards_products_controller.reloadly_gift_cards_product_by_id(accept, authorization, productid)
```

## Example Response

```
{
  "productId": 1,
  "productName": "1-800-PetSupplies",
  "global": false,
  "senderFee": 205.29,
  "discountPercentage": 7.5,
  "denominationType": "FIXED",
  "recipientCurrencyCode": "USD",
  "minRecipientDenomination": null,
  "maxrecipientDenomination": null,
  "senderCurrencyCode": "NGN",
  "minSenderDenomination": null,
  "maxSenderDenomination": null,
  "fixedRecipientDenominations": [
    25,
    50
  ],
  "fixedSenderDenominations": [
    10264.5,
    20529
  ],
  "fixedRecipientToSenderDenominationsMap": [
    {
      "25.00": 10264.5
    },
    {
      "50.00": 20529
    }
  ],
  "logoUrls": [
    "https://cdn.reloadly.com/giftcards/5daa2b8b-b1ad-4ca6-a34d-a7ce3c14dfaf.jpg"
  ],
  "brand": {
    "brandId": 1,
    "brandName": "1-800-PetSupplies"
  },
  "country": {
    "isoName": "US",
    "name": "United States",
    "flagUrl": "https://s3.amazonaws.com/rld-flags/us.svg"
  },
  "redeemInstruction": {
    "concise": "This card is redeemable for merchandise on www.1-800-petsupplies.com",
    "verbose": "Your acceptance of this eCertificate constitutes your agreement to these terms and conditions. This card is redeemable in U.S. only for merchandise on www.1-800-petsupplies.com . Only two eCertificates are redeemable per order. eCertificates cannot be redeemed for cash, except as required by law. Void if altered or reproduced. This gift card is issued in U.S. funds by Tabcom, LLC. When Redeeming online please be sure to enter the entire gift card number including preceding zeros. The maximum number of eCertificates that can be used for phone is nine. By accepting these Terms and Conditions through your use of this Site, you certify that you reside in the United States and are 18 years of age or older. If you are under the age of 18 but at least 14 years of age you may use this Site only under the supervision of a parent or legal guardian who agrees to be bound by these Terms and Conditions."
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The product was either not found or is no longer available, Please contact support | `APIException` |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Not found | `APIException` |


# Reloadly-Gift-Cards-Product-by-Iso

```python
def reloadly_gift_cards_product_by_iso(self,
                                      accept,
                                      authorization,
                                      countrycode)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `string` | Header, Required | - |
| `authorization` | `string` | Header, Required | - |
| `countrycode` | `string` | Template, Required | The ISO code of the country you want to display available gift cards for. |

## Response Type

`mixed`

## Example Usage

```python
accept = 'application/com.reloadly.giftcards-v1+json'
authorization = 'Bearer <YOUR_TOKEN_HERE>'
countrycode = 'US'

result = gift_cards_products_controller.reloadly_gift_cards_product_by_iso(accept, authorization, countrycode)
```

## Example Response

```
{
  "productId": 1,
  "productName": "1-800-PetSupplies",
  "global": false,
  "senderFee": 205.29,
  "discountPercentage": 7.5,
  "denominationType": "FIXED",
  "recipientCurrencyCode": "USD",
  "minRecipientDenomination": null,
  "maxrecipientDenomination": null,
  "senderCurrencyCode": "NGN",
  "minSenderDenomination": null,
  "maxSenderDenomination": null,
  "fixedRecipientDenominations": [
    25,
    50
  ],
  "fixedSenderDenominations": [
    10264.5,
    20529
  ],
  "fixedRecipientToSenderDenominationsMap": [
    {
      "25.00": 10264.5
    },
    {
      "50.00": 20529
    }
  ],
  "logoUrls": [
    "https://cdn.reloadly.com/giftcards/5daa2b8b-b1ad-4ca6-a34d-a7ce3c14dfaf.jpg"
  ],
  "brand": {
    "brandId": 1,
    "brandName": "1-800-PetSupplies"
  },
  "country": {
    "isoName": "US",
    "name": "United States",
    "flagUrl": "https://s3.amazonaws.com/rld-flags/us.svg"
  },
  "redeemInstruction": {
    "concise": "This card is redeemable for merchandise on www.1-800-petsupplies.com",
    "verbose": "Your acceptance of this eCertificate constitutes your agreement to these terms and conditions. This card is redeemable in U.S. only for merchandise on www.1-800-petsupplies.com . Only two eCertificates are redeemable per order. eCertificates cannot be redeemed for cash, except as required by law. Void if altered or reproduced. This gift card is issued in U.S. funds by Tabcom, LLC. When Redeeming online please be sure to enter the entire gift card number including preceding zeros. The maximum number of eCertificates that can be used for phone is nine. By accepting these Terms and Conditions through your use of this Site, you certify that you reside in the United States and are 18 years of age or older. If you are under the age of 18 but at least 14 years of age you may use this Site only under the supervision of a parent or legal guardian who agrees to be bound by these Terms and Conditions."
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Full authentication is required to access this resource | `APIException` |
| 404 | Country not found and/or not currently supported | `APIException` |

