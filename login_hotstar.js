const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: true, // Run in headless mode
    });
    const context = await browser.newContext();
    const page = await context.newPage();

    console.log('Navigating to Hotstar login page...');
    await page.goto('https://www.hotstar.com/');

    console.log('Waiting for login button...');
    await page.waitForSelector('[data-testid="login-button"]');
    await page.click('[data-testid="login-button"]');

    console.log('Hotstar login flow initiated...');
    await browser.close();
})();
