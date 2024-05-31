Hi <Customer Name>,

Thanks for reaching out! I'm happy to assist you integrating your current scraping solution with Zyte Smart Proxy Manager (SPM) and clarifying how to rotate proxies and select IP regions.

### __Configuring Selenium with SPM__

The easiest way to integrate SPM with Selenium is using [Zyte SmartProxy Selenium](https://docs.zyte.com/smart-proxy-manager/integrations/selenium.html#option-1-zyte-smartproxy-selenium), you'll only need to swap the default selenium package with [zyte-smartproxy-selenium](https://github.com/zytedata/zyte-smartproxy-selenium) and provide your SPM API Key when configuring the driver.

```python
# Make sure to install the package before testing.
# python3 -m pip install zyte-smartproxy-selenium

from zyte_smartproxy_selenium import webdriver

browser = webdriver.Chrome(spm_options={'spm_apikey': '<Smart Proxy Manager API KEY>'})
browser.get('https://toscrape.com')
browser.save_screenshot('screenshot.png')
browser.close()
```

If for some reason this does not work for your needs, you can use [Zyte SmartProxy Headless Proxy](https://docs.zyte.com/smart-proxy-manager/integrations/selenium.html#option-1-zyte-smartproxy-selenium), which allows you to authenticate to SPM beforehand, and use a localhost port as your proxy address.

### __Proxy Rotation__

Since SPM handles proxy rotations automatically, each request you make will use a different IP address by default. This automatic rotation helps ensure successful responses and prevents IP bans. You don't need to handle the rotation manually. However, if you want to implement some custom logic for it, you can use the 'X-Crawlera-Session' header in your requests.

To request a new session, use 'X-Crawlera-Session: create', and you'll receive the session ID in the response headers. Then, You may use this session ID in your subsequent requests with 'X-Crawlera-Session: <session ID>'. For more information about sessions, please refer to our [documentation on sessions](https://docs.zyte.com/smart-proxy-manager/sessions.html).

### __Selecting IP Regions__

Zyte SPM allows for country-level region restriction using the 'X-Crawlera-Region' header with a country code in ISO format (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). You can use either upper or lower case (e.g., 'X-Crawlera-Region: FR' or 'X-Crawlera-Region: fr' for France).

If you have any further questions or need additional assistance, feel free to message, we are here to help.

Sincerely,

Italo Oliveira
Technical Support Specialist
Zyte
