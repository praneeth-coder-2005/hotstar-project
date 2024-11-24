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

        // Wait for the page to load fully
        console.log('Waiting for login button...');
        await page.waitForTimeout(5000);

        // Use an updated selector for the login button
        const loginButtonSelector = 'button[data-testid="user-menu-btn"]'; // Update this if necessary
        await page.waitForSelector(loginButtonSelector, { timeout: 60000 });
        await page.click(loginButtonSelector);

        // Wait and interact with the login modal
        console.log('Interacting with login modal...');
        const mobileInputSelector = 'input[type="tel"]';
        await page.waitForSelector(mobileInputSelector, { timeout: 60000 });
        await page.type(mobileInputSelector, 'YOUR_MOBILE_NUMBER', { delay: 100 }); // Replace with your mobile number

        // Submit the mobile number
        const submitButtonSelector = 'button[type="submit"]';
        await page.waitForSelector(submitButtonSelector, { timeout: 60000 });
        await page.click(submitButtonSelector);

        // Wait for OTP input
        console.log('Waiting for OTP...');
        const otpInputSelector = 'input[name="otp"]';
        await page.waitForSelector(otpInputSelector, { timeout: 120000 });

        // **Note**: Manually enter OTP here in the browser
        console.log('Please enter the OTP manually in the browser.');

        // Wait for user to complete the OTP entry and login
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
