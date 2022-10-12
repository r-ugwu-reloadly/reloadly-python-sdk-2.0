
# Reloadly Gift Cards Orders Request

## Structure

`ReloadlyGiftCardsOrdersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Required | - |
| `country_code` | `string` | Required | - |
| `quantity` | `int` | Required | - |
| `unit_price` | `int` | Required | - |
| `custom_identifier` | `string` | Required | - |
| `sender_name` | `string` | Required | - |
| `recipient_email` | `string` | Required | - |
| `recipient_phone_details` | [`RecipientPhoneDetails`](../../doc/models/recipient-phone-details.md) | Required | - |

## Example (as JSON)

```json
{
  "productId": 120,
  "countryCode": "US",
  "quantity": 1,
  "unitPrice": 1,
  "customIdentifier": "obucks10",
  "senderName": "John Doe",
  "recipientEmail": "anyone@email.com",
  "recipientPhoneDetails": {
    "countryCode": "ES",
    "phoneNumber": "657228901"
  }
}
```

