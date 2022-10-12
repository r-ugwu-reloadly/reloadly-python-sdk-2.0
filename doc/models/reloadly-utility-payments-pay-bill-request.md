
# Reloadly Utility Payments Pay Bill Request

## Structure

`ReloadlyUtilityPaymentsPayBillRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscriber_account_number` | `string` | Required | - |
| `amount` | `int` | Required | - |
| `biller_id` | `int` | Required | - |
| `use_local_amount` | `bool` | Required | - |

## Example (as JSON)

```json
{
  "subscriberAccountNumber": "04223568280",
  "amount": 1000,
  "billerId": 5,
  "useLocalAmount": false
}
```

