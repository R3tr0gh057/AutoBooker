import asyncio
from playwright.async_api import async_playwright

# Define the URL and the button text to click
url = 'https://www.goethe.de/ins/in/en/sta/kol/prf/gzb2.cfm'
button_text = 'Select modules'
cookie_accept_button_text = 'Accept All'

async def try_click_button(page, window_number):
    try:
        # Locate the first "Select modules" button using nth=0 to target the first occurrence
        button = page.locator(f'button:has-text("{button_text}") >> nth=0')
        await button.wait_for(timeout=10000)  # Wait up to 10 seconds for the button to appear
        print(f"Clicking the button on window {window_number}...")
        await button.click()
        return True  # Return True if the button was successfully clicked
    except Exception as e:
        print(f"Window {window_number}: Button not found or could not be clicked: {e}")
        return False  # Return False if there was an issue

async def handle_cookie_modal(page):
    try:
        # Locate the "Accept All" button for the cookie modal
        cookie_button = page.locator(f'button:has-text("{cookie_accept_button_text}")')
        # Wait for the cookie button to appear, if it does
        await cookie_button.wait_for(timeout=5000)  # 5 seconds wait for the button to appear
        print("Cookie modal detected. Clicking 'Accept All'...")
        await cookie_button.click()  # Click the 'Accept All' button
    except Exception:
        # If the button isn't found within the timeout, we assume the modal didn't show
        print("No cookie modal detected. Continuing with the page.")

async def check_and_handle_error(page, window_number):
    # Check if the current page URL contains 'error'
    current_url = page.url
    if 'error' in current_url:
        print(f"Error detected in URL on window {window_number}. Refreshing the page...")
        await page.goto(url)  # Back to the main page
        return False  # Return False to indicate error handling
    return True  # Return True if no error detected

async def handle_window(page, window_number):
    # Check for cookie consent modal on page load
    await handle_cookie_modal(page)

    while True:
        # Refresh the page
        await page.reload()
        print(f"Page refreshed on window {window_number}.")

        # Attempt to click the "Select modules" button
        if await try_click_button(page, window_number):
            # Wait for a short period to allow the new page to load
            await asyncio.sleep(5)  # Adjust as needed

            # Check the URL of the new page
            if await check_and_handle_error(page, window_number):
                break  # Exit loop if no error was detected
            else:
                # Wait before retrying
                await asyncio.sleep(0.1)  # Adjust as needed

        # Wait before the next refresh attempt
        await asyncio.sleep(0.5)  # Adjust as needed

async def open_and_handle_window(browser, window_number):
    # Concurrent execution
    context = await browser.new_context()  # Create a new browser context (window)
    page = await context.new_page()  # Create a new page in that context
    print(f"Opening window {window_number}...")
    await page.goto(url)  # Navigate to the target URL
    await handle_window(page, window_number)  # Start handling this window immediately

async def open_multiple_windows_concurrently(number_of_windows):
    # Asyncio for concurrency
    async with async_playwright() as p:
        # Launch the browser in headed mode (with UI)
        browser = await p.chromium.launch(headless=False)  # Set headless=False for headed mode

        # Create tasks to open and handle windows concurrently
        tasks = [asyncio.create_task(open_and_handle_window(browser, i + 1)) for i in range(number_of_windows)]

        # Wait for all tasks to complete
        await asyncio.gather(*tasks)

        # Wait for user input to close the browser
        input('Press Enter to close the browser...')
        await browser.close()

# Ask the user how many windows they want to open
num_windows = int(input("How many windows would you like to open? "))

# Run the asynchronous function
asyncio.run(open_multiple_windows_concurrently(num_windows))