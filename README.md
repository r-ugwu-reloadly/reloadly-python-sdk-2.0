
# Getting Started with reloadly-sdk

## Building

You must have Python `3 >=3.7, <= 3.9` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&step=installDependencies)

## Installation

The following section explains how to use the reloadlysdk library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&projectName=reloadlysdk&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&projectName=reloadlysdk&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&projectName=reloadlysdk&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&projectName=reloadlysdk&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from reloadlysdk.reloadlysdk_client import ReloadlysdkClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&projectName=reloadlysdk&libraryName=reloadlysdk.reloadlysdk_client&className=ReloadlysdkClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Reloadlysdk-Python&projectName=reloadlysdk&libraryName=reloadlysdk.reloadlysdk_client&className=ReloadlysdkClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

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

## List of APIs

* [Airtime-Account Balance](doc/controllers/airtime-account-balance.md)
* [Airtime-Countries](doc/controllers/airtime-countries.md)
* [Airtime-Operators](doc/controllers/airtime-operators.md)
* [Airtime-FX Rates](doc/controllers/airtime-fx-rates.md)
* [Airtime-Commissions](doc/controllers/airtime-commissions.md)
* [Airtime-Promotions](doc/controllers/airtime-promotions.md)
* [Airtime-Topups](doc/controllers/airtime-topups.md)
* [Airtime-Transactions](doc/controllers/airtime-transactions.md)
* [Gift Cards-Account Balance](doc/controllers/gift-cards-account-balance.md)
* [Gift Cards-Countries](doc/controllers/gift-cards-countries.md)
* [Gift Cards-Products](doc/controllers/gift-cards-products.md)
* [Gift Cards-Redeem Instructions](doc/controllers/gift-cards-redeem-instructions.md)
* [Gift Cards-Discounts](doc/controllers/gift-cards-discounts.md)
* [Gift Cards-Transactions](doc/controllers/gift-cards-transactions.md)
* [Gift Cards-Orders](doc/controllers/gift-cards-orders.md)
* [Airtime-Number Lookup](doc/controllers/airtime-number-lookup.md)
* [Utility Payments-Account Balance](doc/controllers/utility-payments-account-balance.md)
* [Utility Payments-Utility Billers](doc/controllers/utility-payments-utility-billers.md)
* [Utility Payments-Pay Bill](doc/controllers/utility-payments-pay-bill.md)
* [Utility Payments-Transactions](doc/controllers/utility-payments-transactions.md)
* [Authentication](doc/controllers/authentication.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

