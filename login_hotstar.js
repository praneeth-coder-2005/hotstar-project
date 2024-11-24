const { chromium } = require('playwright'); // You can use 'firefox' or 'webkit' instead of 'chromium'
const fs = require('fs');

(async () => {
    try {
        // Launch the browser
        const browser = await chromium.launch({
            headless: false, // Set to false for debugging
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });

        const context = await browser.newContext();
        const page = await context.newPage();

        console.log('Navigating to Hotstar login page...');
        await page.goto('https://www.hotstar.com/', { waitUntil: 'networkidle' });

        // Wait for the login button
        console.log('Waiting for login button...');
        const loginButtonSelector = 'button[data-testid="user-menu-btn"]';
        await page.waitForSelector(loginButtonSelector, { timeout: 60000 });
        await page.click(loginButtonSelector);

        // Wait for mobile input
        console.log('Interacting with login modal...');
        const mobileInputSelector = 'input[type="tel"]';
        await page.waitForSelector(mobileInputSelector, { timeout: 60000 });
        await page.fill(mobileInputSelector, 'YOUR_MOBILE_NUMBER'); // Replace with your mobile number

        // Submit the mobile number
        const submitButtonSelector = 'button[type="submit"]';
        await page.waitForSelector(submitButtonSelector, { timeout: 60000 });
        await page.click(submitButtonSelector);

        // Wait for OTP entry
        console.log('Waiting for OTP...');
        const otpInputSelector = 'input[name="otp"]';
        await page.waitForSelector(otpInputSelector, { timeout: 120000 });

        // Pause to manually enter OTP
        console.log('Please enter the OTP manually...');
        await page.waitForTimeout(120000); // Wait 2 minutes for manual OTP entry

        // Save cookies after login
        const cookies = await context.cookies();
        fs.writeFileSync('hotstar_cookies.json', JSON.stringify(cookies, null, 2));
        console.log('Cookies saved to hotstar_cookies.json');

        console.log('Login successful!');
        await browser.close();
    } catch (err) {
        console.error('Error:', err.message);
        process.exit(1);
    }
})();
