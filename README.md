# ethgasstation-client

![Build Status](https://github.com/makerdao/ethgasstation-client/actions/workflows/.github/workflows/tests.yaml/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/makerdao/ethgasstation-client/branch/master/graph/badge.svg)](https://codecov.io/gh/makerdao/ethgasstation-client)

Tiny asynchronous client of the ethgasstation.info API.

#### NOTE:
###### please see https://ethgasstation.info/blog/changes-to-egs-api/. You have to sign up for an API Key and use it when instantiating EthGasStation client. For backward compatibility reasons client can still be created without a key but this can result in API call failures. 

It operates using a background thread, which fetches current recommended gas prices from ethgasstation.info
every `refresh_interval` seconds. If due to network issues no current gas prices have been fetched
for `expiry` seconds, old values expire and all `*_price()` methods will start returning `None` until
the feed becomes available again.

<https://chat.makerdao.com/channel/keeper>

## Installation

This project uses *Python 3.6.6*.

In order to clone the project and install required third-party packages please execute:
```
git clone https://github.com/makerdao/ethgasstation-client.git
cd ethgasstation-client
pip3 install -r requirements.txt
```


## License

See [COPYING](https://github.com/makerdao/ethgasstation-client/blob/master/COPYING) file.


### Disclaimer

YOU (MEANING ANY INDIVIDUAL OR ENTITY ACCESSING, USING OR BOTH THE SOFTWARE INCLUDED IN THIS GITHUB REPOSITORY) EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SOFTWARE IS AT YOUR SOLE RISK.
THE SOFTWARE IN THIS GITHUB REPOSITORY IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
YOU RELEASE AUTHORS OR COPYRIGHT HOLDERS FROM ALL LIABILITY FOR YOU HAVING ACQUIRED OR NOT ACQUIRED CONTENT IN THIS GITHUB REPOSITORY. THE AUTHORS OR COPYRIGHT HOLDERS MAKE NO REPRESENTATIONS CONCERNING ANY CONTENT CONTAINED IN OR ACCESSED THROUGH THE SERVICE, AND THE AUTHORS OR COPYRIGHT HOLDERS WILL NOT BE RESPONSIBLE OR LIABLE FOR THE ACCURACY, COPYRIGHT COMPLIANCE, LEGALITY OR DECENCY OF MATERIAL CONTAINED IN OR ACCESSED THROUGH THIS GITHUB REPOSITORY. 
