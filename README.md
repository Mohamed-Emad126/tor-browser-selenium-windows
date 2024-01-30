# tor-browser-selenium for windows

A Python library to automate Tor Browser with Selenium WebDriver for windows

## 📦 Installation for Windows users

```
download tbselenuim folder and put it in your project directory
```

Download `geckodriver` v0.31.0 from the [geckodriver releases page](https://github.com/mozilla/geckodriver/releases/)
and pass its path when you initialize `TorBrowserDriver`. In the examples below, you should replace `gecko_driver_exe`
with the path to the **geckodriver.exe** file

## 🚀 Usage

Download and extract [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en), and pass its path when you
initialize `TorBrowserDriver`. In the examples below, you should replace `tor_browser_dir` with the path to the **Tor
Browser** folder.

### Example `tor`

`tor` needs to be installed (`apt install tor`) and running on port 9050.
So, Before running the script, you need to run `tor.exe` in the tor browser folder and wait for it to connect to the tor
network

```python
from tbselenium.common import USE_STEM
from tbselenium.tbdriver import TorBrowserDriver

url = "https://github.com/"

tor_browser_dir = r"C:\Users\MohamedEmad126\Desktop\Tor Browser"  # change to your own tor-browser directory
gecko_driver_exe = r"C:\WebDriver\bin\geckodriver.exe"  # change to your own geckodriver path

with TorBrowserDriver(tbb_path=tor_browser_dir,
                      executable_path=gecko_driver_exe,
                      tor_cfg=USE_STEM) as driver:
    driver.load_url(url)
```

For more information and examples and usage, please refer to the original repo: [tor-browser-selenium](https://github.com/webfp/tor-browser-selenium)


## 📚 Reference

Please use the following reference if you use `tor-browser-selenium` in your academic publications.

```
@misc{tor-browser-selenium,
  author = {Gunes Acar and Marc Juarez and individual contributors},
  title = {tor-browser-selenium - Tor Browser automation with Selenium},
  year = {2023},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/webfp/tor-browser-selenium}}
}
```

## 🙌 Credits

We greatly benefited from
the [tor-browser-bundle-testsuite](https://gitlab.torproject.org/tpo/applications/tor-browser-bundle-testsuite)
and [tor-browser-selenium](https://github.com/isislovecruft/tor-browser-selenium) projects.
