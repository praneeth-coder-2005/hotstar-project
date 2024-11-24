const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    // Go to Hotstar login page
    await page.goto('https://www.hotstar.com/in', { waitUntil: 'networkidle2' });

    // Click login
    await page.click('button:contains("Sign In")');
    await page.waitForTimeout(2000);

    // Enter mobile number
    await page.type('input[type="tel"]', '<YOUR_PHONE_NUMBER>');
    await page.keyboard.press('Enter');
    console.log("Enter the OTP manually in the browser...");
    await page.waitForTimeout(60000); // Wait for OTP entry

    // Extract cookies
    const cookies = await page.cookies();
    const fs = require('fs');
    fs.writeFileSync('hotstar_cookies.json', JSON.stringify(cookies, null, 2));

    console.log("Cookies saved to hotstar_cookies.json");
    await browser.close();
})();
