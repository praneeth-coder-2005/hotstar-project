const puppeteer = require('puppeteer');

(async () => {
    try {
        const browser = await puppeteer.launch({
            headless: true, // Set to false to debug visually
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });

        const page = await browser.newPage();

        console.log('Navigating to Hotstar login page...');
        await page.goto('https://www.hotstar.com/', { waitUntil: 'networkidle2' });

        // Click the login button
        console.log('Clicking login button...');
        await page.waitForSelector('[data-testid="login-button"]');
        await page.click('[data-testid="login-button"]');

        // Enter mobile number
        console.log('Entering mobile number...');
        await page.waitForSelector('input[type="tel"]');
        await page.type('input[type="tel"]', 'YOUR_MOBILE_NUMBER', { delay: 100 }); // Replace with your mobile number

        // Submit the mobile number
        console.log('Submitting mobile number...');
        await page.waitForSelector('button[type="submit"]');
        await page.click('button[type="submit"]');

        // Wait for OTP input
        console.log('Waiting for OTP...');
        await page.waitForSelector('input[type="tel"][name="otp"]', { timeout: 120000 });

        // **Note**: You must manually input the OTP here or implement an API to fetch OTP
        console.log('Please enter the OTP manually in the browser.');

        // Wait for user to manually enter the OTP
        await page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 300000 });

        // Save cookies after login
        const cookies = await page.cookies();
        const fs = require('fs');
        fs.writeFileSync('hotstar_cookies.json', JSON.stringify(cookies, null, 2));
        console.log('Cookies saved to hotstar_cookies.json');

        console.log('Login successful!');
        await browser.close();
    } catch (err) {
        console.error('Error:', err.message);
        process.exit(1);
    }
})();
