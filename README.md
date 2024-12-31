
---

# AutoBooker - Multi-Window Automation Script

**AutoBooker** is a Python script that automates the process of opening multiple browser windows and interacting with a web page. It can handle tasks such as clicking a button and accepting cookie consent modals. The script is designed to handle multiple windows concurrently, making it efficient for tasks like testing or automation during peak traffic.

This project is useful for automating tasks on websites, such as booking or registration processes.

## Features
- Open multiple **browser windows** (not tabs) concurrently.
- Detect and interact with a "Select modules" button on the page.
- Automatically detect and click on a cookie consent modal if it appears (e.g., "Accept All").
- Refresh the page and attempt button clicks periodically until successful.
- Handle errors like broken pages by refreshing the page.

## Prerequisites

- **Python 3.7+**
- **Playwright** (for browser automation)

## Installation

### Step 1: Install Python
Ensure that Python 3.7 or later is installed on your system. You can download it from [here](https://www.python.org/downloads/).

### Step 2: Install Playwright
To install Playwright and its necessary dependencies, run the following commands:

```bash
pip install playwright
python -m playwright install
```

This will install the Playwright library and download the required browser binaries.

### Step 3: Install Additional Dependencies (if needed)
If you encounter any missing dependencies, you can install them via:

```bash
pip install asyncio
```

## Usage

### Step 1: Run the Script
To run the script, use the following command in your terminal:

```bash
python main.py
```

### Step 2: Input Number of Windows
The script will prompt you to enter the number of browser windows you want to open. Input the desired number (e.g., `15` for 15 windows), and the script will proceed.

```bash
How many windows would you like to open? 15
```

### How It Works:
- **Opening Multiple Windows**: The script opens multiple **browser windows** (not tabs) using Playwright's **browser contexts**. Each window operates independently.
- **Cookie Modal Handling**: If the page displays a cookie consent modal with the text "Accept All," the script will click the button to accept the cookies.
- **Clicking the Button**: The script attempts to click the "Select modules" button. If the button isn't found, it will retry after refreshing the page.
- **Error Handling**: If any window encounters a page with an "error" in the URL, the script will refresh that page and attempt again.

## Example Output

```bash
How many windows would you like to open? 3
Opening window 1...
Opening window 2...
Opening window 3...
Cookie modal detected. Clicking 'Accept All'...
Page refreshed on window 1.
Clicking the button on window 1...
Page refreshed on window 2.
Clicking the button on window 2...
Page refreshed on window 3.
Clicking the button on window 3...
...
Press Enter to close the browser...
```

## Notes

- The script opens multiple windows concurrently, so you can monitor the progress of each window separately.
- **Headed Mode**: By default, the script runs in **headed mode** (with a visible browser UI). If you want to run the script without a UI (headless mode), you can change the following line in the script:
  
  ```python
  browser = await p.chromium.launch(headless=True)  # Set headless=True to run without UI
  ```

- **Page Refreshing**: The script refreshes the page periodically to ensure the latest version of the page is loaded and the button is clickable.
- **Retry Mechanism**: The script retries clicking the button and waits for a short period before trying again if the button isn't found.

## Troubleshooting

- **Playwright Not Installed**: If you encounter errors related to Playwright not being installed, make sure to run `python -m playwright install` after installing the package to download the necessary browser binaries.
  
- **Button Not Found**: If the script can't find the button, ensure that the selector you're using (`button:has-text("Select modules") >> nth=0`) is accurate for the page you're automating. You can refine the locator based on other unique attributes (like `id` or `class`).

- **Timeout Errors**: If you are dealing with slow page loads, you may increase the timeout value for `wait_for()` to give the page more time to load before clicking the button.

## License

This project is licensed under the **GPLv3 License**.

See the [LICENSE](./LICENSE) file for more details.

---

### **Example Folder Structure**:
```
AutoBooker/
├── main.py
├── README.md
└── LICENSE
```

---

