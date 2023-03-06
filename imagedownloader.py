import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def convert_html_png(html):
    # Define the HTML markup to be saved and downloaded as a PNG image
    html = "<h1>Hello, world!</h1><p>This is an example HTML page.</p>"

    # Define the filename for the temporary HTML file
    html_filename = "chart.html"

    # Save the HTML markup to a temporary file
    with open(html_filename, "w") as f:
        f.write(html)

    # Set up the Selenium WebDriver to take a screenshot of the HTML file as a PNG image
    firefox_options = Options()
    firefox_options.headless = True
    firefox_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(f"file://{tempfile.gettempdir()}/{html_filename}")
    screenshot = driver.get_screenshot_as_png()

    # Define the filename for the downloaded PNG image file
    png_filename = "chart.png"
    return screenshot, png_filename