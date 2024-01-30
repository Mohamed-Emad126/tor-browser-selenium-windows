from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tbselenium.common import USE_STEM
from tbselenium.tbdriver import TorBrowserDriver

url = "https://github.com/"

tor_browser_dir = r"C:\Users\MohamedEmad126\Desktop\Tor Browser"  # change to your own tor-browser directory
gecko_driver_exe = r"C:\WebDriver\bin\geckodriver.exe"  # change to your own geckodriver path

with TorBrowserDriver(tbb_path=tor_browser_dir,
                      executable_path=gecko_driver_exe,
                      tor_cfg=USE_STEM) as driver:
    try:
        driver.load_url(url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, """/html/body/div[1]/div[1]/header/div/div[2]/div/div/a""")))
    except Exception as e:
        print(e)
        driver.quit()
    finally:
        driver.close()
