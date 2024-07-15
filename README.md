# LinkedIn Job Saver

This project contains a Python script that uses Selenium to automate the process of logging into LinkedIn and saving job listings. The current implementation logs into LinkedIn, navigates to a specific job search page, and saves the first job listing on the page. 

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium package
- Chrome WebDriver

## Installation

1. Install Selenium using pip:
    ```bash
    pip install selenium
    ```

2. Download the Chrome WebDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory included in your system's PATH.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/Prathamesh326/Automating-Job-Applications-on-Linkedin.git
    ```

2. Navigate to the repository's directory:
    ```bash
    cd Automating-Job-Applications-on-Linkedin
    ```

3. Open the `main.py` file and enter your LinkedIn email and password in the specified fields:
    ```python
    username.send_keys("your_email")  # Enter your LinkedIn email
    password.send_keys("your_password")  # Enter your LinkedIn password
    ```

4. Run the script:
    ```bash
    python main.py
    ```

The script will open a Chrome browser, navigate to the LinkedIn job search page for Python Developer positions in Mumbai, and save the first job listing.

## Customization

You can modify the script to automatically apply for jobs instead of just saving them. To do this, you will need to:
- Find the appropriate HTML elements for the "Apply" button on the job listing page.
- Write additional code to handle the application process, such as uploading a resume and filling out application forms.

Here is a basic example of how you might extend the script to click the "Apply" button:

```python
# Example code to click the "Apply" button (assuming it's available on the job listing page)
apply_button = driver.find_element(By.XPATH, 'xpath_to_apply_button')
apply_button.click()

# You will need to handle additional steps such as filling out forms and submitting applications.
```

## Notes

- Be cautious when automating actions on LinkedIn to avoid violating their terms of service.
- This script is intended for educational purposes and personal use. Use it responsibly.
